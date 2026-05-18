from __future__ import annotations

import numpy as np
import pandas as pd


def simulate_returns(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    assets = ["energia", "tech", "bonos", "industrial"]
    annual_mu = np.array([0.09, 0.13, 0.04, 0.08])
    annual_vol = np.array([0.22, 0.30, 0.07, 0.18])
    corr = np.array(
        [
            [1.00, 0.45, -0.10, 0.55],
            [0.45, 1.00, -0.20, 0.50],
            [-0.10, -0.20, 1.00, -0.05],
            [0.55, 0.50, -0.05, 1.00],
        ]
    )

    cov = np.outer(annual_vol, annual_vol) * corr / 252
    daily_mu = annual_mu / 252
    returns = rng.multivariate_normal(daily_mu, cov, size=252 * 3)
    return pd.DataFrame(returns, columns=assets)


def portfolio_metrics(weights: np.ndarray, mean_returns: np.ndarray, cov: np.ndarray, rf: float) -> dict[str, float]:
    annual_return = float(weights @ mean_returns * 252)
    annual_vol = float(np.sqrt(weights @ (cov * 252) @ weights))
    sharpe = (annual_return - rf) / annual_vol
    return {"return": annual_return, "volatility": annual_vol, "sharpe": sharpe}


def main() -> None:
    returns = simulate_returns()
    mean_returns = returns.mean().to_numpy()
    cov = returns.cov().to_numpy()
    rf = 0.035
    rng = np.random.default_rng(7)

    rows = []
    for _ in range(50_000):
        weights = rng.dirichlet(np.ones(len(returns.columns)))
        metrics = portfolio_metrics(weights, mean_returns, cov, rf)
        rows.append({**metrics, **dict(zip(returns.columns, weights))})

    portfolios = pd.DataFrame(rows)
    best_sharpe = portfolios.loc[portfolios["sharpe"].idxmax()]
    min_vol = portfolios.loc[portfolios["volatility"].idxmin()]

    print("Portafolio Markowitz por simulacion")
    print("\nMejor Sharpe:")
    print(best_sharpe.round(4))
    print("\nMenor volatilidad:")
    print(min_vol.round(4))


if __name__ == "__main__":
    main()

