"""
Financial Ratio Analyzer Module
Calculates key financial ratios for credit assessment
"""
from typing import Dict, Optional

def calculate_financial_ratios(data: Dict[str, Optional[int]]) -> Dict[str, Optional[float]]:
    """
    Calculate key financial ratios
    Returns: Dict with profit_margin, debt_to_asset_ratio, asset_to_liability_ratio, etc.
    """
    ratios = {}
    
    # 1. Profit Margin (%)
    if data.get('net_profit') and data.get('revenue'):
        ratios['profit_margin'] = round((data['net_profit'] / data['revenue']) * 100, 2)
    else:
        ratios['profit_margin'] = None
    
    # 2. Debt-to-Asset Ratio
    if data.get('debt') and data.get('assets'):
        ratios['debt_to_asset_ratio'] = round(data['debt'] / data['assets'], 2)
    else:
        ratios['debt_to_asset_ratio'] = None
    
    # 3. Asset-to-Liability Ratio
    if data.get('assets') and data.get('liabilities'):
        ratios['asset_to_liability_ratio'] = round(data['assets'] / data['liabilities'], 2)
    else:
        ratios['asset_to_liability_ratio'] = None
    
    # 4. Cash Flow to Debt Ratio
    if data.get('cash_flow') and data.get('debt') and data['debt'] > 0:
        ratios['cash_flow_to_debt_ratio'] = round(data['cash_flow'] / data['debt'], 2)
    else:
        ratios['cash_flow_to_debt_ratio'] = None
    
    # 5. Return on Assets (ROA) %
    if data.get('net_profit') and data.get('assets'):
        ratios['return_on_assets'] = round((data['net_profit'] / data['assets']) * 100, 2)
    else:
        ratios['return_on_assets'] = None
    
    # 6. Current Ratio (simplified: Assets / Liabilities)
    if data.get('assets') and data.get('liabilities'):
        ratios['current_ratio'] = round(data['assets'] / data['liabilities'], 2)
    else:
        ratios['current_ratio'] = None
    
    return ratios

def interpret_ratios(ratios: Dict[str, Optional[float]]) -> Dict[str, str]:
    """
    Interpret financial ratios with business context
    Returns: Dict with interpretations
    """
    interpretations = {}
    
    # Profit Margin
    pm = ratios.get('profit_margin')
    if pm is not None:
        if pm >= 20:
            interpretations['profit_margin'] = "🟢 Excellent profitability"
        elif pm >= 10:
            interpretations['profit_margin'] = "🟡 Good profitability"
        elif pm >= 5:
            interpretations['profit_margin'] = "🟡 Moderate profitability"
        else:
            interpretations['profit_margin'] = "🔴 Low profitability"
    else:
        interpretations['profit_margin'] = "⚪ Not Available"
    
    # Debt-to-Asset Ratio
    dta = ratios.get('debt_to_asset_ratio')
    if dta is not None:
        if dta <= 0.3:
            interpretations['debt_to_asset_ratio'] = "🟢 Low debt burden"
        elif dta <= 0.6:
            interpretations['debt_to_asset_ratio'] = "🟡 Moderate debt"
        else:
            interpretations['debt_to_asset_ratio'] = "🔴 High debt risk"
    else:
        interpretations['debt_to_asset_ratio'] = "⚪ Not Available"
    
    # Asset-to-Liability Ratio
    atl = ratios.get('asset_to_liability_ratio')
    if atl is not None:
        if atl >= 2.0:
            interpretations['asset_to_liability_ratio'] = "🟢 Strong financial position"
        elif atl >= 1.5:
            interpretations['asset_to_liability_ratio'] = "🟡 Adequate coverage"
        elif atl >= 1.0:
            interpretations['asset_to_liability_ratio'] = "🟡 Minimal coverage"
        else:
            interpretations['asset_to_liability_ratio'] = "🔴 Negative equity"
    else:
        interpretations['asset_to_liability_ratio'] = "⚪ Not Available"
    
    # Cash Flow to Debt Ratio
    cfd = ratios.get('cash_flow_to_debt_ratio')
    if cfd is not None:
        if cfd >= 0.5:
            interpretations['cash_flow_to_debt_ratio'] = "🟢 Strong debt servicing"
        elif cfd >= 0.2:
            interpretations['cash_flow_to_debt_ratio'] = "🟡 Adequate cash flow"
        else:
            interpretations['cash_flow_to_debt_ratio'] = "🔴 Weak cash flow"
    else:
        interpretations['cash_flow_to_debt_ratio'] = "⚪ Not Available"
    
    # Return on Assets
    roa = ratios.get('return_on_assets')
    if roa is not None:
        if roa >= 10:
            interpretations['return_on_assets'] = "🟢 Excellent asset efficiency"
        elif roa >= 5:
            interpretations['return_on_assets'] = "🟡 Good asset efficiency"
        else:
            interpretations['return_on_assets'] = "🔴 Poor asset efficiency"
    else:
        interpretations['return_on_assets'] = "⚪ Not Available"
    
    return interpretations

def get_ratio_benchmarks() -> Dict[str, Dict[str, str]]:
    """Return industry benchmarks for reference"""
    return {
        "profit_margin": {
            "excellent": ">= 20%",
            "good": "10-20%",
            "moderate": "5-10%",
            "poor": "< 5%"
        },
        "debt_to_asset_ratio": {
            "low": "<= 0.3",
            "moderate": "0.3-0.6",
            "high": "> 0.6"
        },
        "asset_to_liability_ratio": {
            "strong": ">= 2.0",
            "adequate": "1.5-2.0",
            "minimal": "1.0-1.5",
            "negative": "< 1.0"
        },
        "cash_flow_to_debt_ratio": {
            "strong": ">= 0.5",
            "adequate": "0.2-0.5",
            "weak": "< 0.2"
        }
    }
