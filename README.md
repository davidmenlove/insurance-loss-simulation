# Insurance Loss Simulation (Monte Carlo)

## Problem
Simulate an insurance portfolio and estimate the probability that total losses exceed a specified threshold.

## Approach
Modeled claim frequency using Bernoulli trials with probability 0.1 across 1,000 policyholders. For each claim, loss severity was simulated using a Uniform(500, 2000) distribution. Ran 1,000 simulations and calculated total loss for each simulation to estimate the probability of exceeding a loss threshold.

## Tools Used
- Python
- `random` module
- Loops and conditional logic

## Key Result
Estimated probability that total losses exceed $125,000 is approximately 48.7%. This is close to 50% since the threshold is near the expected total loss, with deviations driven by variability in claim frequency and severity.

## Example Output
Probability total loss exceeds $125,000:
 0.4870

## How to Run
Python simulation.py

## Interpretation
The expected total loss is approximately $125,000, calculated as:
- Expected number of claims: 1000 × 0.1 = 100  
- Expected severity per claim: (500 + 2000) / 2 = 1250  

This gives an expected total loss of 100 × 1250 = $125,000. Since the threshold is set at the expected value, the probability of exceeding it is close to 50%, though randomness in claim frequency and severity introduces variation.
