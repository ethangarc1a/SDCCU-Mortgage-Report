import numpy as np
import pandas as pd

def calculate_mortgage(principal, annual_rate, years):
    """
    Calculates monthly payment, total payment, and total interest.
    
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (e.g., 0.065 for 6.5%)
        years (int): Loan term in years
        
    Returns:
        dict: Monthly payment, Total Paid, Total Interest
    """
    if annual_rate == 0:
        return {
            "Monthly Payment": principal / (years * 12),
            "Total Paid": principal,
            "Total Interest": 0
        }
    
    # Convert to monthly parameters
    i = annual_rate / 12
    n = years * 12
    
    # Formula: M = (P * i) / (1 - (1+i)^-n)
    monthly_payment = (principal * i) / (1 - (1 + i)**(-n))
    
    total_paid = monthly_payment * n
    total_interest = total_paid - principal
    
    return {
        "Monthly Payment": round(monthly_payment, 2),
        "Total Paid": round(total_paid, 2),
        "Total Interest": round(total_interest, 2)
    }

# --- Base Case Scenarios for SDCCU ---
# Scenario A: 30-Year Fixed (Standard San Diego Family Home)
# Principal: $600,000, Rate: 6.625%
scenario_a = calculate_mortgage(600000, 0.06625, 30)

# Scenario B: 15-Year Fixed (Aggressive Payoff)
# Principal: $600,000, Rate: 5.875% (Typically lower rate for shorter term)
scenario_b = calculate_mortgage(600000, 0.05875, 15)


def format_currency(x: float) -> str:
    return f"${x:,.2f}"

# Build DataFrame from scenarios
results_df = pd.DataFrame.from_dict(
    {
        "Scenario A: 30-yr @ 6.625%": scenario_a,
        "Scenario B: 15-yr @ 5.875%": scenario_b,
    },
    orient="index"
)

# Apply currency formatting
for col in results_df.columns:
    results_df[col] = results_df[col].apply(format_currency)

print("\n--- BASE SCENARIO RESULTS ---")
print(results_df.to_string())
