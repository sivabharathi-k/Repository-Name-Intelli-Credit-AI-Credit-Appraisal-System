from financial_extractor import extract_financial_data, format_indian_currency, calculate_financial_ratios

text = """Infosys Limited - Company Financial Overview
(Sample Report)

Company Overview: Infosys Limited is a global IT services and consulting company headquartered
in Bengaluru, India. The company provides digital services, cloud solutions, AI, and business
consulting services to organizations across multiple industries worldwide.

Financial Highlights (FY 2023 Approx.)
Revenue: ₹1,46,767 Crore
Net Profit: ₹24,108 Crore
Total Assets: ₹1,12,000 Crore
Total Liabilities: ₹45,000 Crore
Total Debt: ₹8,500 Crore
Operating Cash Flow: ₹28,000 Crore

Employees: 343,000+
Global Clients: 1800+
Headquarters: Bengaluru, India"""

print("Testing Complete Infosys extraction...")
data = extract_financial_data(text)
print("\nExtracted Data:")
for key, value in data.items():
    print(f"{key}: {value} -> {format_indian_currency(value)}")

print("\nFinancial Ratios:")
ratios = calculate_financial_ratios(data)
for key, value in ratios.items():
    print(f"{key}: {value}")
