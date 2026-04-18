import random


def estimate_loss_exceedance_probability(
    num_policyholders: int,
    claim_probability: float,
    num_simulations: int,
    loss_threshold: float
) -> float:

    num_exceedances = 0

    for _ in range(num_simulations):
        total_loss = 0.0

        for _ in range(num_policyholders):
            if random.random() <= claim_probability:
                total_loss += random.uniform(500, 2000)

        if total_loss > loss_threshold:
            num_exceedances += 1

    return num_exceedances / num_simulations


def main():
    num_policyholders = 1000
    claim_probability = 0.1
    num_simulations = 1000
    loss_threshold = 125000

    probability = estimate_loss_exceedance_probability(
        num_policyholders,
        claim_probability,
        num_simulations,
        loss_threshold
    )

    print(f"Probability total loss exceeds ${loss_threshold:,.0f}:\n {probability:.4f}")


if __name__ == "__main__":
    main()
