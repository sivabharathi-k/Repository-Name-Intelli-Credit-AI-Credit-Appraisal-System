"""
Test Universal Financial Extractor with Real-World Formats
"""
from financial_extractor import extract_financial_data, format_crores, validate_financial_data

# Test Case 1: Bank Report Format (HDFC Bank style)
bank_report = """
HDFC Bank Limited - Quarterly Results

Financial Performance (Q4 FY23)

Total Income: 99200.03 crore
Interest Earned: 85432.50 crore
Operating Profit: 25678.90 crore
Net Profit: 18155.21 crore

Balance Sheet:
Total Assets: 23,50,000 crore
Total Liabilities: 21,80,000 crore
Total Borrowings: 15,20,000 crore

Cash Flow:
Operating Cash Flow: 45000 crore
"""

# Test Case 2: Company Annual Report Format
company_report = """
Infosys Limited - Annual Report FY 2023

Revenue: ₹1,46,767 Crore
Net Profit: ₹24,108 Crore
Total Assets: ₹1,12,000 Crore
Total Liabilities: ₹45,000 Crore
Total Debt: ₹8,500 Crore
Operating Cash Flow: ₹28,000 Crore
"""

# Test Case 3: Decimal Format
decimal_report = """
Financial Highlights

Total Revenue    146767.50
Profit After Tax 24108.30
Total Assets     112000.00
Liabilities      45000.00
Debt             8500.00
Cash Flow        28000.00
"""

# Test Case 4: Mixed Format
mixed_report = """
Q3 Results

Total Income: Rs. 99,200.03 crore
Net Income: 18155.21 crore
Assets: 2350000 lakh
Borrowings: 1520000 lakh
"""

test_cases = [
    ("Bank Report (HDFC Style)", bank_report),
    ("Company Annual Report", company_report),
    ("Decimal Format", decimal_report),
    ("Mixed Format", mixed_report)
]

print("="*80)
print("UNIVERSAL FINANCIAL EXTRACTOR - COMPREHENSIVE TEST")
print("="*80)

for name, text in test_cases:
    print(f"\n{'='*80}")
    print(f"TEST: {name}")
    print(f"{'='*80}")
    
    data = extract_financial_data(text)
    validation = validate_financial_data(data)
    
    print(f"\nExtracted Data:")
    print(f"{'-'*80}")
    for key, value in data.items():
        formatted = format_crores(value)
        status = "OK" if value else "MISSING"
        print(f"{key:20s}: {formatted:>25s}  [{status}]")
    
    print(f"\nValidation:")
    print(f"Completeness: {validation['completeness']:.0f}%")
    print(f"Valid: {validation['is_valid']}")
    
    if validation['warnings']:
        print(f"\nWarnings:")
        for warning in validation['warnings']:
            print(f"  {warning}")
    
    # Summary
    if validation['completeness'] >= 80:
        print(f"\n[SUCCESS] Extraction quality: EXCELLENT")
    elif validation['completeness'] >= 50:
        print(f"\n[PARTIAL] Extraction quality: GOOD")
    else:
        print(f"\n[WARNING] Extraction quality: NEEDS IMPROVEMENT")

print(f"\n{'='*80}")
print("TEST COMPLETE")
print(f"{'='*80}")
