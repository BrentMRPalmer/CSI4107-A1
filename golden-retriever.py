import nltk
import json
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter

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
##########################

def extract_text(document):
    data = json.loads(document)
    # Extract the title and text from document json, and make it lowercase
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

###################
# Step 2: Indexing
###################

def create_inverted_index(documents):
    # Keys are words in vocabulary, values are pairs of document id and count
    inverted_index = dict()

    for document_id, text in documents.items():
        # Count the occurrences of each term in the current document's text
        counter = Counter(text)
        for term, count in counter.items():
            if term not in inverted_index:
                inverted_index[term] = [(document_id, count)]
            else:
                inverted_index[term].append((document_id, count))

    return inverted_index

##############
# Entry Point
##############

if __name__ == "__main__":
    # Params
    corpus_dir = "./scifact/"
    corpus_filename = "corpus.jsonl"
    corpus_path = corpus_dir + corpus_filename

    # Read in the corpus and preprocess (step 1)
    
    # Dictionary with key: document id, value: document text (text includes title and text)
    documents = dict()

    # Read in corpus
    with open(corpus_path, 'r', encoding="utf-8") as corpus:
        for document in corpus:
            # Load in the document in json format
            data = json.loads(document)
            # Preprocess document text before saving
            documents[data["_id"]] = preprocess(document)
    
    # Create inverted index (step 2)
    inverted_index = create_inverted_index(documents)

    print(inverted_index["white"])