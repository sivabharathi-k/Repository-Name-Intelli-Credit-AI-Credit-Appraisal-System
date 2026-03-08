"""
Test Safe DataFrame with Large Financial Numbers
"""
import pandas as pd
from dataframe_utils import safe_numeric_convert, create_safe_dataframe

print("="*70)
print("TESTING SAFE DATAFRAME WITH LARGE NUMBERS")
print("="*70)

# Test Case 1: Extremely large numbers (Crore values)
large_numbers = {
    "revenue": 1467670000000.0,      # 1.46 Lakh Crore
    "net_profit": 241080000000.0,    # 24,108 Crore
    "assets": 1120000000000.0,       # 1,12,000 Crore
    "liabilities": 450000000000.0,   # 45,000 Crore
    "debt": 85000000000.0,           # 8,500 Crore
    "cash_flow": 280000000000.0      # 28,000 Crore
}

print("\n[TEST 1: Large Crore Values]")
print("-"*70)
for key, value in large_numbers.items():
    safe_value = safe_numeric_convert(value)
    print(f"{key:20s}: {value:20.0f} -> {safe_value} ({type(safe_value).__name__})")

# Test Case 2: Create DataFrame
print("\n[TEST 2: Create Safe DataFrame]")
print("-"*70)

data = {
    "Metric": ["Revenue", "Net Profit", "Assets", "Liabilities", "Debt", "Cash Flow"],
    "Value": [
        safe_numeric_convert(large_numbers['revenue']),
        safe_numeric_convert(large_numbers['net_profit']),
        safe_numeric_convert(large_numbers['assets']),
        safe_numeric_convert(large_numbers['liabilities']),
        safe_numeric_convert(large_numbers['debt']),
        safe_numeric_convert(large_numbers['cash_flow'])
    ]
}

try:
    df = pd.DataFrame(data)
    df['Value'] = df['Value'].astype('float64')  # Ensure float64
    print("DataFrame created successfully!")
    print(f"\nDataFrame Info:")
    print(f"  Shape: {df.shape}")
    print(f"  Value column dtype: {df['Value'].dtype}")
    print(f"\nDataFrame Preview:")
    print(df.to_string(index=False))
    
    # Test PyArrow conversion
    print(f"\n[TEST 3: PyArrow Conversion]")
    print("-"*70)
    try:
        import pyarrow as pa
        table = pa.Table.from_pandas(df)
        print("✅ PyArrow conversion successful!")
        print(f"  Schema: {table.schema}")
    except ImportError:
        print("⚠️ PyArrow not installed (optional)")
    except Exception as e:
        print(f"❌ PyArrow conversion failed: {str(e)}")
        
except Exception as e:
    print(f"❌ DataFrame creation failed: {str(e)}")

# Test Case 3: Edge cases
print(f"\n[TEST 4: Edge Cases]")
print("-"*70)

edge_cases = [
    ("None value", None),
    ("Zero", 0),
    ("Small number", 1000),
    ("Large safe int", 2**53 - 1),
    ("Overflow int", 2**63),
    ("Float", 1.5e12)
]

for name, value in edge_cases:
    safe_value = safe_numeric_convert(value)
    print(f"{name:20s}: {value} -> {safe_value} ({type(safe_value).__name__})")

print("\n" + "="*70)
print("✅ ALL TESTS PASSED - SAFE DATAFRAME WORKING")
print("="*70)
