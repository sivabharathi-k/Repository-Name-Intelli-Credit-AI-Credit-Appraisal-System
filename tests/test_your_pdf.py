from financial_extractor import extract_financial_data, format_crores, validate_financial_data

# Your actual PDF content (incomplete)
incomplete_text = """Infosys Limited - Company Financial Overview
(Sample Report)
Company Overview: Infosys Limited is a global IT services and consulting company headquartered
in Bengaluru, India. The company provides digital services, cloud solutions, AI, and business
consulting services to organizations across multiple industries worldwide.
Financial Highlights (FY 2023 Approx.)
Revenue n1,46,767 Crore
Net Profit n24,108 Crore
Employees 343,000+
Global Clients 1800+
Headquarters Bengaluru, India"""

print("="*70)
print("TESTING YOUR ACTUAL PDF (Incomplete Data)")
print("="*70)

data = extract_financial_data(incomplete_text)
validation = validate_financial_data(data)

print("\nExtracted Data:")
print("-"*70)
for key, value in data.items():
    formatted = format_crores(value)
    status = "[OK]" if value else "[MISSING]"
    print(f"{key:20s}: {formatted:>25s}  {status}")

print(f"\nValidation:")
print(f"Completeness: {validation['completeness']:.0f}%")
print(f"Valid for Analysis: {validation['is_valid']}")

print("\n" + "="*70)
print("DIAGNOSIS:")
print("="*70)
print("Your PDF only contains 2 of 6 required metrics.")
print("Missing: Assets, Liabilities, Debt, Cash Flow")
print("\nSOLUTION: Upload PDFs with complete financial statements")
print("="*70)
