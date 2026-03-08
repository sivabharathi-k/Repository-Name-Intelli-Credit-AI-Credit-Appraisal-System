"""
Synthetic Dataset Generator for Credit Risk ML Model
Generates realistic financial data for training
"""
import pandas as pd
import numpy as np

np.random.seed(42)

def generate_synthetic_dataset(n_samples=1000):
    """Generate synthetic loan dataset with realistic relationships"""
    
    data = []
    
    for i in range(n_samples):
        # Base financial metrics (in Crores)
        revenue = np.random.uniform(1000, 500000)
        
        # Profit margin varies by company health
        profit_margin_pct = np.random.uniform(2, 25)
        net_profit = revenue * (profit_margin_pct / 100)
        
        # Assets typically 0.5x to 2x revenue
        assets = revenue * np.random.uniform(0.5, 2.0)
        
        # Liabilities 20% to 80% of assets
        liabilities = assets * np.random.uniform(0.2, 0.8)
        
        # Debt is subset of liabilities
        debt = liabilities * np.random.uniform(0.3, 0.7)
        
        # Cash flow related to profit
        cash_flow = net_profit * np.random.uniform(0.8, 1.5)
        
        # Calculated ratios
        profit_margin = profit_margin_pct
        debt_ratio = debt / assets if assets > 0 else 0
        asset_liability_ratio = assets / liabilities if liabilities > 0 else 1
        cash_flow_strength = cash_flow / debt if debt > 0 else 1
        
        # Research signals
        sentiment_score = np.random.uniform(-0.5, 0.8)
        risk_signal_count = np.random.poisson(2)
        sector_risk = np.random.uniform(0, 100)
        
        # Target variables - realistic relationships
        # Higher risk if: low profit, high debt, negative sentiment
        risk_score = 0
        
        if profit_margin < 5:
            risk_score += 30
        elif profit_margin < 10:
            risk_score += 15
        
        if debt_ratio > 0.7:
            risk_score += 25
        elif debt_ratio > 0.5:
            risk_score += 10
        
        if cash_flow_strength < 0.3:
            risk_score += 20
        elif cash_flow_strength < 0.5:
            risk_score += 10
        
        if sentiment_score < -0.2:
            risk_score += 15
        elif sentiment_score < 0:
            risk_score += 5
        
        if risk_signal_count > 3:
            risk_score += 10
        
        if sector_risk > 70:
            risk_score += 10
        
        # Add some randomness
        risk_score += np.random.uniform(-10, 10)
        risk_score = max(0, min(100, risk_score))
        
        # Determine outcomes
        default_probability = risk_score / 100
        default_occurred = 1 if np.random.random() < default_probability else 0
        
        # Loan approval (inverse of risk)
        approval_threshold = 0.6 - (risk_score / 200)
        loan_approved = 1 if np.random.random() > approval_threshold else 0
        
        # Credit score (inverse of risk)
        credit_score = int(100 - risk_score)
        
        data.append({
            'revenue': revenue,
            'net_profit': net_profit,
            'debt': debt,
            'assets': assets,
            'liabilities': liabilities,
            'cash_flow': cash_flow,
            'profit_margin': profit_margin,
            'debt_ratio': debt_ratio,
            'asset_liability_ratio': asset_liability_ratio,
            'cash_flow_strength': cash_flow_strength,
            'sentiment_score': sentiment_score,
            'risk_signal_count': risk_signal_count,
            'sector_risk': sector_risk,
            'loan_approved': loan_approved,
            'default_occurred': default_occurred,
            'credit_score': credit_score
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Generating synthetic credit risk dataset...")
    
    # Generate dataset
    df = generate_synthetic_dataset(1000)
    
    # Save to CSV
    df.to_csv('data/loan_training_dataset.csv', index=False)
    
    print("Dataset generated:", len(df), "samples")
    print("\nDataset Statistics:")
    print(f"  Default Rate: {df['default_occurred'].mean():.1%}")
    print(f"  Approval Rate: {df['loan_approved'].mean():.1%}")
    print(f"  Avg Credit Score: {df['credit_score'].mean():.1f}")
    print("\nSaved to: data/loan_training_dataset.csv")
