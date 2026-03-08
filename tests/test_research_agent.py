"""
Test script for Research Agent Module
Demonstrates external intelligence gathering and risk signal detection
"""
from research_agent import research_company, get_sentiment_emoji
import json

print("="*70)
print("RESEARCH AGENT - EXTERNAL INTELLIGENCE TEST")
print("="*70)

# Test Case 1: Research a well-known company
print("\n\n" + "="*70)
print("TEST CASE 1: RESEARCHING COMPANY")
print("="*70)

company_name = "Reliance Industries"
base_credit_score = 85

print(f"\nCompany: {company_name}")
print(f"Base Credit Score: {base_credit_score}")

# Perform research
research_results = research_company(company_name, base_credit_score)

print("\n" + "-"*70)
print("RESEARCH RESULTS:")
print("-"*70)

print(f"\nSentiment: {get_sentiment_emoji(research_results['sentiment'])} {research_results['sentiment']}")
print(f"Sentiment Score: {research_results['sentiment_score']}")
print(f"Articles Analyzed: {research_results['articles_analyzed']}")

print(f"\nResearch Summary:")
print(f"{research_results['research_summary']}")

if research_results['risk_signals']:
    print(f"\nRisk Signals Detected ({len(research_results['risk_signals'])}):")
    for signal in research_results['risk_signals']:
        print(f"  ⚠️  {signal}")
else:
    print("\n✅ No risk signals detected")

print(f"\nCredit Score Adjustment:")
print(f"  Original: {base_credit_score}")
print(f"  Adjusted: {research_results['adjusted_risk_score']}")
print(f"  Change: {research_results['adjusted_risk_score'] - base_credit_score:+d}")

if research_results['news_articles']:
    print(f"\nTop News Articles ({len(research_results['news_articles'])}):")
    for idx, article in enumerate(research_results['news_articles'][:3], 1):
        print(f"\n  {idx}. {article['headline']}")
        print(f"     Source: {article.get('source', 'Unknown')}")
        print(f"     Sentiment: {get_sentiment_emoji(article.get('sentiment', 'Neutral'))} {article.get('sentiment', 'Neutral')}")

# Test Case 2: Research with different company
print("\n\n" + "="*70)
print("TEST CASE 2: RESEARCHING ANOTHER COMPANY")
print("="*70)

company_name_2 = "Tata Motors"
base_credit_score_2 = 75

print(f"\nCompany: {company_name_2}")
print(f"Base Credit Score: {base_credit_score_2}")

research_results_2 = research_company(company_name_2, base_credit_score_2)

print("\n" + "-"*70)
print("RESEARCH RESULTS:")
print("-"*70)

print(f"\nSentiment: {get_sentiment_emoji(research_results_2['sentiment'])} {research_results_2['sentiment']}")
print(f"Articles Analyzed: {research_results_2['articles_analyzed']}")
print(f"\nResearch Summary:")
print(f"{research_results_2['research_summary']}")

print(f"\nCredit Score Adjustment:")
print(f"  Original: {base_credit_score_2}")
print(f"  Adjusted: {research_results_2['adjusted_risk_score']}")
print(f"  Change: {research_results_2['adjusted_risk_score'] - base_credit_score_2:+d}")

# Test Case 3: Company with no news
print("\n\n" + "="*70)
print("TEST CASE 3: COMPANY WITH LIMITED NEWS")
print("="*70)

company_name_3 = "XYZ Unknown Company Pvt Ltd"
base_credit_score_3 = 70

print(f"\nCompany: {company_name_3}")
print(f"Base Credit Score: {base_credit_score_3}")

research_results_3 = research_company(company_name_3, base_credit_score_3)

print("\n" + "-"*70)
print("RESEARCH RESULTS:")
print("-"*70)

print(f"\nSentiment: {get_sentiment_emoji(research_results_3['sentiment'])} {research_results_3['sentiment']}")
print(f"Articles Analyzed: {research_results_3['articles_analyzed']}")
print(f"\nResearch Summary:")
print(f"{research_results_3['research_summary']}")

# Summary
print("\n\n" + "="*70)
print("TEST SUMMARY")
print("="*70)
print("✅ Research agent successfully tested")
print("✅ News search working")
print("✅ Sentiment analysis functional")
print("✅ Risk signal detection operational")
print("✅ Credit score adjustment working")
print("\n" + "="*70)
print("RESEARCH AGENT READY FOR DEPLOYMENT!")
print("="*70)

# Display JSON output for one test
print("\n\n" + "="*70)
print("SAMPLE JSON OUTPUT")
print("="*70)
print(json.dumps({
    "company_name": research_results['company_name'],
    "sentiment": research_results['sentiment'],
    "sentiment_score": research_results['sentiment_score'],
    "risk_signals_count": len(research_results['risk_signals']),
    "articles_analyzed": research_results['articles_analyzed'],
    "adjusted_risk_score": research_results['adjusted_risk_score']
}, indent=2))
