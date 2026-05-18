from __future__ import annotations

import math

import numpy as np


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def black_scholes_call(s0: float, k: float, r: float, sigma: float, t: float) -> float:
    d1 = (math.log(s0 / k) + (r + 0.5 * sigma**2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    return s0 * normal_cdf(d1) - k * math.exp(-r * t) * normal_cdf(d2)


def monte_carlo_call(
    s0: float,
    k: float,
    r: float,
    sigma: float,
    t: float,
    simulations: int = 200_000,
    seed: int = 42,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(simulations // 2)
    z = np.concatenate([z, -z])

    st = s0 * np.exp((r - 0.5 * sigma**2) * t + sigma * math.sqrt(t) * z)
    payoff = np.maximum(st - k, 0)
    discounted = math.exp(-r * t) * payoff
    price = float(discounted.mean())
    standard_error = float(discounted.std(ddof=1) / math.sqrt(len(discounted)))
    return price, standard_error


def main() -> None:
    s0 = 100.0
    k = 105.0
    r = 0.04
    sigma = 0.25
    t = 1.0

    bs_price = black_scholes_call(s0, k, r, sigma, t)
    mc_price, mc_se = monte_carlo_call(s0, k, r, sigma, t)

    print("Pricing de call europea")
    print(f"Black-Scholes: {bs_price:.4f}")
    print(f"Monte Carlo:   {mc_price:.4f}")
    print(f"Std error MC:  {mc_se:.4f}")
    print(f"Diferencia:    {mc_price - bs_price:.4f}")


if __name__ == "__main__":
    main()
