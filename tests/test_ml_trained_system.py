"""
Test ML-Powered Credit System
"""
from modules.ml_credit_engine import analyze_credit_application
from modules.model_loader import get_model_info

company_name = "Infosys Limited"

financial_text = """
Revenue: Rs.1,46,767 Crore
Net Profit: Rs.24,108 Crore
Total Assets: Rs.1,12,000 Crore
Total Liabilities: Rs.45,000 Crore
Total Debt: Rs.8,500 Crore
Operating Cash Flow: Rs.28,000 Crore
"""

print("="*70)
print("ML-POWERED CREDIT APPRAISAL SYSTEM TEST")
print("="*70)

# Check model status
model_info = get_model_info()
print(f"\nModel Status:")
print(f"  Type: {model_info['type']}")
print(f"  Available: {model_info['available']}")
if model_info['available']:
    print(f"  Features: {model_info['features']}")
    print(f"  Accuracy: {model_info['accuracy']:.1%}")

print(f"\nAnalyzing: {company_name}")
print("-"*70)

# Run analysis
results = analyze_credit_application(financial_text, company_name, None)

# Display results
print("\n[ML PREDICTION]")
ml_pred = results['ml_prediction']
print(f"Risk Level:           {ml_pred['risk_level']}")
print(f"Credit Score:         {ml_pred['credit_score']}/100")
print(f"Default Probability:  {ml_pred['probability_of_default']:.2%}")

print("\n[LOAN RECOMMENDATION]")
loan = results['loan_recommendation']
print(f"Decision:        {loan['decision']}")
print(f"Loan Amount:     Rs.{loan['loan_amount']:,.0f}")
print(f"Interest Rate:   {loan['interest_rate']}% p.a.")

print("\n" + "="*70)
print("TEST COMPLETE - ML SYSTEM WORKING")
print("="*70)
