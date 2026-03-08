"""
Credit Risk Analysis Engine - PRODUCTION VERSION
Integrates ratio analysis and loan engine for comprehensive credit assessment
"""
from typing import Dict, Optional
from modules.ratio_analyzer import calculate_financial_ratios, interpret_ratios
from modules.loan_engine import calculate_loan_recommendation, get_loan_summary

def determine_risk_level(ratios: Dict[str, Optional[float]], financial_data: Dict[str, Optional[int]]) -> tuple:
    """
    Determine risk level using rule-based AI logic
    Returns: (risk_level, risk_factors, risk_score)
    """
    risk_factors = []
    risk_score = 0
    
    # Rule 1: Debt to Asset Ratio
    debt_ratio = ratios.get('debt_to_asset_ratio')
    if debt_ratio is not None:
        if debt_ratio > 0.7:
            risk_score += 3
            risk_factors.append("🔴 High debt burden (>70% of assets)")
        elif debt_ratio > 0.5:
            risk_score += 2
            risk_factors.append("🟡 Moderate debt levels (50-70% of assets)")
        else:
            risk_factors.append("🟢 Healthy debt levels (<50% of assets)")
    
    # Rule 2: Profit Margin
    profit_margin = ratios.get('profit_margin')
    if profit_margin is not None:
        if profit_margin < 5:
            risk_score += 3
            risk_factors.append("🔴 Low profitability (<5% margin)")
        elif profit_margin < 10:
            risk_score += 1
            risk_factors.append("🟡 Moderate profitability (5-10% margin)")
        else:
            risk_factors.append("🟢 Strong profitability (>10% margin)")
    
    # Rule 3: Cash Flow Strength
    cash_flow_ratio = ratios.get('cash_flow_to_debt_ratio')
    if cash_flow_ratio is not None:
        if cash_flow_ratio < 0.3:
            risk_score += 2
            risk_factors.append("🔴 Weak cash flow coverage")
        elif cash_flow_ratio < 0.5:
            risk_score += 1
            risk_factors.append("🟡 Adequate cash flow")
        else:
            risk_factors.append("🟢 Strong cash flow generation")
    
    # Rule 4: Asset to Liability Ratio
    asset_liability_ratio = ratios.get('asset_to_liability_ratio')
    if asset_liability_ratio is not None:
        if asset_liability_ratio < 1.2:
            risk_score += 2
            risk_factors.append("🔴 Limited asset coverage")
        elif asset_liability_ratio < 1.5:
            risk_score += 1
            risk_factors.append("🟡 Moderate asset coverage")
        else:
            risk_factors.append("🟢 Strong asset coverage")
    
    # Rule 5: Revenue Check
    if not financial_data.get('revenue'):
        risk_score += 2
        risk_factors.append("⚠️ Revenue data not available")
    
    # Determine risk level
    if risk_score >= 6:
        risk_level = "HIGH"
    elif risk_score >= 3:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    return risk_level, risk_factors, risk_score

def calculate_credit_score(risk_level: str, ratios: Dict[str, Optional[float]], risk_score: int) -> int:
    """
    Calculate credit score (0-100) based on comprehensive analysis
    """
    # Base score by risk level
    if risk_level == "LOW":
        base_score = 85
    elif risk_level == "MEDIUM":
        base_score = 60
    else:
        base_score = 30
    
    # Adjustments based on specific ratios
    adjustments = 0
    
    # Profit margin bonus
    profit_margin = ratios.get('profit_margin')
    if profit_margin is not None:
        if profit_margin > 20:
            adjustments += 10
        elif profit_margin > 15:
            adjustments += 5
    
    # Debt ratio penalty
    debt_ratio = ratios.get('debt_to_asset_ratio')
    if debt_ratio is not None:
        if debt_ratio > 0.7:
            adjustments -= 15
        elif debt_ratio > 0.5:
            adjustments -= 8
    
    # Cash flow bonus
    cash_flow_ratio = ratios.get('cash_flow_to_debt_ratio')
    if cash_flow_ratio is not None:
        if cash_flow_ratio > 0.5:
            adjustments += 8
        elif cash_flow_ratio > 0.3:
            adjustments += 4
    
    # ROA bonus
    roa = ratios.get('return_on_assets')
    if roa is not None:
        if roa > 10:
            adjustments += 5
    
    credit_score = max(0, min(100, base_score + adjustments))
    return credit_score

def analyze_credit_risk(financial_data: Dict[str, Optional[int]]) -> Dict[str, any]:
    """
    Main function: Comprehensive credit risk analysis
    Returns: Complete analysis with risk level, credit score, and loan recommendation
    """
    # Validate input
    if not financial_data or not any(financial_data.values()):
        return {
            "risk_level": "UNKNOWN",
            "credit_score": 0,
            "loan_recommendation": {
                "decision": "REJECTED",
                "loan_amount": 0,
                "interest_rate": 0.0,
                "explanation": "❌ Insufficient financial data for analysis"
            },
            "ratios": {},
            "ratio_interpretations": {},
            "risk_factors": ["⚠️ No financial data available"],
            "data_completeness": 0
        }
    
    # Calculate ratios
    ratios = calculate_financial_ratios(financial_data)
    ratio_interpretations = interpret_ratios(ratios)
    
    # Determine risk level
    risk_level, risk_factors, risk_score_value = determine_risk_level(ratios, financial_data)
    
    # Calculate credit score
    credit_score = calculate_credit_score(risk_level, ratios, risk_score_value)
    
    # Generate loan recommendation
    loan_recommendation = calculate_loan_recommendation(
        financial_data, ratios, credit_score, risk_level
    )
    
    # Calculate data completeness
    found_count = sum(1 for v in financial_data.values() if v is not None)
    data_completeness = (found_count / len(financial_data)) * 100
    
    # Compile complete analysis
    analysis = {
        "risk_level": risk_level,
        "credit_score": credit_score,
        "loan_recommendation": loan_recommendation,
        "ratios": ratios,
        "ratio_interpretations": ratio_interpretations,
        "risk_factors": risk_factors,
        "data_completeness": data_completeness
    }
    
    return analysis

def get_risk_emoji(risk_level: str) -> str:
    """Get emoji indicator for risk level"""
    risk_emojis = {
        "LOW": "🟢",
        "MEDIUM": "🟡",
        "HIGH": "🔴",
        "UNKNOWN": "⚪"
    }
    return risk_emojis.get(risk_level, "⚪")

def get_decision_emoji(decision: str) -> str:
    """Get emoji for loan decision"""
    decision_emojis = {
        "APPROVED": "✅",
        "CONDITIONAL": "⚠️",
        "REJECTED": "❌"
    }
    return decision_emojis.get(decision, "❓")
