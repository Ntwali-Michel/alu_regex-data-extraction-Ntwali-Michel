#!/usr/bin/env python3
def extract_emails(text):
    """Extracts all email addresses from the given text."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def extract_urls(text):
    """Extracts all URLs from the given text."""
    pattern = r"https?://[a-zA-Z0-9./_-]+"
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    """Extracts phone numbers in various formats."""
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

def extract_credit_cards(text):
    """Extracts credit card numbers."""
    pattern = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    return re.findall(pattern, text)

def extract_time(text):
    """Extracts time in 12-hour or 24-hour format."""
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b"
    return re.findall(pattern, text)

def extract_html_tags(text):
    """Extracts HTML tags from a given string."""
    pattern = r"<[^>]+>"
    return re.findall(pattern, text)

def extract_hashtags(text):
    """Extracts hashtags from a given string."""
    pattern = r"#\w+"
    return re.findall(pattern, text)

def extract_currency_amounts(text):
    """Extracts currency amounts (e.g., $19.99, $1,234.56)."""
    pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample_text = """
    Contact us at user@example.com or visit https://example.com. 
    Call (123) 456-7890 now! Your card number 1234-5678-9012-3456 is safe.
    The meeting is at 14:30. #ExampleTag $1,234.56
    <p>This is a paragraph</p>
    """

    print("📧 Extracted Emails:", extract_emails(sample_text))
    print("🔗 Extracted URLs:", extract_urls(sample_text))
    print("📞 Extracted Phone Numbers:", extract_phone_numbers(sample_text))
    print("💳 Extracted Credit Cards:", extract_credit_cards(sample_text))
    print("⏰ Extracted Time:", extract_time(sample_text))
    print("🏷️ Extracted HTML Tags:", extract_html_tags(sample_text))
    print("🏷️ Extracted Hashtags:", extract_hashtags(sample_text))
    print("💲 Extracted Currency Amounts:", extract_currency_amounts(sample_text))


