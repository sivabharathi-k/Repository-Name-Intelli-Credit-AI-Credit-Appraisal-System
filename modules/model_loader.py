"""
ML Model Loader
Loads trained model or falls back to rule-based system
"""
import pickle
from pathlib import Path
from typing import Optional, Dict

_cached_model = None

def load_credit_model() -> Optional[Dict]:
    """
    Load trained ML model from disk
    Returns: Model data dict or None if not available
    """
    global _cached_model
    
    # Return cached model if already loaded
    if _cached_model is not None:
        return _cached_model
    
    model_path = Path('models/credit_risk_model.pkl')
    
    if not model_path.exists():
        return None
    
    try:
        with open(model_path, 'rb') as f:
            _cached_model = pickle.load(f)
        return _cached_model
    except Exception as e:
        print(f"Warning: Failed to load model: {e}")
        return None

def is_model_available() -> bool:
    """Check if trained model is available"""
    return load_credit_model() is not None

def get_model_info() -> Dict:
    """Get information about loaded model"""
    model_data = load_credit_model()
    
    if model_data is None:
        return {
            'available': False,
            'type': 'Rule-Based',
            'description': 'Using rule-based risk scoring (fallback)'
        }
    
    return {
        'available': True,
        'type': 'RandomForestClassifier',
        'features': len(model_data['feature_columns']),
        'accuracy': model_data['metrics']['accuracy'],
        'description': f"Trained on synthetic dataset with {model_data['metrics']['accuracy']:.1%} accuracy"
    }
