"""
Feature Engineering Layer
Combines financial, operational, and research signals for ML model
"""
import numpy as np
from typing import Dict, Optional, List

def engineer_financial_features(financial_data: Dict[str, Optional[float]]) -> Dict[str, float]:
    """
    Engineer features from financial data
    Returns: Dictionary of engineered features
    """
    features = {}
    
    # Extract base metrics
    revenue = financial_data.get('revenue') or 0
    net_profit = financial_data.get('net_profit') or 0
    assets = financial_data.get('assets') or 0
    liabilities = financial_data.get('liabilities') or 0
    debt = financial_data.get('debt') or 0
    cash_flow = financial_data.get('cash_flow') or 0
    
    # Feature 1: Profit Margin (%)
    features['profit_margin'] = (net_profit / revenue * 100) if revenue > 0 else 0
    
    # Feature 2: Debt-to-Asset Ratio
    features['debt_to_asset_ratio'] = (debt / assets) if assets > 0 else 0
    
    # Feature 3: Asset-to-Liability Ratio
    features['asset_to_liability_ratio'] = (assets / liabilities) if liabilities > 0 else 0
    
    # Feature 4: Cash Flow to Debt Ratio
    features['cash_flow_to_debt_ratio'] = (cash_flow / debt) if debt > 0 else 0
    
    # Feature 5: Return on Assets (%)
    features['return_on_assets'] = (net_profit / assets * 100) if assets > 0 else 0
    
    # Feature 6: Debt Service Coverage (simplified)
    features['debt_service_coverage'] = (cash_flow / debt) if debt > 0 else 0
    
    # Feature 7: Revenue Scale (log normalized)
    features['revenue_scale'] = np.log10(revenue + 1)
    
    # Feature 8: Profitability Score (0-100)
    profit_score = min(100, (net_profit / revenue * 100) * 5) if revenue > 0 else 0
    features['profitability_score'] = profit_score
    
    # Feature 9: Leverage Score (0-100, inverse of debt ratio)
    leverage_score = max(0, 100 - (debt / assets * 100)) if assets > 0 else 50
    features['leverage_score'] = leverage_score
    
    # Feature 10: Liquidity Score (0-100)
    liquidity_score = min(100, (cash_flow / debt * 50)) if debt > 0 else 100
    features['liquidity_score'] = liquidity_score
    
    return features

def engineer_research_features(research_data: Optional[Dict]) -> Dict[str, float]:
    """
    Engineer features from external research
    Returns: Dictionary of research-based features
    """
    features = {}
    
    if not research_data:
        # Default values when research not available
        features['sentiment_score'] = 0.0
        features['risk_signal_count'] = 0
        features['news_negativity'] = 0.0
        features['research_risk_score'] = 50.0
        return features
    
    # Feature 1: Sentiment Score (-1 to 1, normalized to 0-100)
    sentiment_raw = research_data.get('sentiment_score', 0.0)
    features['sentiment_score'] = (sentiment_raw + 1) * 50  # Convert to 0-100
    
    # Feature 2: Risk Signal Count
    features['risk_signal_count'] = len(research_data.get('risk_signals', []))
    
    # Feature 3: News Negativity (0-100)
    sentiment = research_data.get('sentiment', 'Neutral')
    if sentiment == 'Negative':
        features['news_negativity'] = 75.0
    elif sentiment == 'Neutral':
        features['news_negativity'] = 50.0
    else:
        features['news_negativity'] = 25.0
    
    # Feature 4: Research Risk Score (0-100)
    # Higher risk signals = higher risk score
    risk_count = features['risk_signal_count']
    base_risk = 50
    risk_penalty = min(40, risk_count * 10)
    sentiment_adjustment = (50 - features['sentiment_score']) * 0.3
    features['research_risk_score'] = min(100, base_risk + risk_penalty + sentiment_adjustment)
    
    return features

def create_ml_feature_vector(
    financial_data: Dict[str, Optional[float]],
    research_data: Optional[Dict] = None
) -> Dict[str, float]:
    """
    Create complete feature vector for ML model
    Returns: Dictionary of all engineered features
    """
    # Combine all features
    features = {}
    
    # Financial features
    financial_features = engineer_financial_features(financial_data)
    features.update(financial_features)
    
    # Research features
    research_features = engineer_research_features(research_data)
    features.update(research_features)
    
    # Composite features
    # Feature: Overall Financial Health Score (0-100)
    financial_health = (
        features['profitability_score'] * 0.3 +
        features['leverage_score'] * 0.3 +
        features['liquidity_score'] * 0.4
    )
    features['financial_health_score'] = financial_health
    
    # Feature: Combined Risk Score (0-100)
    # Lower is better
    combined_risk = (
        (100 - financial_health) * 0.6 +
        features['research_risk_score'] * 0.4
    )
    features['combined_risk_score'] = combined_risk
    
    return features

def get_feature_names() -> List[str]:
    """Return list of feature names for ML model"""
    return [
        'profit_margin',
        'debt_to_asset_ratio',
        'asset_to_liability_ratio',
        'cash_flow_to_debt_ratio',
        'return_on_assets',
        'debt_service_coverage',
        'revenue_scale',
        'profitability_score',
        'leverage_score',
        'liquidity_score',
        'sentiment_score',
        'risk_signal_count',
        'news_negativity',
        'research_risk_score',
        'financial_health_score',
        'combined_risk_score'
    ]

def prepare_ml_input(features: Dict[str, float]) -> List[float]:
    """
    Prepare feature vector for ML model input
    Returns: List of feature values in correct order
    """
    feature_names = get_feature_names()
    return [features.get(name, 0.0) for name in feature_names]
