"""
Test script for Financial Data Extraction Engine
Demonstrates how the extraction works with sample data
"""
from financial_extractor import extract_financial_data, format_indian_currency, calculate_financial_ratios
import json

# Sample financial text (as extracted from PDF)
sample_text = """
FINANCIAL STATEMENT - FY 2023-24

Company Performance Overview:

Revenue: ₹5,20,00,000
Net Profit: ₹48,00,000
Total Debt: ₹1,60,00,000
Operating Cash Flow: ₹72,00,000
Total Assets: ₹3,80,00,000
Total Liabilities: ₹2,10,00,000

The company has shown strong growth this year.
"""

print("="*60)
print("FINANCIAL DATA EXTRACTION TEST")
print("="*60)

# Extract financial data
print("\n1. Extracting financial metrics...")
financial_data = extract_financial_data(sample_text)

print("\n2. Extracted Data (JSON):")
print(json.dumps(financial_data, indent=2))

print("\n3. Formatted Display:")
print(f"Revenue: {format_indian_currency(financial_data['revenue'])}")
print(f"Net Profit: {format_indian_currency(financial_data['net_profit'])}")
print(f"Total Debt: {format_indian_currency(financial_data['debt'])}")
print(f"Operating Cash Flow: {format_indian_currency(financial_data['cash_flow'])}")
print(f"Total Assets: {format_indian_currency(financial_data['assets'])}")
print(f"Total Liabilities: {format_indian_currency(financial_data['liabilities'])}")

# Calculate ratios
print("\n4. Financial Ratios:")
ratios = calculate_financial_ratios(financial_data)
for ratio_name, ratio_value in ratios.items():
    print(f"{ratio_name}: {ratio_value}")

print("\n" + "="*60)
print("TEST COMPLETED SUCCESSFULLY!")
print("="*60)

# Test different formats
print("\n\nTesting Different Currency Formats:")
print("="*60)

test_cases = [
    "Revenue: ₹5,20,00,000",
    "Sales: Rs 52000000",
    "Profit: 5.2 Crore",
    "Debt: 48 Lakh",
    "Assets: 3.8 Cr",
]

for test in test_cases:
    result = extract_financial_data(test)
    print(f"\nInput: {test}")
    print(f"Output: {result}")
