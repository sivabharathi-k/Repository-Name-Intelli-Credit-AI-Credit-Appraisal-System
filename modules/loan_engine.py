"""
Loan Recommendation Engine
Provides intelligent loan decisions based on financial analysis
"""
from typing import Dict, Optional, Tuple

def calculate_loan_recommendation(
    financial_data: Dict[str, Optional[float]],
    ratios: Dict[str, Optional[float]],
    credit_score: int,
    risk_level: str
) -> Dict[str, any]:
    """
    Generate loan recommendation based on comprehensive analysis
    Returns: loan decision, amount, interest rate, terms
    """
    
    recommendation = {
        "decision": "REJECTED",
        "loan_amount": 0,
        "interest_rate": 0.0,
        "tenure_months": 0,
        "conditions": [],
        "explanation": ""
    }
    
    # Extract key metrics
    revenue = financial_data.get('revenue', 0)
    assets = financial_data.get('assets', 0)
    net_profit = financial_data.get('net_profit', 0)
    
    # Decision Logic
    if credit_score >= 70 and risk_level == "LOW":
        recommendation["decision"] = "APPROVED"
        recommendation["loan_amount"] = int(min(revenue * 0.5, assets * 0.4) if revenue and assets else 0)
        recommendation["interest_rate"] = 8.5
        recommendation["tenure_months"] = 60
        recommendation["explanation"] = "✅ Strong financial position with low risk profile"
        
    elif credit_score >= 50 and risk_level in ["LOW", "MEDIUM"]:
        recommendation["decision"] = "APPROVED"
        recommendation["loan_amount"] = int(min(revenue * 0.3, assets * 0.25) if revenue and assets else 0)
        recommendation["interest_rate"] = 11.5
        recommendation["tenure_months"] = 48
        recommendation["conditions"] = [
            "Quarterly financial reporting required",
            "Maintain minimum debt-to-asset ratio < 0.6"
        ]
        recommendation["explanation"] = "✅ Approved with conditions - moderate risk profile"
        
    elif credit_score >= 35:
        recommendation["decision"] = "CONDITIONAL"
        recommendation["loan_amount"] = int(min(revenue * 0.15, assets * 0.15) if revenue and assets else 0)
        recommendation["interest_rate"] = 14.5
        recommendation["tenure_months"] = 36
        recommendation["conditions"] = [
            "Collateral required (150% of loan amount)",
            "Personal guarantee from directors",
            "Monthly financial reporting",
            "Maintain minimum cash reserves"
        ]
        recommendation["explanation"] = "⚠️ Conditional approval - requires additional security"
        
    else:
        recommendation["decision"] = "REJECTED"
        recommendation["loan_amount"] = 0
        recommendation["interest_rate"] = 0.0
        recommendation["tenure_months"] = 0
        recommendation["explanation"] = "❌ High risk profile - loan application rejected"
        recommendation["conditions"] = [
            "Improve profitability",
            "Reduce debt burden",
            "Strengthen cash flow",
            "Reapply after 6 months with improved financials"
        ]
    
    return recommendation

def calculate_emi(loan_amount: float, interest_rate: float, tenure_months: int) -> int:
    """Calculate monthly EMI"""
    if loan_amount == 0 or tenure_months == 0:
        return 0
    
    monthly_rate = interest_rate / (12 * 100)
    emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** tenure_months) / (((1 + monthly_rate) ** tenure_months) - 1)
    return int(emi)

def get_loan_summary(recommendation: Dict[str, any]) -> str:
    """Generate human-readable loan summary"""
    decision = recommendation["decision"]
    amount = recommendation["loan_amount"]
    rate = recommendation["interest_rate"]
    tenure = recommendation["tenure_months"]
    
    if decision == "APPROVED":
        emi = calculate_emi(amount, rate, tenure)
        return f"""
🎉 **LOAN APPROVED**

**Loan Amount:** Rs.{amount:,}
**Interest Rate:** {rate}% per annum
**Tenure:** {tenure} months ({tenure//12} years)
**Monthly EMI:** Rs.{emi:,}
**Total Repayment:** Rs.{emi * tenure:,}

{recommendation['explanation']}
"""
    
    elif decision == "CONDITIONAL":
        emi = calculate_emi(amount, rate, tenure)
        conditions_text = "\n".join([f"• {c}" for c in recommendation["conditions"]])
        return f"""
⚠️ **CONDITIONAL APPROVAL**

**Loan Amount:** Rs.{amount:,}
**Interest Rate:** {rate}% per annum
**Tenure:** {tenure} months ({tenure//12} years)
**Monthly EMI:** Rs.{emi:,}

**Conditions:**
{conditions_text}

{recommendation['explanation']}
"""
    
    else:
        recommendations_text = "\n".join([f"• {c}" for c in recommendation["conditions"]])
        return f"""
❌ **LOAN REJECTED**

{recommendation['explanation']}

**Recommendations for Improvement:**
{recommendations_text}
"""

def calculate_max_loan_capacity(
    revenue: Optional[float],
    assets: Optional[float],
    net_profit: Optional[float],
    existing_debt: Optional[float]
) -> Dict[str, int]:
    """Calculate maximum loan capacity based on different methods"""
    
    capacity = {
        "revenue_based": 0,
        "asset_based": 0,
        "profit_based": 0,
        "recommended": 0
    }
    
    if revenue:
        capacity["revenue_based"] = int(revenue * 0.5)  # 50% of annual revenue
    
    if assets:
        capacity["asset_based"] = int(assets * 0.4)  # 40% of total assets
    
    if net_profit:
        capacity["profit_based"] = int(net_profit * 5)  # 5x annual profit
    
    # Recommended is the minimum of all methods (conservative approach)
    non_zero = [v for v in capacity.values() if v > 0]
    if non_zero:
        capacity["recommended"] = min(non_zero)
    
    return capacity
