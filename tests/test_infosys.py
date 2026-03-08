from financial_extractor import extract_financial_data, format_indian_currency

text = """Infosys Limited - Company Financial Overview
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

print("Testing Infosys extraction...")
data = extract_financial_data(text)
print("\nExtracted Data:")
for key, value in data.items():
    print(f"{key}: {value} -> {format_indian_currency(value)}")
