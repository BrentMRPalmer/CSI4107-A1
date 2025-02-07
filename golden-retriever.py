import nltk
import string
import json
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
        documents.append(word_tokenize(data["title"] + " " + data["text"]))

###################
# Remove stopwords
###################

# # Intialize set of stopwords 
# stop_words = set(stopwords.words('english'))
# stop_words.update(string.punctuation)
# stop_words.update(string.digits)
# custom_stopwords = {}
# stop_words.update(custom_stopwords)
# print(stop_words)

# filtered_words = []

# for word in word_tokens:
#     if word not in stop_words:
#         filtered_words.append(word)

# print(filtered_words)
