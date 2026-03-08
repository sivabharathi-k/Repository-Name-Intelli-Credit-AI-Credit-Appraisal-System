"""Test ML System"""
import sys
sys.path.insert(0, '.')

from modules.model_loader import get_model_info

print("="*70)
print("ML MODEL STATUS")
print("="*70)

model_info = get_model_info()
print(f"\nModel Type: {model_info['type']}")
print(f"Available: {model_info['available']}")

if model_info['available']:
    print(f"Features: {model_info['features']}")
    print(f"Accuracy: {model_info['accuracy']:.1%}")
    print(f"\nDescription: {model_info['description']}")
    print("\n[SUCCESS] Trained ML model loaded successfully!")
else:
    print(f"\nDescription: {model_info['description']}")
    print("\n[FALLBACK] Using rule-based system")

print("="*70)
