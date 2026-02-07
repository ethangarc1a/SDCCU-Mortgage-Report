# Mortgage Payment Analysis

Python project that calculates fixed-rate mortgage payments using the standard amortization formula and compares loan scenarios. Includes a sensitivity analysis showing how small APR changes affect monthly payment and total interest.

## What this does
- Computes **monthly payment**, **total paid**, and **total interest**
- Compares:
  - **Scenario A:** $600,000 @ 6.625% for 30 years
  - **Scenario B:** $600,000 @ 5.875% for 15 years
- Runs a **rate sensitivity analysis** on a $600,000 30-year loan (5.5% → 7.5%)

## Mortgage formula
Let:
- `P` = principal (loan amount)
- `r` = annual interest rate (decimal)
- `i = r / 12` = monthly interest rate
- `n = 12 * years` = number of payments

Monthly payment:
\[
M = \frac{P \cdot i}{1 - (1+i)^{-n}}
\]

## Requirements
- Python 3.9+
- numpy
- pandas

Install:
```bash
pip install numpy pandas
