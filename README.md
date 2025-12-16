Pillar Two – GloBE Effective Tax Rate (ETR) Calculator

This repository provides a mid-level, fully functional Python-based engine for calculating the jurisdictional Effective Tax Rate (ETR) under OECD Pillar Two (GloBE Rules).

The project is designed to demonstrate:

Strong understanding of international tax law (Pillar Two)

Ability to translate legal rules into executable logic

Practical use of Python for tax compliance and policy analysis

This is suitable for PhD applications, Big4 tax technology roles, OECD-related research, and legal-tech portfolios.

1. Legal Scope Covered

GloBE Income calculation (simplified)

Covered Taxes

Jurisdictional blending

Effective Tax Rate (ETR)

Top-up Tax computation (15% minimum tax)

⚠️ This model is educational and analytical, not a substitute for official compliance software.


2. Methodology (Legal → Code)
ETR Formula (Article 5 GloBE Rules)
ETR = Covered Taxes / GloBE Income
Top-up Tax Formula:
Top-up Tax = (15% − ETR) × GloBE Income
If ETR ≥ 15%, then Top-up Tax = 0.

4. How to Run

Step 1: Install dependencies:

pip install pandas

Step 2: Run the calculator

4. Example Output

Jurisdiction	GloBE Income	Covered Taxes	ETR (%)	Top-up Tax
Germany	1,000,000	120,000	12.0	30,000
Ireland	800,000	60,000	7.5	60,000
UAE	500,000	25,000	5.0	50,000

5. Why This Project Matters

This repository shows:

A) Practical understanding of OECD Pillar Two mechanics

B) Capability to build tax engines, not just theoretical analysis

C) Readiness for advanced tax research or tax-tech roles

6. Possible Extensions

A) Deferred tax adjustments (Article 4.4)

B) Substance-based income exclusion (PPE)

C) UTPR and IIR logic

D) Streamlit dashboard

E) R-based visualization module

7. Legal References

OECD (2021): Global Anti-Base Erosion Model Rules (Pillar Two)

OECD Commentary and Administrative Guidance

8. Author
Mohammadamir Modami
MSc International Law – International Tax Focus

Python | R | Tax Technology | OECD Pillar Two
