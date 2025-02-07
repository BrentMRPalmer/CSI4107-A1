import nltk
import json
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#############
# Downloads
#############
nltk.download('punkt_tab')
nltk.download('stopwords')

####################
# Intialialization
####################

# Initialize set of stopwords
stop_words = set(stopwords.words('english'))
custom_stopwords = {}
with open("./resources/provided_stopwords.txt", 'r', encoding="utf-8") as provided_stopwords:
    for stopword in provided_stopwords:
        stop_words.add(stopword.strip())
stop_words.update(custom_stopwords)

# Initialize stemmer
stemmer = PorterStemmer()

##########################
# Step 1: Preprocessing
#########################

def extract_text(document):
    data = json.loads(document)
    return f"{data["title"]} + ' ' + {data["text"]}".lower()

def tokenize(document):
    return word_tokenize(document)

def remove_stopwords(document):
    filtered_words = []
    for word in document:
        # Take out stopwords, and special characters, and numbers
        # Removes anything without at least one character from the English alphabet
        if word not in stop_words and any(char.isalpha() for char in word):
            filtered_words.append(word)
    return filtered_words

def stem(document):
    stemmed_words = []
    for word in document:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words

def preprocess(document):
    text_document = extract_text(document)
    tokenized_document = tokenize(text_document)
    filtered_document = remove_stopwords(tokenized_document)
    return stem(filtered_document)
    
if __name__ == "__main__":
    #################
    # Read in corpus
    #################
    documents = []
    with open("./scifact/corpus.jsonl", 'r', encoding="utf-8") as corpus:
        for document in corpus:
            documents.append(preprocess(document))

    ##################
    # Verify outputs
    ##################

    for document in documents:
        print(document)
        time.sleep(15)