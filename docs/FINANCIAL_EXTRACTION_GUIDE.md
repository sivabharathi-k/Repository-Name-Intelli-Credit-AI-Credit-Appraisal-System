# 💰 Financial Data Extraction Engine - Documentation

## Overview

The Financial Data Extraction Engine automatically detects and extracts financial metrics from text using regex pattern matching and handles multiple Indian currency formats.

## How It Works

### 1. Pattern Matching
The system uses regex patterns to identify financial metrics in text:

```python
# Example patterns for Revenue
r'revenue[:\s]+([₹rs\d,\.\s]+(?:crore|lakh|cr|lac)?)'
r'total\s+revenue[:\s]+([₹rs\d,\.\s]+(?:crore|lakh|cr|lac)?)'
```

### 2. Currency Conversion
Handles multiple Indian currency formats:

| Input Format | Numeric Output |
|--------------|----------------|
| ₹5,20,00,000 | 52000000 |
| Rs 52000000 | 52000000 |
| 5.2 Crore | 52000000 |
| 48 Lakh | 4800000 |

### 3. Data Extraction
Extracts 6 key financial metrics:
- Revenue
- Net Profit
- Total Debt
- Operating Cash Flow
- Total Assets
- Total Liabilities

## Usage

### Basic Usage

```python
from financial_extractor import extract_financial_data

text = """
Revenue: ₹5,20,00,000
Net Profit: ₹48,00,000
"""

data = extract_financial_data(text)
print(data)
# Output: {'revenue': 52000000, 'net_profit': 4800000, ...}
```

### Format Currency

```python
from financial_extractor import format_indian_currency

formatted = format_indian_currency(52000000)
print(formatted)  # Output: ₹5,20,00,000
```

### Calculate Ratios

```python
from financial_extractor import calculate_financial_ratios

ratios = calculate_financial_ratios(data)
print(ratios)
# Output: {'profit_margin': 9.23, 'debt_to_asset_ratio': 0.42, ...}
```

## Integration with Streamlit

The financial extractor is automatically integrated into the main app:

1. Upload PDF → Text Extraction
2. Text Cleaning
3. **Financial Data Extraction** (NEW)
4. Display Dashboard with metrics

## Testing

Run the test script:

```bash
python test_financial_extractor.py
```

## Supported Patterns

### Revenue
- "Revenue: ₹X"
- "Total Revenue: ₹X"
- "Sales: ₹X"

### Net Profit
- "Net Profit: ₹X"
- "Profit: ₹X"
- "Net Income: ₹X"

### Debt
- "Total Debt: ₹X"
- "Debt: ₹X"
- "Borrowings: ₹X"

### Cash Flow
- "Operating Cash Flow: ₹X"
- "Cash Flow: ₹X"
- "OCF: ₹X"

### Assets
- "Total Assets: ₹X"
- "Assets: ₹X"

### Liabilities
- "Total Liabilities: ₹X"
- "Liabilities: ₹X"

## Key Features

✓ Handles messy text formats
✓ Case-insensitive matching
✓ Multiple pattern variations
✓ Indian currency format support
✓ Automatic ratio calculation
✓ Returns None for missing values
✓ Clean JSON output

## Example Output

```json
{
  "revenue": 52000000,
  "net_profit": 4800000,
  "debt": 16000000,
  "cash_flow": 7200000,
  "assets": 38000000,
  "liabilities": 21000000
}
```

## Financial Ratios Calculated

1. **Profit Margin**: (Net Profit / Revenue) × 100
2. **Debt-to-Asset Ratio**: Debt / Assets
3. **Asset-to-Liability Ratio**: Assets / Liabilities

## Hackathon Tips

- Demo with real financial PDFs for impact
- Show the dashboard visualization
- Highlight automatic extraction vs manual entry
- Emphasize time savings
- Show error handling (missing values)

## Future Enhancements

- Support for more currencies (USD, EUR)
- Extract dates and periods
- Trend analysis across multiple years
- ML-based extraction for complex formats
- Export to Excel/CSV
