import re


def extract_urls(text):
    url_pattern = r"(https?://[^\s]+|www\.[^\s]+|\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b)"
    return re.findall(url_pattern, text)


# Example
text = "Check git profile at https://github.com/Yuvi4215 or visit www.google.com and search Yuvi4215 github."
print(extract_urls(text))
