"""
Test Complete ML Credit Intelligence System
"""
from ml_credit_engine import analyze_credit_application, get_explainability_report

# Sample company data
company_name = "Infosys Limited"

financial_text = """
Infosys Limited - Annual Financial Report FY 2023

Financial Highlights:
Revenue: Rs.1,46,767 Crore
Net Profit: Rs.24,108 Crore
Total Assets: Rs.1,12,000 Crore
Total Liabilities: Rs.45,000 Crore
Total Debt: Rs.8,500 Crore
Operating Cash Flow: Rs.28,000 Crore

Company is a leading IT services provider with strong market position.
"""

# Simulated research data
research_data = {
    'sentiment': 'Positive',
    'sentiment_score': 0.3,
    'risk_signals': [],
    'articles_analyzed': 5,
    'research_summary': 'Positive outlook with no major risks detected'
}

print("="*80)
print("INTELLI-CREDIT: ML-POWERED CREDIT APPRAISAL SYSTEM")
print("="*80)

print(f"\nAnalyzing: {company_name}")
print("-"*80)

# Run complete analysis
results = analyze_credit_application(financial_text, company_name, research_data)

# Display results
print("\n[1] FINANCIAL DATA EXTRACTION")
print("-"*80)
from financial_extractor import format_crores
for key, value in results['financial_data'].items():
    print(f"{key:20s}: {format_crores(value)}")

print(f"\nData Completeness: {results['validation']['completeness']:.0f}%")

print("\n[2] ML FEATURE ENGINEERING")
print("-"*80)
key_features = ['profit_margin', 'debt_to_asset_ratio', 'liquidity_score', 
                'financial_health_score', 'research_risk_score']
for feature in key_features:
    value = results['ml_features'].get(feature, 0)
    print(f"{feature:30s}: {value:8.2f}")

print("\n[3] ML RISK PREDICTION")
print("-"*80)
ml_pred = results['ml_prediction']
print(f"Risk Level:           {ml_pred['risk_level']}")
print(f"Credit Score:         {ml_pred['credit_score']}/100")
print(f"Default Probability:  {ml_pred['probability_of_default']:.2%}")
print(f"Model Confidence:     {ml_pred['model_confidence']:.1%}")

print("\n[4] LOAN RECOMMENDATION")
print("-"*80)
loan = results['loan_recommendation']
print(f"Decision:        {loan['decision']}")
print(f"Loan Amount:     Rs.{loan['loan_amount']:,.0f}")
print(f"Interest Rate:   {loan['interest_rate']}% p.a.")
print(f"Tenure:          {loan['tenure_months']} months")

print("\n[5] ML EXPLAINABILITY")
print("-"*80)
print("Key Decision Factors:")
for explanation in ml_pred['explanations']:
    print(f"  {explanation}")

print("\n[6] CAM SUMMARY")
print("-"*80)
print(results['cam_summary'])

print("\n[7] FEATURE IMPORTANCE")
print("-"*80)
for feature, importance in sorted(
    ml_pred['feature_importance'].items(),
    key=lambda x: x[1],
    reverse=True
)[:5]:
    bar = "█" * int(importance * 30)
    print(f"{feature:30s} {importance:5.1%} {bar}")

print("\n" + "="*80)
print("[SUCCESS] ML CREDIT INTELLIGENCE SYSTEM WORKING")
print("="*80)

# Save CAM report
with open('CAM_Report_Infosys.txt', 'w', encoding='utf-8') as f:
    f.write(results['cam_report'])

print("\n[CAM Report saved to: CAM_Report_Infosys.txt]")

# Generate explainability report
explainability = get_explainability_report(ml_pred, results['ml_features'])
with open('ML_Explainability_Report.txt', 'w', encoding='utf-8') as f:
    f.write(explainability)

print("[Explainability Report saved to: ML_Explainability_Report.txt]")
