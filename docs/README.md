# 💼 AI Credit Decision System

A powerful hackathon project that extracts and analyzes text from financial PDF documents using AI-powered processing.

## 🚀 Features

- **Multi-PDF Upload**: Process multiple financial documents simultaneously
- **Robust Text Extraction**: Handles messy financial PDFs with error recovery
- **Intelligent Text Cleaning**: Normalizes and prepares text for analysis
- **Financial Data Extraction**: Automatically extracts revenue, profit, debt, assets, and more
- **Indian Currency Support**: Handles ₹, Crore, Lakh formats
- **Financial Ratios**: Calculates profit margin, debt-to-asset ratio, etc.
- **AI Credit Risk Analysis**: Rule-based AI engine for credit appraisal
- **Loan Decision Engine**: Intelligent loan recommendations with interest rates
- **Credit Scoring**: 0-100 credit score calculation
- **External Intelligence Research**: Automated news search and risk signal detection (NEW)
- **Sentiment Analysis**: AI-powered news sentiment analysis (NEW)
- **Risk Signal Detection**: Identifies fraud, legal, and regulatory risks (NEW)
- **Professional Dashboard**: Visual metrics display with formatted currency
- **Professional UI**: Clean, modern Streamlit interface
- **Real-time Progress**: Visual feedback during processing
- **Export Capability**: Download extracted text for further analysis
- **Error Handling**: Gracefully handles corrupted or problematic PDFs

## 📁 Project Structure

```
credit_ai_project/
│
├── app.py                  # Main Streamlit application
├── pdf_extractor.py        # PDF text extraction module
├── text_cleaner.py         # Text cleaning and normalization
├── financial_extractor.py  # Financial data extraction engine
├── risk_analyzer.py        # Credit risk analysis & loan decision
├── research_agent.py       # External intelligence & news research (NEW)
├── utils.py                # Helper utilities
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── test_financial_extractor.py  # Test script for financial extraction
├── test_risk_analyzer.py        # Test script for risk analysis
├── test_research_agent.py       # Test script for research agent (NEW)
│
└── data/
    └── extracted_text/    # Saved extracted text files
```

## 🛠️ Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install streamlit==1.31.0
pip install pdfplumber==0.10.3
pip install pandas==2.1.4
pip install requests==2.31.0
pip install beautifulsoup4==4.12.2
pip install vaderSentiment==3.3.2
```

### Step 2: Verify Installation

```bash
streamlit --version
```

## ▶️ Running the Application

### Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 How to Use

1. **Upload PDFs**: Click "Browse files" and select one or more financial PDF documents
2. **Enable Research** (Optional): Check "Enable External Research" in sidebar and enter company name
3. **Review Files**: Check the uploaded files list to confirm
4. **Analyze**: Click the "🚀 Analyze Documents" button
5. **View External Intelligence** (if enabled): See AI-powered news analysis:
   - News Sentiment (🟢 Positive / 🟡 Neutral / 🔴 Negative)
   - Risk Signals Detected
   - Recent News Articles
   - Research Summary
   - Credit Score Adjustment
6. **View Credit Risk Analysis**: See AI-powered credit appraisal:
   - Risk Level (🟢 Low / 🟡 Medium / 🔴 High)
   - Credit Score (0-100)
   - Loan Decision (Approved/Conditional/Rejected)
   - Recommended Loan Amount
   - Suggested Interest Rate
   - Detailed Explanation
7. **View Financial Dashboard**: See extracted metrics:
   - Revenue, Net Profit, Assets, Liabilities
   - Debt, Operating Cash Flow
   - Financial ratios (Profit Margin, Debt-to-Asset Ratio)
8. **View Text Results**: Expand each document to see:
   - Word count and character count
   - Text preview (first 2000 characters)
   - Full extracted text
9. **Download**: Use the download button to save extracted text

## 🎯 Key Modules

### pdf_extractor.py
- Extracts text from PDF files page by page
- Handles extraction errors gracefully
- Skips empty pages automatically
- Supports multiple file processing

### text_cleaner.py
- Removes extra spaces and line breaks
- Normalizes text formatting
- Prepares text for financial analysis

### financial_extractor.py
- Extracts financial metrics using regex
- Handles Indian currency formats (₹, Crore, Lakh)
- Converts to numeric values
- Calculates financial ratios
- Returns structured JSON data

### risk_analyzer.py
- Rule-based AI credit risk analysis
- Calculates 4 key financial ratios
- Determines risk level (Low/Medium/High)
- Generates credit score (0-100)
- Provides loan recommendations
- Calculates interest rates
- Explains decision reasoning

### research_agent.py (NEW)
- Automated company news search
- Google News RSS integration
- Sentiment analysis (VADER)
- Risk signal detection (20+ keywords)
- Credit score adjustment based on news
- External intelligence gathering
- Real-time news monitoring

### utils.py
- Directory management
- File saving operations
- Word count calculations

### app.py
- Streamlit UI implementation
- User interaction handling
- Credit risk dashboard (NEW)
- Financial dashboard visualization
- Results visualization

## 🔧 Technical Details

**Tech Stack:**
- Python 3.8+
- Streamlit (Web UI)
- pdfplumber (PDF processing)
- pandas (Data handling & tables)
- Regex (Pattern matching)
- requests (HTTP requests)
- BeautifulSoup (Web scraping)
- VADER Sentiment (Sentiment analysis)

**Financial Extraction:**
- Regex-based pattern matching
- Multi-format currency support
- Automatic numeric conversion
- Financial ratio calculations

**Credit Risk Analysis:**
- Rule-based AI decision engine
- Multi-factor risk assessment
- Dynamic credit scoring (0-100)
- Intelligent loan recommendations
- Interest rate calculation
- Explainable AI reasoning

**External Intelligence:**
- Automated news search
- Sentiment analysis (Positive/Neutral/Negative)
- Risk signal detection (fraud, legal, regulatory)
- Credit score adjustment
- Real-time news monitoring
- Multiple data sources

**Error Handling:**
- Corrupted PDF detection
- Page-level error recovery
- Missing value handling (returns None)
- User-friendly error messages

**Logging:**
- Processing status updates
- Page extraction progress
- Financial metric extraction logs
- Credit risk analysis logs
- External research logs
- Success/failure notifications

## 🏆 Hackathon Ready

This project is designed for hackathon presentations with:
- Professional UI design
- AI-powered credit risk analysis
- External intelligence research (NEW)
- Loan decision engine
- Financial metrics dashboard
- Real-time progress indicators
- Statistics sidebar
- Automatic financial analysis
- Clean, modular code
- Easy to extend and customize

## 🧪 Testing

Test the financial extractor:

```bash
python test_financial_extractor.py
```

Test the risk analyzer:

```bash
python test_risk_analyzer.py
```

Test the research agent:

```bash
python test_research_agent.py
```

Use sample data:
- `sample_financial_data.txt` - Sample financial statement

## 🔮 Future Enhancements

- Financial data extraction (revenue, expenses, ratios) ✅ DONE
- Credit risk analysis and loan decisions ✅ DONE
- External intelligence and news research ✅ DONE
- Machine learning models (Random Forest, XGBoost)
- NewsAPI integration for more sources
- Social media sentiment analysis
- Document classification
- Multi-language support
- Multi-currency support (USD, EUR)
- Database integration
- API endpoints
- Trend analysis across years
- Historical credit score tracking
- Industry benchmarking
- Real-time alerts

## 📝 License

Open source - feel free to use and modify for your hackathon projects!

## 👨‍💻 Author

Built with ❤️ for hackathon success!
