import nltk
import string
import json
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#############
# Downloads
#############
nltk.download('punkt_tab')
nltk.download('stopwords')

#################
# Read in corpus
#################

documents = []
with open("./scifact/corpus.jsonl", 'r', encoding="utf-8") as corpus:
    for document in corpus:
        data = json.loads(document)
        text = f"{data["title"]} + ' ' + {data["text"]}".lower()
        documents.append(word_tokenize(text))

###################
# Remove stopwords
###################

# Intialize set of stopwords 
stop_words = set(stopwords.words('english'))
stop_words.update(string.punctuation)
stop_words.update(string.digits)
custom_stopwords = {}
with open("./resources/provided_stopwords.txt", 'r', encoding="utf-8") as provided_stopwords:
    for stopword in provided_stopwords:
        stop_words.add(stopword.strip())
stop_words.update(custom_stopwords)

# Filter out stopwords
for i in range(len(documents)):
    document = documents[i]
    filtered_words = []
    for word in document:
        if word not in stop_words and any(char.isalpha() for char in word):
            filtered_words.append(word)
    documents[i] = filtered_words

for document in documents:
    print(document)
    time.sleep(15)
