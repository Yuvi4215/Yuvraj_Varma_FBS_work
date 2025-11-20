import re


def censor_text(text, forbidden_words):
    for word in forbidden_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub("*" * len(word), text)
    return text


if __name__=="__main__":
    text = "This is a secret message containing banned words."
    forbidden = ["secret", "banned"]
    print(censor_text(text, forbidden))