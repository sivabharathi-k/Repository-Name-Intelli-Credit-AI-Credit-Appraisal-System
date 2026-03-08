"""
Research Agent Module
Automatically collects external intelligence and detects credit risks
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Risk keywords for detection
RISK_KEYWORDS = [
    'fraud', 'investigation', 'lawsuit', 'bankruptcy', 'default',
    'penalty', 'regulatory action', 'tax raid', 'litigation',
    'scam', 'embezzlement', 'corruption', 'seized', 'arrested',
    'probe', 'inquiry', 'violation', 'fine', 'suspended'
]

def search_company_news(company_name, max_results=10):
    """
    Search for company news using Google News RSS
    
    Args:
        company_name (str): Company name to search
        max_results (int): Maximum number of results
        
    Returns:
        list: News articles
    """
    articles = []
    
    # Search queries
    queries = [
        f"{company_name} news",
        f"{company_name} legal case",
        f"{company_name} investigation",
        f"{company_name} fraud",
        f"{company_name} regulatory"
    ]
    
    for query in queries[:2]:  # Limit to 2 queries for speed
        try:
            # Google News RSS feed
            url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-IN&gl=IN&ceid=IN:en"
            
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'xml')
                items = soup.find_all('item')[:5]  # Top 5 per query
                
                for item in items:
                    # Clean HTML from summary
                    summary_text = ''
                    if item.description:
                        summary_html = item.description.text
                        summary_soup = BeautifulSoup(summary_html, 'html.parser')
                        summary_text = summary_soup.get_text(strip=True)
                    
                    article = {
                        'headline': item.title.text if item.title else 'No title',
                        'link': item.link.text if item.link else '',
                        'source': item.source.text if item.source else 'Unknown',
                        'pub_date': item.pubDate.text if item.pubDate else '',
                        'summary': summary_text
                    }
                    articles.append(article)
        except Exception as e:
            print(f"Error fetching news for query '{query}': {str(e)}")
            continue
    
    # Remove duplicates based on headline
    seen = set()
    unique_articles = []
    for article in articles:
        if article['headline'] not in seen:
            seen.add(article['headline'])
            unique_articles.append(article)
    
    return unique_articles[:max_results]

def analyze_sentiment(text):
    """
    Analyze sentiment of text using VADER
    
    Args:
        text (str): Text to analyze
        
    Returns:
        tuple: (sentiment_label, sentiment_score)
    """
    if not text:
        return "Neutral", 0.0
    
    # Get sentiment scores
    scores = sentiment_analyzer.polarity_scores(text)
    compound = scores['compound']
    
    # Classify sentiment
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, compound

def detect_risk_signals(articles):
    """
    Detect risk signals in news articles
    
    Args:
        articles (list): List of news articles
        
    Returns:
        list: Detected risk signals
    """
    risk_signals = []
    
    for article in articles:
        text = (article.get('headline', '') + ' ' + article.get('summary', '')).lower()
        
        # Check for risk keywords
        for keyword in RISK_KEYWORDS:
            if keyword in text:
                signal = f"{article.get('headline', 'Unknown')} - Contains '{keyword}'"
                risk_signals.append(signal)
                break  # One signal per article
    
    return risk_signals

def generate_research_summary(articles, overall_sentiment, risk_signals):
    """
    Generate AI research summary
    
    Args:
        articles (list): News articles
        overall_sentiment (str): Overall sentiment
        risk_signals (list): Detected risk signals
        
    Returns:
        str: Research summary
    """
    if not articles:
        return "No recent news found for this company. Limited external intelligence available."
    
    num_articles = len(articles)
    num_risks = len(risk_signals)
    
    # Generate summary based on findings
    if overall_sentiment == "Negative" and num_risks > 0:
        summary = f"Analysis of {num_articles} recent articles reveals negative sentiment with {num_risks} risk signal(s) detected. "
        summary += "Company faces potential legal, regulatory, or reputational risks. Recommend enhanced due diligence."
    
    elif overall_sentiment == "Negative" and num_risks == 0:
        summary = f"Analysis of {num_articles} recent articles shows negative sentiment but no major risk signals detected. "
        summary += "May indicate general industry challenges or market conditions."
    
    elif overall_sentiment == "Neutral" and num_risks > 0:
        summary = f"Mixed sentiment detected across {num_articles} articles with {num_risks} risk signal(s). "
        summary += "Some concerns identified that warrant further investigation."
    
    elif overall_sentiment == "Positive":
        summary = f"Analysis of {num_articles} recent articles shows positive sentiment. "
        summary += "No major legal or regulatory risks detected. Company appears to have stable public profile."
    
    else:
        summary = f"Neutral sentiment across {num_articles} articles. "
        summary += "No significant positive or negative indicators detected."
    
    return summary

def adjust_risk_from_news(base_risk_score, sentiment, num_risk_signals):
    """
    Adjust credit risk score based on news sentiment
    
    Args:
        base_risk_score (int): Original credit score (0-100)
        sentiment (str): Overall sentiment
        num_risk_signals (int): Number of risk signals
        
    Returns:
        int: Adjusted risk score
    """
    adjusted_score = base_risk_score
    
    # Adjust based on sentiment
    if sentiment == "Negative":
        adjusted_score -= 10
    elif sentiment == "Positive":
        adjusted_score += 5
    
    # Adjust based on risk signals
    if num_risk_signals > 0:
        adjusted_score -= (num_risk_signals * 5)  # -5 points per risk signal
    
    # Ensure score stays within 0-100
    adjusted_score = max(0, min(100, adjusted_score))
    
    return adjusted_score

def get_sentiment_emoji(sentiment):
    """Get emoji for sentiment"""
    emojis = {
        "Positive": "🟢",
        "Neutral": "🟡",
        "Negative": "🔴"
    }
    return emojis.get(sentiment, "⚪")

def research_company(company_name, base_credit_score=None):
    """
    Main function: Research company and generate intelligence report
    
    Args:
        company_name (str): Company name to research
        base_credit_score (int): Base credit score for adjustment
        
    Returns:
        dict: Complete research analysis
    """
    print(f"\n{'='*60}")
    print(f"Researching: {company_name}")
    print(f"{'='*60}")
    
    # Search for news
    print("→ Searching news sources...")
    articles = search_company_news(company_name)
    
    if not articles:
        return {
            "company_name": company_name,
            "sentiment": "Neutral",
            "sentiment_score": 0.0,
            "risk_signals": [],
            "news_articles": [],
            "research_summary": "No recent news found for this company.",
            "adjusted_risk_score": base_credit_score,
            "articles_analyzed": 0
        }
    
    # Analyze sentiment for each article
    print(f"→ Analyzing {len(articles)} articles...")
    for article in articles:
        text = article['headline'] + ' ' + article.get('summary', '')
        sentiment, score = analyze_sentiment(text)
        article['sentiment'] = sentiment
        article['sentiment_score'] = score
    
    # Calculate overall sentiment
    avg_score = sum(a['sentiment_score'] for a in articles) / len(articles)
    overall_sentiment, _ = analyze_sentiment("")  # Get label from score
    if avg_score >= 0.05:
        overall_sentiment = "Positive"
    elif avg_score <= -0.05:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"
    
    # Detect risk signals
    print("→ Detecting risk signals...")
    risk_signals = detect_risk_signals(articles)
    
    # Generate research summary
    print("→ Generating research summary...")
    research_summary = generate_research_summary(articles, overall_sentiment, risk_signals)
    
    # Adjust risk score if provided
    adjusted_score = base_credit_score
    if base_credit_score is not None:
        adjusted_score = adjust_risk_from_news(base_credit_score, overall_sentiment, len(risk_signals))
        print(f"→ Risk score adjusted: {base_credit_score} → {adjusted_score}")
    
    print(f"✓ Research complete!")
    
    # Compile results
    return {
        "company_name": company_name,
        "sentiment": overall_sentiment,
        "sentiment_score": round(avg_score, 3),
        "risk_signals": risk_signals,
        "news_articles": articles,
        "research_summary": research_summary,
        "adjusted_risk_score": adjusted_score,
        "articles_analyzed": len(articles)
    }

def format_article_for_display(article):
    """Format article for display"""
    return {
        "headline": article.get('headline', 'No title'),
        "source": article.get('source', 'Unknown'),
        "sentiment": article.get('sentiment', 'Neutral'),
        "link": article.get('link', '#')
    }
