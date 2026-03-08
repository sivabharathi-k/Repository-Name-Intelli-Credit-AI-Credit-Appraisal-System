# -*- coding: utf-8 -*-
"""
Universal Financial Data Extractor - PRODUCTION VERSION
Works with bank reports, annual reports, quarterly results, investor presentations
"""
import re
from typing import Dict, Optional, List, Tuple

# Comprehensive keyword mapping for financial metrics
FINANCIAL_KEYWORDS = {
    'revenue': [
        'revenue', 'total revenue', 'total income', 'income', 'sales', 'total sales',
        'turnover', 'gross revenue', 'operating revenue', 'net sales', 'total operating income'
    ],
    'net_profit': [
        'net profit', 'profit after tax', 'pat', 'net income', 'profit for the year',
        'profit for the period', 'net earnings', 'profit attributable', 'consolidated net profit'
    ],
    'assets': [
        'total assets', 'assets', 'total asset', 'gross assets'
    ],
    'liabilities': [
        'total liabilities', 'liabilities', 'total liability', 'gross liabilities'
    ],
    'debt': [
        'total debt', 'debt', 'borrowings', 'total borrowings', 'loans', 'total loans',
        'debt obligations', 'long term debt', 'short term debt'
    ],
    'cash_flow': [
        'operating cash flow', 'cash flow from operations', 'cash flow from operating activities',
        'net cash from operating', 'operating activities', 'cash generated from operations'
    ]
}

def parse_financial_number(value_str: str) -> Optional[float]:
    """
    Universal number parser for financial values
    Handles: ₹99,200.03 crore | 3,20,000 lakh | 1.5 billion | 18155.21
    """
    if not value_str:
        return None
    
    original = value_str
    value_str = value_str.upper().strip()
    
    # Remove currency symbols and common prefixes
    value_str = re.sub(r'[₹$€£RS\.](?=\d)', '', value_str)
    
    # Detect multipliers
    multiplier = 1.0
    if 'CRORE' in value_str or ' CR' in value_str:
        multiplier = 10000000.0
    elif 'LAKH' in value_str or 'LAC' in value_str:
        multiplier = 100000.0
    elif 'BILLION' in value_str or ' BN' in value_str:
        multiplier = 1000000000.0
    elif 'MILLION' in value_str or ' MN' in value_str or ' M' in value_str:
        multiplier = 1000000.0
    elif 'THOUSAND' in value_str or ' K' in value_str:
        multiplier = 1000.0
    
    # Extract numeric value (handle both comma and decimal)
    # Remove all non-numeric except comma and dot
    number_str = re.sub(r'[^\d,\.]', '', value_str)
    
    # Handle Indian format: 99,200.03 or 18155.21
    if ',' in number_str and '.' in number_str:
        # Format: 99,200.03 - remove commas
        number_str = number_str.replace(',', '')
    elif ',' in number_str:
        # Could be: 99,200 (thousands separator) or 99,20,00,000 (Indian)
        # If multiple commas, it's Indian format - remove all
        if number_str.count(',') > 1:
            number_str = number_str.replace(',', '')
        else:
            # Single comma - could be thousands separator
            number_str = number_str.replace(',', '')
    
    try:
        number = float(number_str)
        return number * multiplier
    except:
        return None

def extract_value_from_line(line: str, keywords: List[str]) -> Optional[float]:
    """Extract financial value from a line using keyword matching"""
    line_lower = line.lower()
    
    # Check if any keyword matches
    for keyword in keywords:
        if keyword in line_lower:
            # Extract everything after the keyword
            pattern = rf'{re.escape(keyword)}[:\s]+([^\n]+)'
            match = re.search(pattern, line_lower, re.IGNORECASE)
            if match:
                value_text = match.group(1)
                # Try to parse the number
                value = parse_financial_number(value_text)
                if value:
                    return value
    
    return None

def extract_from_table_format(text: str, keywords: List[str]) -> Optional[float]:
    """
    Extract from table-like formats:
    Total Income    99200.03
    Net Profit      18155.21
    """
    lines = text.split('\n')
    
    for line in lines:
        for keyword in keywords:
            if keyword in line.lower():
                # Try to find number after keyword
                parts = re.split(r'\s{2,}|\t', line)  # Split by multiple spaces or tab
                if len(parts) >= 2:
                    # Last part is usually the value
                    value = parse_financial_number(parts[-1])
                    if value:
                        return value
                
                # Alternative: find any number in the line
                numbers = re.findall(r'[\d,\.]+', line)
                if numbers:
                    # Try the last number found
                    value = parse_financial_number(numbers[-1])
                    if value:
                        return value
    
    return None

def extract_financial_data(text: str) -> Dict[str, Optional[float]]:
    """
    Universal financial data extractor
    Works with any financial report format
    """
    result = {
        "revenue": None,
        "net_profit": None,
        "debt": None,
        "cash_flow": None,
        "assets": None,
        "liabilities": None
    }
    
    if not text:
        return result
    
    # Try multiple extraction methods for each metric
    for metric, keywords in FINANCIAL_KEYWORDS.items():
        # Method 1: Line-based extraction with colon/space separator
        value = extract_value_from_line(text, keywords)
        if value:
            result[metric] = value
            continue
        
        # Method 2: Table format extraction
        value = extract_from_table_format(text, keywords)
        if value:
            result[metric] = value
            continue
        
        # Method 3: Aggressive pattern matching
        for keyword in keywords:
            # Look for keyword followed by any number pattern
            pattern = rf'{re.escape(keyword)}[:\s\-–—]*([0-9,\.]+\s*(?:crore|lakh|billion|million|cr|lac|bn|mn)?)'
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                # Try to parse the first match
                value = parse_financial_number(matches[0])
                if value:
                    result[metric] = value
                    break
    
    return result

def format_indian_currency(amount: Optional[float]) -> str:
    """Format number as Indian currency"""
    if amount is None:
        return "Not Found"
    
    s = str(int(amount))
    if len(s) <= 3:
        return f"Rs.{s}"
    
    last_three = s[-3:]
    remaining = s[:-3]
    
    formatted = ""
    while len(remaining) > 2:
        formatted = "," + remaining[-2:] + formatted
        remaining = remaining[:-2]
    if remaining:
        formatted = remaining + formatted
    
    return f"Rs.{formatted},{last_three}"

def format_crores(amount: Optional[float]) -> str:
    """Format as Crores for better readability"""
    if amount is None:
        return "Not Found"
    
    crores = amount / 10000000
    if crores >= 1000:
        return f"Rs.{crores:,.0f} Cr"
    elif crores >= 1:
        return f"Rs.{crores:,.2f} Cr"
    else:
        lakhs = amount / 100000
        return f"Rs.{lakhs:,.2f} L"

def validate_financial_data(data: Dict[str, Optional[float]]) -> Dict[str, any]:
    """Validate extracted financial data"""
    validation = {
        "is_valid": False,
        "completeness": 0,
        "warnings": []
    }
    
    # Check completeness
    found_count = sum(1 for v in data.values() if v is not None)
    validation["completeness"] = (found_count / len(data)) * 100
    
    # Minimum requirement: Revenue or Assets
    if data.get('revenue') or data.get('assets'):
        validation["is_valid"] = True
    else:
        validation["warnings"].append("⚠️ No Revenue or Assets found")
    
    # Logical checks
    if data.get('net_profit') and data.get('revenue'):
        if data['net_profit'] > data['revenue']:
            validation["warnings"].append("⚠️ Net Profit exceeds Revenue")
    
    if data.get('debt') and data.get('assets'):
        if data['debt'] > data['assets']:
            validation["warnings"].append("⚠️ Debt exceeds Assets")
    
    if data.get('liabilities') and data.get('assets'):
        if data['liabilities'] > data['assets']:
            validation["warnings"].append("⚠️ Liabilities exceed Assets")
    
    return validation

def extract_with_fallback(text: str) -> Tuple[Dict[str, Optional[float]], Dict[str, any]]:
    """
    Extract with multiple fallback strategies
    Returns: (financial_data, validation_info)
    """
    # Primary extraction
    data = extract_financial_data(text)
    validation = validate_financial_data(data)
    
    # If completeness is low, try alternative strategies
    if validation["completeness"] < 50:
        # Strategy: Look for any large numbers and try to infer context
        lines = text.split('\n')
        for line in lines:
            line_lower = line.lower()
            
            # Look for lines with financial context
            if any(word in line_lower for word in ['income', 'profit', 'revenue', 'sales']):
                numbers = re.findall(r'[\d,\.]+', line)
                if numbers:
                    value = parse_financial_number(numbers[-1])
                    if value and value > 1000000:  # Significant amount
                        if 'income' in line_lower and not data['revenue']:
                            data['revenue'] = value
                        elif 'profit' in line_lower and not data['net_profit']:
                            data['net_profit'] = value
        
        # Re-validate
        validation = validate_financial_data(data)
    
    return data, validation
