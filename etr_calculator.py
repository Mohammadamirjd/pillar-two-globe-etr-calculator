import pandas as pd


MINIMUM_RATE = 0.15




def calculate_etr(globe_income, covered_taxes):
if globe_income <= 0:
return 0
return covered_taxes / globe_income




def calculate_top_up_tax(globe_income, etr):
if etr >= MINIMUM_RATE:
return 0
return (MINIMUM_RATE - etr) * globe_income




def process_data(file_path):
df = pd.read_csv(file_path)


df['ETR'] = df.apply(
lambda x: calculate_etr(x['GloBE_Income'], x['Covered_Taxes']),
axis=1
)


df['Top_Up_Tax'] = df.apply(
lambda x: calculate_top_up_tax(x['GloBE_Income'], x['ETR']),
axis=1
)


df['ETR_Percentage'] = df['ETR'] * 100


return df




if __name__ == '__main__':
input_file = 'data/sample_financials.csv'
results = process_data(input_file)


print("Pillar Two – Jurisdictional ETR Results")
print(results)