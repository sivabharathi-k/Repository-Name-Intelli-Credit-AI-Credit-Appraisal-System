from financial_extractor import extract_financial_data, format_crores, validate_financial_data

# Complete financial data
text = open('sample_infosys_complete.txt', 'r', encoding='utf-8').read()

print("="*70)
print("TESTING COMPLETE INFOSYS FINANCIAL EXTRACTION")
print("="*70)

# Extract
data = extract_financial_data(text)

print("\n[EXTRACTED FINANCIAL DATA]")
print("-"*70)
for key, value in data.items():
    formatted = format_crores(value)
    print(f"{key:20s}: {formatted:>20s}")

# Validate
validation = validate_financial_data(data)
print(f"\n[VALIDATION]")
print(f"Data Completeness: {validation['completeness']:.0f}%")
print(f"Valid for Analysis: {validation['is_valid']}")

if validation['warnings']:
    print(f"\nWarnings:")
    for warning in validation['warnings']:
        print(f"  - {warning}")

print("\n" + "="*70)
if validation['completeness'] == 100:
    print("✅ SUCCESS - ALL 6 METRICS EXTRACTED")
else:
    print(f"⚠️ PARTIAL - {validation['completeness']:.0f}% COMPLETE")
print("="*70)
