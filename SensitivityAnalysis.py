# Sensitivity Analysis: Effect of Interest Rate on a $600,000 30-Year Loan
rates = [0.055, 0.060, 0.065, 0.070, 0.075] # 5.5% to 7.5%
principal = 600000
term = 30

results_list = []

for r in rates:
    res = calculate_mortgage(principal, r, term)
    results_list.append({
        "Rate (%)": f"{r*100:.1f}%",
        "Monthly Payment": f"${res['Monthly Payment']:,.2f}",
        "Total Interest": f"${res['Total Interest']:,.2f}"
    })

# Display as a dataframe-like table
df_results = pd.DataFrame(results_list)
print("\n--- SENSITIVITY ANALYSIS: INTEREST RATES ---")
print(df_results.to_string(index=False))
