import re

def extract_dates(text):
    date_pattern = r"""
        (\b\d{2}/\d{2}/\d{4}\b) |
        (\b\d{2}-\d{2}-\d{4}\b) |
        (\b(?:January|February|March|April|May|June|July|
             August|September|October|November|December)
           \s\d{1,2},\s\d{4}\b)"""
    return re.findall(date_pattern, text, re.VERBOSE)



text = "Conference dates: 01/22/2023, 15-02-2024 and January 5, 2025."
print(extract_dates(text))
