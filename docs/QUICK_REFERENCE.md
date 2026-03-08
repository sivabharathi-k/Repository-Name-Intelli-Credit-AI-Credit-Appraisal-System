# 📋 QUICK REFERENCE - Financial Extractor API

## Import

```python
from financial_extractor import (
    extract_financial_data,
    format_indian_currency,
    calculate_financial_ratios
)
```

## Main Function

```python
extract_financial_data(text: str) -> dict
```

**Input**: String containing financial text  
**Output**: Dictionary with 6 metrics

```python
{
    "revenue": int or None,
    "net_profit": int or None,
    "debt": int or None,
    "cash_flow": int or None,
    "assets": int or None,
    "liabilities": int or None
}
```

## Usage

```python
# Extract
text = "Revenue: ₹5,20,00,000"
data = extract_financial_data(text)

# Access
revenue = data['revenue']  # 52000000

# Format
formatted = format_indian_currency(revenue)  # "₹5,20,00,000"

# Calculate ratios
ratios = calculate_financial_ratios(data)
# {'profit_margin': 9.23, 'debt_to_asset_ratio': 0.42, ...}
```

## Supported Formats

| Input | Output |
|-------|--------|
| ₹5,20,00,000 | 52000000 |
| Rs 52000000 | 52000000 |
| 5.2 Crore | 52000000 |
| 48 Lakh | 4800000 |

## Metrics Detected

- Revenue (revenue, total revenue, sales)
- Net Profit (net profit, profit, net income)
- Total Debt (total debt, debt, borrowings)
- Operating Cash Flow (operating cash flow, cash flow, ocf)
- Total Assets (total assets, assets)
- Total Liabilities (total liabilities, liabilities)

## Ratios Calculated

- **Profit Margin**: (Net Profit / Revenue) × 100
- **Debt-to-Asset Ratio**: Debt / Assets
- **Asset-to-Liability Ratio**: Assets / Liabilities

## Error Handling

```python
# Missing values return None
if data['revenue'] is None:
    print("Revenue not found")

# Format handles None
formatted = format_indian_currency(None)  # "Not Found"
```

## Complete Example

```python
from financial_extractor import *

# Sample text
text = """
Revenue: ₹5,20,00,000
Net Profit: 48 Lakh
Total Assets: 3.8 Crore
"""

# Extract
data = extract_financial_data(text)

# Display
print(f"Revenue: {format_indian_currency(data['revenue'])}")
print(f"Profit: {format_indian_currency(data['net_profit'])}")
print(f"Assets: {format_indian_currency(data['assets'])}")

# Ratios
ratios = calculate_financial_ratios(data)
for name, value in ratios.items():
    print(f"{name}: {value}")
```

## Streamlit Integration

```python
import streamlit as st
from financial_extractor import *

# Extract
data = extract_financial_data(text)

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", format_indian_currency(data['revenue']))
col2.metric("Profit", format_indian_currency(data['net_profit']))
col3.metric("Debt", format_indian_currency(data['debt']))

# Display ratios
ratios = calculate_financial_ratios(data)
if 'profit_margin' in ratios:
    st.metric("Profit Margin", f"{ratios['profit_margin']}%")
```

## Testing

```bash
python test_financial_extractor.py
```

## Files

- `financial_extractor.py` - Main module
- `test_financial_extractor.py` - Test script
- `sample_financial_data.txt` - Sample data

## Tips

✓ Text is case-insensitive  
✓ Handles extra spaces  
✓ Tries multiple patterns  
✓ Returns None if not found  
✓ Works with messy PDFs  

## Common Issues

**Issue**: No data extracted  
**Fix**: Check if keywords exist in text

**Issue**: Wrong format  
**Fix**: Add pattern to `patterns` dict

**Issue**: Wrong conversion  
**Fix**: Update `convert_indian_number_to_numeric`
