from __future__ import annotations

import numpy as np
import pandas as pd


def simulate_energy_demand(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2024-01-01", periods=24 * 180, freq="h")
    hour = dates.hour
    day_of_week = dates.dayofweek
    t = np.arange(len(dates))

    daily_cycle = 18 * np.sin(2 * np.pi * (hour - 7) / 24)
    weekly_effect = np.where(day_of_week >= 5, -10, 0)
    trend = 0.006 * t
    temperature = 24 + 7 * np.sin(2 * np.pi * t / (24 * 365)) + rng.normal(0, 2.5, len(dates))
    cooling_load = np.maximum(temperature - 22, 0) * 2.2
    noise = rng.normal(0, 5, len(dates))

    demand_mwh = 95 + daily_cycle + weekly_effect + trend + cooling_load + noise

    return pd.DataFrame(
        {
            "timestamp": dates,
            "temperature_c": temperature,
            "demand_mwh": demand_mwh,
        }
    )


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["hour"] = out["timestamp"].dt.hour
    out["day_of_week"] = out["timestamp"].dt.dayofweek
    out["month"] = out["timestamp"].dt.month
    out["is_weekend"] = (out["day_of_week"] >= 5).astype(int)
    out["lag_1"] = out["demand_mwh"].shift(1)
    out["lag_24"] = out["demand_mwh"].shift(24)
    out["rolling_24"] = out["demand_mwh"].shift(1).rolling(24).mean()
    return out.dropna()


def fit_ridge_regression(x: np.ndarray, y: np.ndarray, alpha: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std[std == 0] = 1.0
    x_scaled = (x - mean) / std
    design = np.column_stack([np.ones(len(x_scaled)), x_scaled])

    penalty = np.eye(design.shape[1]) * alpha
    penalty[0, 0] = 0.0
    beta = np.linalg.solve(design.T @ design + penalty, design.T @ y)
    return beta, mean, std


def predict_ridge(x: np.ndarray, beta: np.ndarray, mean: np.ndarray, std: np.ndarray) -> np.ndarray:
    x_scaled = (x - mean) / std
    design = np.column_stack([np.ones(len(x_scaled)), x_scaled])
    return design @ beta


def mean_absolute_error(y_true: pd.Series, y_pred: np.ndarray | pd.Series) -> float:
    return float(np.mean(np.abs(np.asarray(y_true) - np.asarray(y_pred))))


def root_mean_squared_error(y_true: pd.Series, y_pred: np.ndarray | pd.Series) -> float:
    return float(np.sqrt(np.mean((np.asarray(y_true) - np.asarray(y_pred)) ** 2)))


def main() -> None:
    df = simulate_energy_demand()
    model_df = add_features(df)

    split_idx = int(len(model_df) * 0.8)
    train = model_df.iloc[:split_idx]
    test = model_df.iloc[split_idx:]

    features = [
        "temperature_c",
        "hour",
        "day_of_week",
        "month",
        "is_weekend",
        "lag_1",
        "lag_24",
        "rolling_24",
    ]

    beta, mean, std = fit_ridge_regression(train[features].to_numpy(), train["demand_mwh"].to_numpy(), alpha=10.0)
    prediction = predict_ridge(test[features].to_numpy(), beta, mean, std)
    naive = test["lag_24"]

    model_mae = mean_absolute_error(test["demand_mwh"], prediction)
    model_rmse = root_mean_squared_error(test["demand_mwh"], prediction)
    naive_mae = mean_absolute_error(test["demand_mwh"], naive)
    naive_rmse = root_mean_squared_error(test["demand_mwh"], naive)

    print("Forecast energetico")
    print(f"Filas simuladas: {len(df):,}")
    print(f"Modelo ridge - MAE: {model_mae:.2f}, RMSE: {model_rmse:.2f}")
    print(f"Naive lag24 - MAE: {naive_mae:.2f}, RMSE: {naive_rmse:.2f}")

    coefficients = pd.Series(beta[1:], index=features).sort_values(key=np.abs, ascending=False)
    print("\nCoeficientes estandarizados:")
    print(coefficients.round(3))


if __name__ == "__main__":
    main()
