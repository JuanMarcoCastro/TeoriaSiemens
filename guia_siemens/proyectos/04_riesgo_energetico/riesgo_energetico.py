from __future__ import annotations

import numpy as np
import pandas as pd


def run_simulation(simulations: int = 100_000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    demand_mwh = rng.lognormal(mean=np.log(1_200), sigma=0.18, size=simulations)
    price_usd_mwh = rng.lognormal(mean=np.log(82), sigma=0.22, size=simulations)
    outage_event = rng.binomial(1, 0.08, size=simulations)
    outage_hours = outage_event * rng.exponential(scale=3.0, size=simulations)

    energy_cost = demand_mwh * price_usd_mwh
    downtime_cost = outage_hours * 18_000
    total_cost = energy_cost + downtime_cost

    return pd.DataFrame(
        {
            "demand_mwh": demand_mwh,
            "price_usd_mwh": price_usd_mwh,
            "outage_hours": outage_hours,
            "energy_cost": energy_cost,
            "downtime_cost": downtime_cost,
            "total_cost": total_cost,
        }
    )


def summarize(results: pd.DataFrame, budget: float = 135_000) -> pd.Series:
    total = results["total_cost"]
    return pd.Series(
        {
            "mean_cost": total.mean(),
            "median_cost": total.median(),
            "p90_cost": total.quantile(0.90),
            "p95_cost": total.quantile(0.95),
            "p99_cost": total.quantile(0.99),
            "prob_over_budget": (total > budget).mean(),
            "mean_outage_hours": results["outage_hours"].mean(),
        }
    )


def main() -> None:
    results = run_simulation()
    summary = summarize(results)

    print("Simulacion de riesgo energetico")
    print(summary.round(2))

    worst = results.nlargest(5, "total_cost")
    print("\nCinco escenarios mas costosos:")
    print(worst.round(2).to_string(index=False))


if __name__ == "__main__":
    main()

