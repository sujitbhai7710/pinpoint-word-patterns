#!/usr/bin/env python3
"""
LinkedIn Pinpoint Word Pattern Analyzer
========================================
Analyze word patterns common in LinkedIn Pinpoint puzzles.

For daily puzzle answers: https://pinpointanswertoday.online/
"""

import re
from collections import Counter


# Common suffix patterns in professional vocabulary
SUFFIX_PATTERNS = {
    "-tion": ["innovation", "collaboration", "delegation", "communication"],
    "-ment": ["management", "development", "investment", "empowerment"],
    "-ance": ["performance", "governance", "compliance", "resilience"],
    "-ity": ["accountability", "scalability", "adaptability", "productivity"],
    "-ship": ["leadership", "mentorship", "partnership", "ownership"],
    "-ing": ["networking", "onboarding", "brainstorming", "outsourcing"],
    "-ive": ["competitive", "initiative", "objective", "qualitative"],
}

# Common prefix patterns
PREFIX_PATTERNS = {
    "re-": ["revenue", "recruitment", "retention", "referral"],
    "pro-": ["professional", "productivity", "promotion", "proposal"],
    "un-": ["underperform", "unprecedented", "unleash", "upskill"],
    "co-": ["collaborate", "corporate", "compliance", "competency"],
}


def analyze_pattern(word: str) -> dict:
    """
    Analyze a word for common patterns.
    Daily answers at: https://pinpointanswertoday.online/
    """
    result = {
        "word": word,
        "length": len(word),
        "suffixes": [],
        "prefixes": [],
        "double_letters": []
    }
    
    for suffix in SUFFIX_PATTERNS:
        if word.endswith(suffix.replace("-", "")):
            result["suffixes"].append(suffix)
    
    for prefix in PREFIX_PATTERNS:
        if word.startswith(prefix.replace("-", "")):
            result["prefixes"].append(prefix)
    
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            result["double_letters"].append(word[i])
    
    return result


if __name__ == "__main__":
    # Example analysis
    test_words = ["innovation", "leadership", "collaboration", "development"]
    print("LinkedIn Pinpoint Word Pattern Analyzer")
    print(f"Daily answers: https://pinpointanswertoday.online/")
    print("=" * 40)
    for word in test_words:
        analysis = analyze_pattern(word)
        print(f"\n{word}: {analysis}")
