"""
Safe DataFrame Utilities
Prevents PyArrow overflow errors with large financial numbers
"""
import pandas as pd
import numpy as np
from typing import Dict, Any, Optional

def safe_numeric_convert(value: Optional[float], max_int_value: float = 2**53) -> Any:
    """
    Safely convert numeric value for dataframe
    If value exceeds safe integer range, keep as float
    """
    if value is None or pd.isna(value):
        return 0
    
    # If value is too large for safe int conversion, keep as float
    if abs(value) > max_int_value:
        return float(value)
    
    # Otherwise convert to int
    try:
        return int(value)
    except (ValueError, OverflowError):
        return float(value)

def create_safe_dataframe(data: Dict[str, Any]) -> pd.DataFrame:
    """
    Create pandas DataFrame with safe numeric types
    Prevents PyArrow overflow errors
    """
    # Convert all values safely
    safe_data = {}
    for key, value in data.items():
        if isinstance(value, (list, tuple)):
            safe_data[key] = [safe_numeric_convert(v) if isinstance(v, (int, float)) else v for v in value]
        elif isinstance(value, (int, float)):
            safe_data[key] = safe_numeric_convert(value)
        else:
            safe_data[key] = value
    
    # Create dataframe
    df = pd.DataFrame(safe_data)
    
    # Ensure numeric columns use float64 for large numbers
    for col in df.columns:
        if df[col].dtype in ['int64', 'int32']:
            # Check if any value is too large
            if (df[col].abs() > 2**53).any():
                df[col] = df[col].astype('float64')
    
    return df

def format_dataframe_for_display(df: pd.DataFrame) -> pd.DataFrame:
    """
    Format dataframe for safe Streamlit display
    Replaces large numbers with formatted strings if needed
    """
    df_display = df.copy()
    
    for col in df_display.columns:
        if df_display[col].dtype in ['int64', 'float64']:
            # If values are very large, consider formatting
            max_val = df_display[col].abs().max()
            if max_val > 1e10:  # Values over 10 billion
                # Keep as float to avoid overflow
                df_display[col] = df_display[col].astype('float64')
    
    return df_display
