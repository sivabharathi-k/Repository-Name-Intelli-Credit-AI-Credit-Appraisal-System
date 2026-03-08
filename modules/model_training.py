"""
ML Model Training Module
Trains RandomForestClassifier for credit risk prediction
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pickle
from pathlib import Path

def train_credit_risk_model():
    """Train Random Forest model for credit risk prediction"""
    
    print("="*70)
    print("ML MODEL TRAINING PIPELINE")
    print("="*70)
    
    # 1. Load dataset
    print("\n[1] Loading dataset...")
    df = pd.read_csv('data/loan_training_dataset.csv')
    print(f"    Loaded {len(df)} samples")
    
    # 2. Feature selection
    feature_columns = [
        'profit_margin',
        'debt_ratio',
        'asset_liability_ratio',
        'cash_flow_strength',
        'revenue',
        'assets',
        'sentiment_score',
        'risk_signal_count',
        'sector_risk'
    ]
    
    X = df[feature_columns]
    y = df['default_occurred']
    
    print(f"    Features: {len(feature_columns)}")
    print(f"    Target: default_occurred")
    print(f"    Default rate: {y.mean():.1%}")
    
    # 3. Train/test split
    print("\n[2] Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"    Train: {len(X_train)} samples")
    print(f"    Test: {len(X_test)} samples")
    
    # 4. Train model
    print("\n[3] Training RandomForestClassifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("    Training complete")
    
    # 5. Evaluate model
    print("\n[4] Evaluating model...")
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred_proba)
    }
    
    print(f"    Accuracy:  {metrics['accuracy']:.3f}")
    print(f"    Precision: {metrics['precision']:.3f}")
    print(f"    Recall:    {metrics['recall']:.3f}")
    print(f"    F1 Score:  {metrics['f1_score']:.3f}")
    print(f"    ROC AUC:   {metrics['roc_auc']:.3f}")
    
    # 6. Feature importance
    print("\n[5] Feature Importance:")
    feature_importance = pd.DataFrame({
        'feature': feature_columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        bar = "#" * int(row['importance'] * 50)
        print(f"    {row['feature']:25s} {row['importance']:.3f} {bar}")
    
    # 7. Save model
    print("\n[6] Saving model...")
    Path('models').mkdir(exist_ok=True)
    
    model_data = {
        'model': model,
        'feature_columns': feature_columns,
        'metrics': metrics,
        'feature_importance': feature_importance.to_dict('records')
    }
    
    with open('models/credit_risk_model.pkl', 'wb') as f:
        pickle.dump(model_data, f)
    
    print("    Model saved to: models/credit_risk_model.pkl")
    
    print("\n" + "="*70)
    print("MODEL TRAINING COMPLETE")
    print("="*70)
    
    return model, metrics, feature_importance

if __name__ == "__main__":
    train_credit_risk_model()
