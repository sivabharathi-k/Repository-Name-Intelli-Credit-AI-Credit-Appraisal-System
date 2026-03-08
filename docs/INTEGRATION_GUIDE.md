# 🔗 Financial Extraction - Integration Guide

## Complete Workflow

```
PDF Upload
    ↓
Text Extraction (pdfplumber)
    ↓
Text Cleaning (regex normalization)
    ↓
Financial Data Extraction (NEW)
    ↓
Dashboard Display (Streamlit)
```

## Step-by-Step Integration

### Step 1: Import the Module

```python
from financial_extractor import (
    extract_financial_data,
    format_indian_currency,
    calculate_financial_ratios
)
```

### Step 2: Extract Financial Data

```python
# After text extraction and cleaning
cleaned_text = clean_text(raw_text)

# Extract financial metrics
financial_data = extract_financial_data(cleaned_text)

# Result:
# {
#   "revenue": 52000000,
#   "net_profit": 4800000,
#   "debt": 16000000,
#   "cash_flow": 7200000,
#   "assets": 38000000,
#   "liabilities": 21000000
# }
```

### Step 3: Calculate Ratios

```python
ratios = calculate_financial_ratios(financial_data)

# Result:
# {
#   "profit_margin": 9.23,
#   "debt_to_asset_ratio": 0.42,
#   "asset_to_liability_ratio": 1.81
# }
```

### Step 4: Display in Streamlit

```python
# Display metrics in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💵 Revenue", format_indian_currency(financial_data['revenue']))

with col2:
    st.metric("💰 Net Profit", format_indian_currency(financial_data['net_profit']))

with col3:
    st.metric("💳 Total Debt", format_indian_currency(financial_data['debt']))
```

### Step 5: Create Summary Table

```python
import pandas as pd

df_data = {
    "Metric": ["Revenue", "Net Profit", "Total Assets"],
    "Value (₹)": [
        financial_data['revenue'],
        financial_data['net_profit'],
        financial_data['assets']
    ],
    "Formatted": [
        format_indian_currency(financial_data['revenue']),
        format_indian_currency(financial_data['net_profit']),
        format_indian_currency(financial_data['assets'])
    ]
}

df = pd.DataFrame(df_data)
st.dataframe(df, use_container_width=True)
```

## Currency Format Examples

### Input Formats Supported

```python
# Format 1: Indian comma notation
"Revenue: ₹5,20,00,000"  → 52000000

# Format 2: Plain rupee symbol
"Revenue: Rs 52000000"   → 52000000

# Format 3: Crore notation
"Revenue: 5.2 Crore"     → 52000000
"Revenue: 5.2 Cr"        → 52000000

# Format 4: Lakh notation
"Profit: 48 Lakh"        → 4800000
"Profit: 48 Lac"         → 4800000
```

### Output Format

```python
format_indian_currency(52000000)
# Output: "₹5,20,00,000"

format_indian_currency(4800000)
# Output: "₹48,00,000"

format_indian_currency(None)
# Output: "Not Found"
```

## Pattern Matching Logic

### How Regex Works

```python
# Pattern for Revenue
r'revenue[:\s]+([₹rs\d,\.\s]+(?:crore|lakh|cr|lac)?)'

# Breakdown:
# revenue      - Match the word "revenue"
# [:\s]+       - Match colon or spaces
# ([...])      - Capture group for the value
# ₹rs\d,\.\s   - Match currency symbols, digits, commas, dots, spaces
# (?:...)?     - Optional non-capturing group for units
# crore|lakh   - Match "crore" or "lakh"
```

### Multiple Pattern Attempts

The system tries multiple patterns for each metric:

```python
patterns = {
    "revenue": [
        r'revenue[:\s]+(...)',           # Try "revenue"
        r'total\s+revenue[:\s]+(...)',   # Try "total revenue"
        r'sales[:\s]+(...)',             # Try "sales"
    ]
}
```

## Error Handling

### Missing Values

```python
financial_data = extract_financial_data(text)

# If a metric is not found, it returns None
if financial_data['revenue'] is None:
    st.warning("Revenue not found in document")
else:
    st.metric("Revenue", format_indian_currency(financial_data['revenue']))
```

### Corrupted Data

```python
# The system handles:
# - Malformed numbers
# - Missing currency symbols
# - Inconsistent formatting
# - Extra whitespace
# - Mixed formats in same document
```

## Testing Your Integration

### Quick Test

```python
# test_integration.py
from financial_extractor import extract_financial_data

test_text = """
Company Financial Report
Revenue: ₹5,20,00,000
Net Profit: 48 Lakh
Total Assets: 3.8 Crore
"""

result = extract_financial_data(test_text)
print(result)

# Expected Output:
# {
#   'revenue': 52000000,
#   'net_profit': 4800000,
#   'debt': None,
#   'cash_flow': None,
#   'assets': 38000000,
#   'liabilities': None
# }
```

## Customization

### Add New Metrics

```python
# In financial_extractor.py, add to patterns dict:

patterns = {
    # ... existing patterns ...
    "equity": [
        r'equity[:\s]+([₹rs\d,\.\s]+(?:crore|lakh|cr|lac)?)',
        r'shareholders\s+equity[:\s]+([₹rs\d,\.\s]+(?:crore|lakh|cr|lac)?)',
    ]
}

# Add to result dict:
result = {
    # ... existing fields ...
    "equity": None
}
```

### Add New Currency Units

```python
# In convert_indian_number_to_numeric function:

# Handle Thousand
if 'THOUSAND' in value_str or 'K' in value_str:
    number = re.findall(r'[\d,\.]+', value_str)
    if number:
        num = float(number[0].replace(',', ''))
        return int(num * 1000)
```

## Performance Tips

1. **Batch Processing**: Process multiple PDFs in parallel
2. **Caching**: Use `@st.cache_data` for repeated extractions
3. **Preprocessing**: Clean text before extraction for better accuracy
4. **Validation**: Verify extracted values are reasonable

## Troubleshooting

### Issue: No data extracted
**Solution**: Check if text contains the expected keywords (revenue, profit, etc.)

### Issue: Wrong values extracted
**Solution**: Review the regex patterns and add more specific patterns

### Issue: Format not recognized
**Solution**: Add the new format to `convert_indian_number_to_numeric`

## Demo Script

```bash
# Run the complete demo
streamlit run app.py

# Test extraction only
python test_financial_extractor.py

# Check sample data
cat sample_financial_data.txt
```

## Hackathon Presentation Tips

1. **Show Before/After**: Manual vs Automated extraction
2. **Live Demo**: Upload real PDF and show instant results
3. **Highlight Speed**: "Extracts in seconds vs hours manually"
4. **Show Dashboard**: Visual metrics are impressive
5. **Mention Scalability**: "Can process 100s of documents"

## Next Steps

- Add more financial metrics (EBITDA, ROE, etc.)
- Implement ML-based extraction for complex formats
- Add data validation and sanity checks
- Export to Excel/CSV
- Create API endpoints
- Add historical trend analysis
