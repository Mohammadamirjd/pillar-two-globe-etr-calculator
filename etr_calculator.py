import pandas as pd

# OECD Pillar Two minimum effective tax rate
MINIMUM_RATE = 0.15


def process_data(file_path):
    """
    Processes jurisdiction-level financial data and computes
    GloBE Effective Tax Rate (ETR) and Top-Up Tax in accordance
    with OECD Pillar Two principles.
    """

    # Load input financial data
    df = pd.read_csv(file_path)

    # Validate presence of required input columns
    required_columns = {'GloBE_Income', 'Covered_Taxes', 'Substance_Exclusion'}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Sanitize numeric inputs to avoid NaN-related calculation errors
    df[['GloBE_Income', 'Covered_Taxes', 'Substance_Exclusion']] = (
        df[['GloBE_Income', 'Covered_Taxes', 'Substance_Exclusion']]
        .fillna(0)
    )

    # Compute Excess Profit after applying the Substance-Based Income Exclusion (SBIE)
    # Excess Profit cannot be negative under Pillar Two rules
    df['Excess_Profit'] = (
        df['GloBE_Income'] - df['Substance_Exclusion']
    ).clip(lower=0)

    # Initialize ETR column
    df['ETR'] = 0.0

    # Calculate Effective Tax Rate only where GloBE Income is positive
    # Negative ETRs are not permitted and are floored at zero
    positive_income_mask = df['GloBE_Income'] > 0
    df.loc[positive_income_mask, 'ETR'] = (
        df.loc[positive_income_mask, 'Covered_Taxes'] /
        df.loc[positive_income_mask, 'GloBE_Income']
    ).clip(lower=0)

    # Initialize Top-Up Tax column
    df['Top_Up_Tax'] = 0.0

    # Compute Top-Up Tax for low-taxed jurisdictions
    # The Top-Up Tax is applied only to Excess Profit
    low_tax_mask = df['ETR'] < MINIMUM_RATE
    df.loc[low_tax_mask, 'Top_Up_Tax'] = (
        (MINIMUM_RATE - df.loc[low_tax_mask, 'ETR']) *
        df.loc[low_tax_mask, 'Excess_Profit']
    )

    # Prepare reporting-friendly output fields
    df['ETR_Percentage'] = (df['ETR'] * 100).round(2)
    df['Top_Up_Tax'] = df['Top_Up_Tax'].round(2)

    return df


if __name__ == '__main__':
    # Entry point for standalone execution
    input_file = 'data/sample_financials.csv'

    # Run Pillar Two computations
    results = process_data(input_file)

    # Display jurisdictional ETR and Top-Up Tax results
    print("Pillar Two – Jurisdictional ETR Results")
    print(results)
