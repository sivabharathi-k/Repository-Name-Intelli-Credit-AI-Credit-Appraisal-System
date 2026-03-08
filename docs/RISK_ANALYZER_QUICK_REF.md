# 📋 QUICK REFERENCE - Credit Risk Analyzer API

## Import

```python
from risk_analyzer import (
    analyze_credit_risk,
    get_risk_emoji,
    format_currency_inr
)
```

## Main Function

```python
analyze_credit_risk(financial_data: dict) -> dict
```

**Input**: Dictionary with financial metrics  
**Output**: Complete credit analysis

```python
{
    "risk_level": "LOW" | "MEDIUM" | "HIGH",
    "credit_score": 0-100,
    "decision": "Approved" | "Conditionally Approved" | "Rejected",
    "recommended_loan_amount": int,
    "interest_rate": "X.X%",
    "explanation": str,
    "ratios": {...},
    "risk_factors": [...]
}
```

## Usage

```python
# Input financial data
data = {
    "revenue": 52000000,
    "net_profit": 4800000,
    "debt": 16000000,
    "cash_flow": 7200000,
    "assets": 38000000,
    "liabilities": 21000000
}

# Analyze
analysis = analyze_credit_risk(data)

# Access results
print(f"Risk: {analysis['risk_level']}")
print(f"Score: {analysis['credit_score']}")
print(f"Decision: {analysis['decision']}")
print(f"Loan: {format_currency_inr(analysis['recommended_loan_amount'])}")
print(f"Rate: {analysis['interest_rate']}")
```

## Risk Levels

| Risk Level | Credit Score | Loan Amount | Interest Rate |
|------------|--------------|-------------|---------------|
| 🟢 LOW | 80-100 | 35% of revenue | 10.5% |
| 🟡 MEDIUM | 50-79 | 20% of revenue | 13.0% |
| 🔴 HIGH | 0-49 | ₹0 (Rejected) | N/A |

## Financial Ratios Calculated

```python
Profit Margin = Net Profit / Revenue
Debt-to-Asset Ratio = Debt / Assets
Asset-to-Liability Ratio = Assets / Liabilities
Cash Flow Strength = Cash Flow / Debt
```

## AI Rules

### Rule 1: Debt Burden
- Debt-to-Asset > 0.7 → High Risk (+3)
- Debt-to-Asset > 0.5 → Medium Risk (+2)
- Debt-to-Asset ≤ 0.5 → Low Risk

### Rule 2: Profitability
- Profit Margin < 5% → High Risk (+3)
- Profit Margin < 10% → Medium Risk (+1)
- Profit Margin ≥ 10% → Low Risk

### Rule 3: Cash Flow
- Cash Flow Strength < 0.3 → Medium Risk (+2)
- Cash Flow Strength < 0.5 → Low-Medium Risk (+1)
- Cash Flow Strength ≥ 0.5 → Low Risk

### Rule 4: Asset Coverage
- Asset-to-Liability < 1.2 → Medium Risk (+2)
- Asset-to-Liability ≥ 1.2 → Low Risk

## Risk Determination

```
Total Risk Score ≥ 6 → HIGH RISK 🔴
Total Risk Score 3-5 → MEDIUM RISK 🟡
Total Risk Score < 3 → LOW RISK 🟢
```

## Example Outputs

### Low Risk Example
```python
{
    "risk_level": "LOW",
    "credit_score": 87,
    "decision": "Approved",
    "recommended_loan_amount": 18200000,
    "interest_rate": "10.5%",
    "explanation": "Strong financial health with good profitability and manageable debt"
}
```

### Medium Risk Example
```python
{
    "risk_level": "MEDIUM",
    "credit_score": 62,
    "decision": "Conditionally Approved",
    "recommended_loan_amount": 6000000,
    "interest_rate": "13.0%",
    "explanation": "Moderate risk profile - loan approved with conditions and higher interest"
}
```

### High Risk Example
```python
{
    "risk_level": "HIGH",
    "credit_score": 28,
    "decision": "Rejected",
    "recommended_loan_amount": 0,
    "interest_rate": "N/A",
    "explanation": "High financial risk - insufficient cash flow or excessive debt burden"
}
```

## Streamlit Integration

```python
import streamlit as st
from risk_analyzer import analyze_credit_risk, get_risk_emoji

# Analyze
analysis = analyze_credit_risk(financial_data)

# Display risk level
risk_emoji = get_risk_emoji(analysis['risk_level'])
st.markdown(f"## {risk_emoji} Risk Level: {analysis['risk_level']}")

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Credit Score", f"{analysis['credit_score']}/100")
col2.metric("Decision", analysis['decision'])
col3.metric("Loan Amount", format_currency_inr(analysis['recommended_loan_amount']))

# Display explanation
st.info(analysis['explanation'])

# Display risk factors
for factor in analysis['risk_factors']:
    st.write(f"• {factor}")
```

## Helper Functions

### get_risk_emoji(risk_level)
```python
get_risk_emoji("LOW")     # Returns: "🟢"
get_risk_emoji("MEDIUM")  # Returns: "🟡"
get_risk_emoji("HIGH")    # Returns: "🔴"
```

### format_currency_inr(amount)
```python
format_currency_inr(52000000)  # Returns: "₹5,20,00,000"
format_currency_inr(4800000)   # Returns: "₹48,00,000"
format_currency_inr(0)         # Returns: "₹0"
```

## Testing

```bash
python test_risk_analyzer.py
```

Tests 3 scenarios:
- Low Risk Company
- Medium Risk Company
- High Risk Company

## Common Patterns

### Check if Approved
```python
if analysis['decision'] == "Approved":
    print("Loan approved!")
```

### Get Loan Details
```python
if analysis['recommended_loan_amount'] > 0:
    print(f"Loan: {format_currency_inr(analysis['recommended_loan_amount'])}")
    print(f"Rate: {analysis['interest_rate']}")
```

### Display Risk Factors
```python
for factor in analysis['risk_factors']:
    print(f"• {factor}")
```

### Check Ratios
```python
ratios = analysis['ratios']
if ratios['profit_margin'] > 0.10:
    print("Good profitability")
if ratios['debt_to_asset_ratio'] < 0.5:
    print("Healthy debt levels")
```

## Error Handling

```python
# Handles missing data
analysis = analyze_credit_risk({})
# Returns: risk_level="UNKNOWN", decision="Insufficient Data"

# Handles None values
analysis = analyze_credit_risk({
    "revenue": None,
    "net_profit": None,
    ...
})
# Returns: risk_level="UNKNOWN"
```

## Tips

✓ All financial values should be in numeric format (not strings)
✓ Use Indian Rupees (₹) as base currency
✓ System handles None values gracefully
✓ Risk level is always uppercase
✓ Credit score is always 0-100
✓ Loan amount is 0 for rejected applications

## Files

- `risk_analyzer.py` - Main module
- `test_risk_analyzer.py` - Test script
- `CREDIT_RISK_GUIDE.md` - Full documentation

## Quick Test

```python
from risk_analyzer import analyze_credit_risk

# Test data
data = {
    "revenue": 52000000,
    "net_profit": 4800000,
    "debt": 16000000,
    "cash_flow": 7200000,
    "assets": 38000000,
    "liabilities": 21000000
}

# Analyze
result = analyze_credit_risk(data)

# Print
print(f"Risk: {result['risk_level']}")
print(f"Score: {result['credit_score']}")
print(f"Decision: {result['decision']}")
```

Expected Output:
```
Risk: LOW
Score: 87
Decision: Approved
```
