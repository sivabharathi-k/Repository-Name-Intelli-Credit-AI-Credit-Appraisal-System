## 🔍 Research Agent - External Intelligence Module

## Overview

The Research Agent automatically collects external intelligence about companies by searching news sources, analyzing sentiment, and detecting potential credit risks. It acts as an AI-powered due diligence assistant.

## How It Works

### 1. Company Search

Searches multiple sources for company-related information:

```python
Search Queries:
- "{company_name} news"
- "{company_name} legal case"
- "{company_name} investigation"
- "{company_name} fraud"
- "{company_name} regulatory"
```

### 2. Data Sources

- **Google News RSS** - Real-time news aggregation
- **Web Scraping** - BeautifulSoup for HTML parsing
- **Multiple Queries** - Comprehensive coverage

### 3. News Extraction

Extracts structured data from each article:
- Headline
- Source
- Summary
- Link
- Publication date
- Sentiment

### 4. Sentiment Analysis

Uses **VADER Sentiment Analysis**:
- Positive: Score ≥ 0.05
- Neutral: -0.05 < Score < 0.05
- Negative: Score ≤ -0.05

### 5. Risk Signal Detection

Scans for 20+ risk keywords:
```
fraud, investigation, lawsuit, bankruptcy, default,
penalty, regulatory action, tax raid, litigation,
scam, embezzlement, corruption, seized, arrested,
probe, inquiry, violation, fine, suspended
```

### 6. Credit Score Adjustment

Adjusts base credit score based on findings:
- Negative sentiment: -10 points
- Positive sentiment: +5 points
- Each risk signal: -5 points

---

## Usage

### Basic Usage

```python
from research_agent import research_company

# Research a company
results = research_company("ABC Industries Ltd", base_credit_score=85)

# Access results
print(f"Sentiment: {results['sentiment']}")
print(f"Risk Signals: {len(results['risk_signals'])}")
print(f"Adjusted Score: {results['adjusted_risk_score']}")
```

### Output Structure

```json
{
  "company_name": "ABC Industries Ltd",
  "sentiment": "Negative",
  "sentiment_score": -0.234,
  "risk_signals": [
    "Company under investigation - Contains 'investigation'",
    "Regulatory penalty imposed - Contains 'penalty'"
  ],
  "news_articles": [
    {
      "headline": "ABC Industries faces regulatory scrutiny",
      "source": "Economic Times",
      "summary": "...",
      "link": "https://...",
      "sentiment": "Negative",
      "sentiment_score": -0.45
    }
  ],
  "research_summary": "Analysis of 8 recent articles reveals negative sentiment with 2 risk signal(s) detected...",
  "adjusted_risk_score": 70,
  "articles_analyzed": 8
}
```

---

## Key Functions

### 1. search_company_news(company_name, max_results=10)

Searches Google News RSS for company information.

```python
articles = search_company_news("Reliance Industries", max_results=10)
# Returns: List of article dictionaries
```

### 2. analyze_sentiment(text)

Analyzes sentiment using VADER.

```python
sentiment, score = analyze_sentiment("Company reports strong growth")
# Returns: ("Positive", 0.67)
```

### 3. detect_risk_signals(articles)

Detects risk keywords in articles.

```python
risk_signals = detect_risk_signals(articles)
# Returns: ["Article headline - Contains 'fraud'", ...]
```

### 4. generate_research_summary(articles, sentiment, risk_signals)

Generates AI summary of findings.

```python
summary = generate_research_summary(articles, "Negative", risk_signals)
# Returns: "Analysis of 10 articles reveals negative sentiment..."
```

### 5. adjust_risk_from_news(base_score, sentiment, num_signals)

Adjusts credit score based on news.

```python
adjusted = adjust_risk_from_news(85, "Negative", 2)
# Returns: 70 (85 - 10 for sentiment - 10 for 2 signals)
```

### 6. research_company(company_name, base_credit_score)

Main function - performs complete research.

```python
results = research_company("ABC Ltd", 85)
# Returns: Complete research analysis dictionary
```

---

## Integration with Streamlit

### Enable Research in Sidebar

```python
enable_research = st.checkbox("Enable External Research")
if enable_research:
    company_name = st.text_input("Company Name")
```

### Perform Research

```python
if enable_research and company_name:
    research_results = research_company(company_name, base_credit_score)
    results[filename]['research'] = research_results
```

### Display Results

```python
if 'research' in result:
    st.subheader("🔍 External Intelligence Analysis")
    
    # Sentiment display
    sentiment_emoji = get_sentiment_emoji(research['sentiment'])
    st.markdown(f"{sentiment_emoji} Sentiment: {research['sentiment']}")
    
    # Research summary
    st.info(research['research_summary'])
    
    # Risk signals
    for signal in research['risk_signals']:
        st.warning(f"• {signal}")
    
    # News articles
    for article in research['news_articles']:
        st.write(f"📰 {article['headline']}")
        st.write(f"   Sentiment: {article['sentiment']}")
```

---

## Example Scenarios

### Scenario 1: Clean Company Profile

```
Input:
  Company: "Tata Consultancy Services"
  Base Score: 90

Output:
  Sentiment: Positive 🟢
  Risk Signals: 0
  Adjusted Score: 95 (+5)
  Summary: "Positive sentiment. No major risks detected."
```

### Scenario 2: Company Under Investigation

```
Input:
  Company: "XYZ Corp"
  Base Score: 80

Output:
  Sentiment: Negative 🔴
  Risk Signals: 3
  Adjusted Score: 55 (-25)
  Summary: "Negative sentiment with 3 risk signals detected.
           Company faces legal and regulatory risks."
```

### Scenario 3: No News Available

```
Input:
  Company: "Small Private Ltd"
  Base Score: 75

Output:
  Sentiment: Neutral 🟡
  Risk Signals: 0
  Adjusted Score: 75 (no change)
  Summary: "No recent news found. Limited external intelligence."
```

---

## Risk Keywords Detected

### Legal & Regulatory
- lawsuit, litigation, legal case
- regulatory action, violation
- penalty, fine, suspended

### Financial Distress
- bankruptcy, default, insolvent
- debt crisis, financial trouble

### Criminal Activity
- fraud, scam, embezzlement
- corruption, bribery
- arrested, seized

### Investigations
- investigation, probe, inquiry
- tax raid, enforcement action
- under scrutiny

---

## Sentiment Analysis Logic

### VADER Sentiment Scores

```
Compound Score Range: -1.0 to +1.0

Positive:  ≥ 0.05
Neutral:   -0.05 to 0.05
Negative:  ≤ -0.05
```

### Example Scores

```
"Company reports record profits" → +0.78 (Positive)
"Quarterly results announced" → 0.02 (Neutral)
"Company faces investigation" → -0.65 (Negative)
```

---

## Credit Score Adjustment Logic

### Base Adjustments

```python
Negative Sentiment: -10 points
Positive Sentiment: +5 points
Neutral Sentiment: 0 points
```

### Risk Signal Penalties

```python
Each Risk Signal: -5 points
Maximum Penalty: -25 points (5 signals)
```

### Example Calculations

```
Base Score: 85
Sentiment: Negative (-10)
Risk Signals: 2 (-10)
Adjusted: 85 - 10 - 10 = 65
```

---

## Dashboard Features

### External Intelligence Section

```
┌────────────────────────────────────────┐
│  🔍 EXTERNAL INTELLIGENCE ANALYSIS    │
├────────────────────────────────────────┤
│  🔴 News Sentiment: Negative          │
│                                        │
│  📊 Research Summary:                 │
│  Analysis reveals negative sentiment  │
│  with 2 risk signals detected...      │
│                                        │
│  ⚠️ Risk Signals Detected:            │
│  • Company under investigation        │
│  • Regulatory penalty imposed         │
│                                        │
│  📰 Recent News Articles:             │
│  1. Company faces scrutiny            │
│     Sentiment: 🔴 Negative            │
│  2. Regulatory action announced       │
│     Sentiment: 🔴 Negative            │
│                                        │
│  📉 Score Adjustment: -15             │
│  Original: 85 → Adjusted: 70          │
└────────────────────────────────────────┘
```

---

## Testing

### Run Test Script

```bash
python test_research_agent.py
```

### Test Cases

1. **Well-known Company** - Tests with major company
2. **Another Company** - Tests with different company
3. **Unknown Company** - Tests with no news

---

## Performance

- **Search Time**: 3-5 seconds per company
- **Articles Retrieved**: 5-10 per search
- **Accuracy**: Depends on news availability
- **Rate Limiting**: Built-in delays to avoid blocking

---

## Limitations

1. **News Availability**: Depends on public news sources
2. **Language**: English news only
3. **Recency**: Limited to recent news (Google News)
4. **False Positives**: Keyword matching may flag unrelated news
5. **Rate Limits**: Too many requests may be blocked

---

## Best Practices

### 1. Use Specific Company Names
```python
✅ "Reliance Industries Limited"
❌ "Reliance"
```

### 2. Enable for High-Value Loans
```python
if loan_amount > 10000000:
    enable_research = True
```

### 3. Manual Review
```python
# Always review risk signals manually
if len(risk_signals) > 0:
    print("Manual review recommended")
```

### 4. Cache Results
```python
# Cache research results to avoid repeated searches
@st.cache_data(ttl=3600)
def cached_research(company_name):
    return research_company(company_name)
```

---

## Customization

### Add More Risk Keywords

```python
# In research_agent.py
RISK_KEYWORDS = [
    'fraud', 'investigation', 'lawsuit',
    'your_custom_keyword',  # Add here
]
```

### Adjust Score Penalties

```python
# In adjust_risk_from_news()
if sentiment == "Negative":
    adjusted_score -= 15  # Change from 10
```

### Change News Sources

```python
# Add NewsAPI integration
def search_newsapi(company_name):
    api_key = "your_api_key"
    url = f"https://newsapi.org/v2/everything?q={company_name}"
    # ... implementation
```

---

## Future Enhancements

- Integration with NewsAPI for more sources
- Social media sentiment analysis
- Company website scraping
- Financial news aggregators
- Real-time alerts
- Historical trend analysis
- Industry-specific risk factors
- Competitor analysis
- ESG risk assessment

---

## API Reference

### Main Function

```python
research_company(company_name: str, base_credit_score: int = None) -> dict
```

### Helper Functions

```python
search_company_news(company_name: str, max_results: int = 10) -> list
analyze_sentiment(text: str) -> tuple
detect_risk_signals(articles: list) -> list
generate_research_summary(articles: list, sentiment: str, risk_signals: list) -> str
adjust_risk_from_news(base_score: int, sentiment: str, num_signals: int) -> int
get_sentiment_emoji(sentiment: str) -> str
format_article_for_display(article: dict) -> dict
```

---

## Dependencies

```
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
vaderSentiment==3.3.2
```

---

## Summary

The Research Agent provides:
- ✅ Automated news search
- ✅ Sentiment analysis
- ✅ Risk signal detection
- ✅ Credit score adjustment
- ✅ Professional dashboard
- ✅ Real-time intelligence

**Adds powerful external intelligence to your credit decision system! 🔍**
