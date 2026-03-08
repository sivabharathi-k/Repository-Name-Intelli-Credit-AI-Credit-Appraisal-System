# -*- coding: utf-8 -*-
"""
Test script for Financial Data Extraction Engine
"""
from financial_extractor import extract_financial_data, format_indian_currency, calculate_financial_ratios
import json

sample_text = """
FINANCIAL STATEMENT - FY 2023-24

Revenue: ₹5,20,00,000
Net Profit: ₹48,00,000
Total Debt: ₹1,60,00,000
Operating Cash Flow: ₹72,00,000
Total Assets: ₹3,80,00,000
Total Liabilities: ₹2,10,00,000
"""

print("="*60)
print("FINANCIAL DATA EXTRACTION TEST")
print("="*60)

financial_data = extract_financial_data(sample_text)

print("\nExtracted Data (JSON):")
print(json.dumps(financial_data, indent=2))

print("\nFormatted Display:")
for key, value in financial_data.items():
    print(f"{key}: {format_indian_currency(value)}")

print("\nFinancial Ratios:")
ratios = calculate_financial_ratios(financial_data)
for ratio_name, ratio_value in ratios.items():
    print(f"{ratio_name}: {ratio_value}")

print("\n" + "="*60)
print("TEST COMPLETED!")
print("="*60)

# Test Crore format
print("\n\nTesting Crore Format:")
crore_text = """
Revenue: 1,46,767 Crore
Net Profit: 24,108 Crore
Total Assets: 1,20,000 Crore
"""

print("Input text:")
print(crore_text)

crore_data = extract_financial_data(crore_text)
print("\nExtracted:")
print(json.dumps(crore_data, indent=2))

print("\nFormatted:")
for key, value in crore_data.items():
    if value:
        print(f"{key}: {format_indian_currency(value)}")
