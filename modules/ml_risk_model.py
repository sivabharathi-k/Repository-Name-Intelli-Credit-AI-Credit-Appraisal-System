"""
ML-Based Credit Risk Model
Uses trained RandomForest or falls back to rule-based system
"""
import numpy as np
import pickle
from typing import Dict, Tuple, List
from pathlib import Path
from modules.model_loader import load_credit_model, is_model_available

# Simulated pre-trained model (in production, load actual trained model)
class CreditRiskModel:
    """ML-based credit risk prediction model"""
    
    def __init__(self):
        self.model_path = Path("models/credit_risk_model.pkl")
        self.is_trained = False
        
    def predict_risk(self, features: List[float]) -> Tuple[str, float, Dict[str, float]]:
        """
        Predict credit risk using trained ML model or rule-based fallback
        Returns: (risk_level, probability_of_default, feature_importance)
        """
        # Try to use trained model first
        model_data = load_credit_model()
        
        if model_data is not None:
            return self._predict_with_ml_model(features, model_data)
        else:
            return self._predict_with_rules(features)
        
        # Extract key features
        profit_margin = features[0] if len(features) > 0 else 0
        debt_ratio = features[1] if len(features) > 1 else 0
        liquidity = features[9] if len(features) > 9 else 0
        research_risk = features[13] if len(features) > 13 else 50
        financial_health = features[14] if len(features) > 14 else 50
        
        # Calculate risk score (0-100, higher = more risky)
        risk_score = 0
        
        # Profitability factor
        if profit_margin < 5:
            risk_score += 25
        elif profit_margin < 10:
            risk_score += 15
        elif profit_margin < 15:
            risk_score += 5
        
        # Debt factor
        if debt_ratio > 0.7:
            risk_score += 25
        elif debt_ratio > 0.5:
            risk_score += 15
        elif debt_ratio > 0.3:
            risk_score += 5
        
        # Liquidity factor
        if liquidity < 30:
            risk_score += 20
        elif liquidity < 50:
            risk_score += 10
        
        # Research factor
        if research_risk > 70:
            risk_score += 15
        elif research_risk > 50:
            risk_score += 5
        
        # Financial health factor
        if financial_health < 40:
            risk_score += 15
        elif financial_health < 60:
            risk_score += 5
        
        # Determine risk level
        if risk_score <= 30:
            risk_level = "LOW"
            probability_of_default = 0.05 + (risk_score / 300)
        elif risk_score <= 60:
            risk_level = "MEDIUM"
            probability_of_default = 0.15 + (risk_score / 200)
        else:
            risk_level = "HIGH"
            probability_of_default = 0.35 + (risk_score / 150)
        
        # Cap probability at 0.95
        probability_of_default = min(0.95, probability_of_default)
        
        # Feature importance (simulated SHAP values)
        feature_importance = {
            'profit_margin': 0.20,
            'debt_to_asset_ratio': 0.18,
            'liquidity_score': 0.15,
            'financial_health_score': 0.15,
            'research_risk_score': 0.12,
            'cash_flow_to_debt_ratio': 0.10,
            'sentiment_score': 0.05,
            'risk_signal_count': 0.05
        }
        
        return risk_level, probability_of_default, feature_importance
    
    def _predict_with_ml_model(self, features: List[float], model_data: Dict) -> Tuple[str, float, Dict[str, float]]:
        """
        Predict using trained RandomForest model
        """
        model = model_data['model']
        feature_columns = model_data['feature_columns']
        
        # Prepare features for model (first 9 features match training)
        model_features = features[:9]
        
        # Predict
        prediction = model.predict([model_features])[0]
        probability = model.predict_proba([model_features])[0]
        
        # Probability of default (class 1)
        prob_default = probability[1]
        
        # Determine risk level
        if prob_default < 0.3:
            risk_level = "LOW"
        elif prob_default < 0.6:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"
        
        # Get feature importance from model
        feature_importance = {}
        for i, col in enumerate(feature_columns):
            feature_importance[col] = float(model.feature_importances_[i])
        
        return risk_level, prob_default, feature_importance
    
    def _predict_with_rules(self, features: List[float]) -> Tuple[str, float, Dict[str, float]]:
        """
        Rule-based prediction (fallback)
        """
    
    def get_credit_score(self, probability_of_default: float) -> int:
        """
        Convert probability of default to credit score (0-100)
        Lower PD = Higher score
        """
        # Inverse relationship: PD 0.05 -> Score 95, PD 0.95 -> Score 5
        credit_score = int((1 - probability_of_default) * 100)
        return max(0, min(100, credit_score))
    
    def explain_prediction(
        self,
        features: List[float],
        feature_names: List[str],
        feature_importance: Dict[str, float]
    ) -> List[str]:
        """
        Generate human-readable explanation of prediction
        Returns: List of explanation strings
        """
        explanations = []
        
        # Map features to values
        feature_dict = dict(zip(feature_names, features))
        
        # Analyze key factors
        profit_margin = feature_dict.get('profit_margin', 0)
        if profit_margin > 15:
            explanations.append(f"✅ Strong profitability ({profit_margin:.1f}% margin)")
        elif profit_margin > 10:
            explanations.append(f"🟡 Moderate profitability ({profit_margin:.1f}% margin)")
        else:
            explanations.append(f"🔴 Low profitability ({profit_margin:.1f}% margin)")
        
        debt_ratio = feature_dict.get('debt_to_asset_ratio', 0)
        if debt_ratio < 0.3:
            explanations.append(f"✅ Low debt burden ({debt_ratio:.2f} ratio)")
        elif debt_ratio < 0.6:
            explanations.append(f"🟡 Moderate debt levels ({debt_ratio:.2f} ratio)")
        else:
            explanations.append(f"🔴 High debt burden ({debt_ratio:.2f} ratio)")
        
        liquidity = feature_dict.get('liquidity_score', 0)
        if liquidity > 70:
            explanations.append(f"✅ Strong liquidity position (score: {liquidity:.0f})")
        elif liquidity > 40:
            explanations.append(f"🟡 Adequate liquidity (score: {liquidity:.0f})")
        else:
            explanations.append(f"🔴 Weak liquidity (score: {liquidity:.0f})")
        
        research_risk = feature_dict.get('research_risk_score', 50)
        if research_risk < 40:
            explanations.append(f"✅ Positive external signals (risk: {research_risk:.0f})")
        elif research_risk < 60:
            explanations.append(f"🟡 Neutral external signals (risk: {research_risk:.0f})")
        else:
            explanations.append(f"🔴 Negative external signals (risk: {research_risk:.0f})")
        
        return explanations

def predict_credit_risk(features: List[float], feature_names: List[str]) -> Dict:
    """
    Main function: Predict credit risk using ML model
    Returns: Complete prediction results with explanations
    """
    model = CreditRiskModel()
    
    # Get prediction
    risk_level, prob_default, feature_importance = model.predict_risk(features)
    
    # Calculate credit score
    credit_score = model.get_credit_score(prob_default)
    
    # Generate explanations
    explanations = model.explain_prediction(features, feature_names, feature_importance)
    
    # Compile results
    results = {
        'risk_level': risk_level,
        'credit_score': credit_score,
        'probability_of_default': prob_default,
        'feature_importance': feature_importance,
        'explanations': explanations,
        'model_confidence': 0.85  # Simulated confidence
    }
    
    return results
