import wikipedia
import re, time
from typing import List

def tokenize(text: str) -> List[str]:
    """Splits given text into a list of the individual tokens in order

    Args:
        text - text to tokenize

    Returns:
        tokens of given text in order
    """
    tokens = []
    token = ""
    for c in text:
        if (
            re.match("[a-zA-Z0-9]", str(c)) != None
            or c == "'"
            or c == "_"
            or c == "-"
        ):
            token += c
        else:
            if token != "":
                tokens.append(token.lower())
                token = ""
            

    if token != "":
        tokens.append(token.lower())
    return tokens

article = wikipedia.page("Artemis II", auto_suggest=False).content
# print(article)
words = tokenize(article)
# print(words)

# open and read stoplist file
with open("sorted_stoplist.txt", "r", encoding='utf8') as f:
    stoplist = f.read()
stoplist_tokenized = tokenize(stoplist)
# print(stoplist_tokenized)

freqs = {}

for word in words:
    if word not in stoplist_tokenized:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1

# print(freqs)
        
# Print out the number of unique words
total_unique_words = len(freqs)
print(f"Unique words: {total_unique_words}")

# Print out the total number of words
total_words = sum(freqs.values())
print(f"Total words: {total_words}")

# Print the top 20 words
top_words = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
print("Top 20 words in content")
for word, count in top_words[:20]:
    print(f" {word}: {count}")