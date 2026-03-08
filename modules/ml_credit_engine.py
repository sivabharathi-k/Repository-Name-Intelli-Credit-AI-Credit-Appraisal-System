"""
Integrated ML Credit Intelligence Engine
Combines all modules for end-to-end credit appraisal
"""
from typing import Dict, Optional, Tuple
from modules.financial_extractor import extract_financial_data, validate_financial_data
from modules.feature_engineering import create_ml_feature_vector, get_feature_names, prepare_ml_input
from modules.ml_risk_model import predict_credit_risk
from modules.loan_engine import calculate_loan_recommendation
from modules.cam_generator import generate_cam_report, generate_cam_summary

def analyze_credit_application(
    text: str,
    company_name: str,
    research_data: Optional[Dict] = None
) -> Dict:
    """
    Complete ML-powered credit analysis pipeline
    
    Pipeline:
    1. Extract financial data
    2. Engineer features
    3. ML risk prediction
    4. Loan recommendation
    5. Generate CAM report
    
    Returns: Complete analysis results
    """
    
    # Step 1: Data Ingestion & Financial Extraction
    financial_data = extract_financial_data(text)
    validation = validate_financial_data(financial_data)
    
    # Step 2: Feature Engineering
    ml_features = create_ml_feature_vector(financial_data, research_data)
    feature_names = get_feature_names()
    feature_vector = prepare_ml_input(ml_features)
    
    # Step 3: ML Risk Prediction
    ml_prediction = predict_credit_risk(feature_vector, feature_names)
    
    # Step 4: Loan Recommendation (using ML outputs)
    from modules.ratio_analyzer import calculate_financial_ratios
    ratios = calculate_financial_ratios(financial_data)
    
    loan_recommendation = calculate_loan_recommendation(
        financial_data,
        ratios,
        ml_prediction['credit_score'],
        ml_prediction['risk_level']
    )
    
    # Step 5: Generate CAM Report
    cam_report = generate_cam_report(
        company_name,
        financial_data,
        ml_prediction,
        loan_recommendation,
        research_data
    )
    
    cam_summary = generate_cam_summary(ml_prediction, loan_recommendation)
    
    # Compile complete results
    results = {
        'financial_data': financial_data,
        'validation': validation,
        'ml_features': ml_features,
        'ml_prediction': ml_prediction,
        'ratios': ratios,
        'loan_recommendation': loan_recommendation,
        'cam_report': cam_report,
        'cam_summary': cam_summary,
        'research_data': research_data
    }
    
    return results

def get_explainability_report(ml_prediction: Dict, ml_features: Dict) -> str:
    """
    Generate explainability report for ML predictions
    Uses feature importance and SHAP-like explanations
    """
    report = []
    
    report.append("="*70)
    report.append("ML MODEL EXPLAINABILITY REPORT")
    report.append("="*70)
    
    report.append("\n1. PREDICTION SUMMARY")
    report.append("-"*70)
    report.append(f"Risk Level: {ml_prediction['risk_level']}")
    report.append(f"Credit Score: {ml_prediction['credit_score']}/100")
    report.append(f"Default Probability: {ml_prediction['probability_of_default']:.2%}")
    report.append(f"Model Confidence: {ml_prediction['model_confidence']:.1%}")
    
    report.append("\n\n2. KEY DECISION FACTORS")
    report.append("-"*70)
    report.append("Top factors influencing the decision:\n")
    
    for i, explanation in enumerate(ml_prediction['explanations'], 1):
        report.append(f"{i}. {explanation}")
    
    report.append("\n\n3. FEATURE IMPORTANCE")
    report.append("-"*70)
    report.append("Model feature weights:\n")
    
    for feature, importance in sorted(
        ml_prediction['feature_importance'].items(),
        key=lambda x: x[1],
        reverse=True
    ):
        bar = "█" * int(importance * 50)
        report.append(f"{feature:30s} {importance:5.1%} {bar}")
    
    report.append("\n\n4. FEATURE VALUES")
    report.append("-"*70)
    report.append("Input features used in prediction:\n")
    
    key_features = [
        'profit_margin', 'debt_to_asset_ratio', 'liquidity_score',
        'financial_health_score', 'research_risk_score'
    ]
    
    for feature in key_features:
        value = ml_features.get(feature, 0)
        report.append(f"{feature:30s}: {value:8.2f}")
    
    report.append("\n" + "="*70)
    
    return "\n".join(report)
