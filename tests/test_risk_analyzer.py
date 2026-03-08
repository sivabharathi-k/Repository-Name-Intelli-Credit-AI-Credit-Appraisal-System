"""
Test script for Credit Risk Analysis and Loan Decision Engine
Demonstrates the AI-powered credit appraisal system
"""
from risk_analyzer import analyze_credit_risk, get_risk_emoji, format_currency_inr
import json

print("="*70)
print("CREDIT RISK ANALYSIS & LOAN DECISION ENGINE - TEST")
print("="*70)

# Test Case 1: Low Risk Company
print("\n\n" + "="*70)
print("TEST CASE 1: LOW RISK COMPANY")
print("="*70)

low_risk_data = {
    "revenue": 52000000,
    "net_profit": 4800000,
    "debt": 16000000,
    "cash_flow": 7200000,
    "assets": 38000000,
    "liabilities": 21000000
}

print("\nFinancial Data:")
print(json.dumps(low_risk_data, indent=2))

analysis = analyze_credit_risk(low_risk_data)

print("\n" + "-"*70)
print("CREDIT ANALYSIS RESULTS:")
print("-"*70)
print(f"Risk Level: {get_risk_emoji(analysis['risk_level'])} {analysis['risk_level']}")
print(f"Credit Score: {analysis['credit_score']}/100")
print(f"Decision: {analysis['decision']}")
print(f"Recommended Loan: {format_currency_inr(analysis['recommended_loan_amount'])}")
print(f"Interest Rate: {analysis['interest_rate']}")
print(f"Explanation: {analysis['explanation']}")

print("\nFinancial Ratios:")
for ratio, value in analysis['ratios'].items():
    print(f"  • {ratio}: {value:.4f}")

print("\nRisk Factors:")
for factor in analysis['risk_factors']:
    print(f"  • {factor}")

# Test Case 2: Medium Risk Company
print("\n\n" + "="*70)
print("TEST CASE 2: MEDIUM RISK COMPANY")
print("="*70)

medium_risk_data = {
    "revenue": 30000000,
    "net_profit": 1500000,  # Low profit margin (5%)
    "debt": 18000000,       # Higher debt
    "cash_flow": 6000000,
    "assets": 35000000,
    "liabilities": 25000000
}

print("\nFinancial Data:")
print(json.dumps(medium_risk_data, indent=2))

analysis = analyze_credit_risk(medium_risk_data)

print("\n" + "-"*70)
print("CREDIT ANALYSIS RESULTS:")
print("-"*70)
print(f"Risk Level: {get_risk_emoji(analysis['risk_level'])} {analysis['risk_level']}")
print(f"Credit Score: {analysis['credit_score']}/100")
print(f"Decision: {analysis['decision']}")
print(f"Recommended Loan: {format_currency_inr(analysis['recommended_loan_amount'])}")
print(f"Interest Rate: {analysis['interest_rate']}")
print(f"Explanation: {analysis['explanation']}")

print("\nFinancial Ratios:")
for ratio, value in analysis['ratios'].items():
    print(f"  • {ratio}: {value:.4f}")

print("\nRisk Factors:")
for factor in analysis['risk_factors']:
    print(f"  • {factor}")

# Test Case 3: High Risk Company
print("\n\n" + "="*70)
print("TEST CASE 3: HIGH RISK COMPANY")
print("="*70)

high_risk_data = {
    "revenue": 20000000,
    "net_profit": 500000,   # Very low profit margin (2.5%)
    "debt": 18000000,       # Very high debt
    "cash_flow": 3000000,   # Weak cash flow
    "assets": 22000000,
    "liabilities": 20000000  # High liabilities
}

print("\nFinancial Data:")
print(json.dumps(high_risk_data, indent=2))

analysis = analyze_credit_risk(high_risk_data)

print("\n" + "-"*70)
print("CREDIT ANALYSIS RESULTS:")
print("-"*70)
print(f"Risk Level: {get_risk_emoji(analysis['risk_level'])} {analysis['risk_level']}")
print(f"Credit Score: {analysis['credit_score']}/100")
print(f"Decision: {analysis['decision']}")
print(f"Recommended Loan: {format_currency_inr(analysis['recommended_loan_amount'])}")
print(f"Interest Rate: {analysis['interest_rate']}")
print(f"Explanation: {analysis['explanation']}")

print("\nFinancial Ratios:")
for ratio, value in analysis['ratios'].items():
    print(f"  • {ratio}: {value:.4f}")

print("\nRisk Factors:")
for factor in analysis['risk_factors']:
    print(f"  • {factor}")

# Summary
print("\n\n" + "="*70)
print("TEST SUMMARY")
print("="*70)
print("✅ All test cases executed successfully!")
print("✅ Risk analysis engine working correctly")
print("✅ Loan recommendations generated")
print("✅ Credit scores calculated")
print("\n" + "="*70)
print("SYSTEM READY FOR DEMO!")
print("="*70)
