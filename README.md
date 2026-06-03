# 💼 Intelli-Credit: ML-Powered Credit Appraisal System

AI-powered credit decision system for automated corporate credit appraisal.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

## 📁 Project Structure

```
Loan_Ai/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependencies
│
├── modules/                # Core ML modules
│   ├── financial_extractor.py      # Universal financial parser
│   ├── feature_engineering.py      # ML feature engineering
│   ├── ml_risk_model.py            # ML risk prediction
│   ├── ml_credit_engine.py         # Integrated ML engine
│   ├── cam_generator.py            # CAM report generator
│   ├── loan_engine.py              # Loan recommendations
│   ├── ratio_analyzer.py           # Financial ratios
│   ├── research_agent.py           # External intelligence
│   ├── pdf_extractor.py            # PDF processing
│   ├── text_cleaner.py             # Text normalization
│   └── dataframe_utils.py          # Safe dataframe utils
│
├── core/                   # Core utilities
│   ├── risk_analyzer.py            # Risk analysis
│   └── utils.py                    # Helper functions
│
├── tests/                  # Test scripts
│   └── test_ml_system.py           # ML system tests
│
├── data/                   # Data files
│   ├── extracted_text/             # Extracted PDFs
│   └── sample_infosys_complete.txt # Sample data
│
├── reports/                # Generated reports
│   ├── CAM_Report_*.txt            # CAM reports
│   └── ML_Explainability_*.txt     # Explainability reports
│
└── docs/                   # Documentation
    └── HACKATHON_SOLUTION.md       # Complete solution guide
```

## ✨ Features

- **Universal Financial Parser** - Handles Crore/Lakh/Billion formats
- **ML Risk Prediction** - 16 engineered features
- **Explainable AI** - Feature importance & SHAP-like explanations
- **External Research** - News sentiment & risk signals
- **CAM Report Generator** - Professional credit appraisal memos
- **Loan Recommendations** - Automated loan decisions

## 🎯 Usage

### 1. Upload Financial PDFs
Upload company financial reports (annual reports, quarterly results, etc.)

### 2. Enable Research (Optional)
Enter company name for external intelligence gathering

### 3. Analyze
Click "Analyze Documents" to run complete ML pipeline

### 4. View Results
- Financial Dashboard
- ML Risk Prediction
- Loan Recommendation
- CAM Report
- Explainability Analysis

## 🧪 Testing

```bash
# Test ML system
python tests/test_ml_system.py

# Test financial extraction
python tests/test_universal_extractor.py
```

## 📊 ML Pipeline

```
PDF Upload → Text Extraction → Financial Parsing
    ↓
Feature Engineering (16 features)
    ↓
ML Risk Model → Credit Score + Default Probability
    ↓
Loan Recommendation → Amount + Interest Rate
    ↓
CAM Report Generation
```



