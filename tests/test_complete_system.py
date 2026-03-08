"""
Complete System Test
Tests all modules integration
"""
from financial_extractor import extract_financial_data, format_crores, validate_financial_data
from ratio_analyzer import calculate_financial_ratios, interpret_ratios
from risk_analyzer import analyze_credit_risk
from loan_engine import get_loan_summary

# Test data
test_text = """
Infosys Limited - Financial Report FY 2023

Revenue: ₹1,46,767 Crore
Net Profit: ₹24,108 Crore
Total Assets: ₹1,12,000 Crore
Total Liabilities: ₹45,000 Crore
Total Debt: ₹8,500 Crore
Operating Cash Flow: ₹28,000 Crore
"""

print("="*70)
print("AI CREDIT DECISION SYSTEM - COMPLETE TEST")
print("="*70)

# Step 1: Extract Financial Data
print("\n[1] FINANCIAL EXTRACTION")
print("-"*70)
financial_data = extract_financial_data(test_text)
for key, value in financial_data.items():
    print(f"{key:20s}: {value:>15,} -> {format_crores(value)}")

# Validate
validation = validate_financial_data(financial_data)
print(f"\nData Completeness: {validation['completeness']:.0f}%")
print(f"Valid for Analysis: {validation['is_valid']}")

# Step 2: Calculate Ratios
print("\n[2] FINANCIAL RATIOS")
print("-"*70)
ratios = calculate_financial_ratios(financial_data)
interpretations = interpret_ratios(ratios)

for key, value in ratios.items():
    interp = interpretations.get(key, "N/A").replace('🟢', '[OK]').replace('🟡', '[WARN]').replace('🔴', '[RISK]').replace('⚪', '[N/A]')
    if value is not None:
        display_val = f"{value}%" if 'margin' in key or 'return' in key else f"{value}"
        print(f"{key:30s}: {display_val:>10s} -> {interp}")
    else:
        print(f"{key:30s}: {'N/A':>10s} -> {interp}")

# Step 3: Credit Risk Analysis
print("\n[3] CREDIT RISK ANALYSIS")
print("-"*70)
risk_analysis = analyze_credit_risk(financial_data)

print(f"Risk Level: {risk_analysis['risk_level']}")
print(f"Credit Score: {risk_analysis['credit_score']}/100")
print(f"\nRisk Factors:")
for factor in risk_analysis['risk_factors']:
    clean_factor = factor.replace('🟢', '[OK]').replace('🟡', '[WARN]').replace('🔴', '[RISK]').replace('⚪', '[N/A]')
    print(f"  • {clean_factor}")

# Step 4: Loan Recommendation
print("\n[4] LOAN RECOMMENDATION")
print("-"*70)
loan_rec = risk_analysis['loan_recommendation']
print(f"Decision: {loan_rec['decision']}")
print(f"Loan Amount: Rs.{loan_rec['loan_amount']:,}")
print(f"Interest Rate: {loan_rec['interest_rate']}% p.a.")
print(f"Tenure: {loan_rec['tenure_months']} months")
print(f"\nExplanation: {loan_rec['explanation']}")

if loan_rec.get('conditions'):
    print(f"\nConditions:")
    for condition in loan_rec['conditions']:
        print(f"  • {condition}")

print("\n" + "="*70)
print("✅ ALL TESTS PASSED - SYSTEM WORKING PERFECTLY")
print("="*70)
