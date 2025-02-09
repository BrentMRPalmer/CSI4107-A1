import nltk
import json
import time
import math
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

# Default set of English stopwords from nltk
stop_words = set(stopwords.words('english'))

# Any specific words we wanted to remove
custom_stopwords = {} 
stop_words.update(custom_stopwords)

# Stopwords recommended from the assignment description
with open("./resources/provided_stopwords.txt", 'r', encoding="utf-8") as provided_stopwords:
    for stopword in provided_stopwords:
        stop_words.add(stopword.strip())

# Initialize stemmer
stemmer = PorterStemmer()

##########################
# Step 1: Preprocessing
##########################

def extract_document_title(document):
    """ Extracts and concatenates the title from a JSON-formatted document string.
    
    Given a string representing the document in the original json format (with keys _id, title, text, and metadata),
    the function extracts the title. It also converts the string to lowercase.

    Args:
        document (str): A JSON-formatted string representing a document with keys _id, title, text, and metadata.
    
    Returns:
        str: A lowercase string containing the document title.
    """
    data = json.loads(document)
    # Extract the title from document json, and make it lowercase
    return f"{data['title']}".lower()

def extract_document_title_and_text(document):
    """ Extracts and concatenates the title and text from a JSON-formatted document string.
    
    Given a string representing the document in the original json format (with keys _id, title, text, and metadata),
    the function extracts the title and text. It concantenates them, putting an space in between. It also converts
    the string to lowercase.

    Args:
        document (str): A JSON-formatted string representing a document with keys _id, title, text, and metadata.
    
    Returns:
        str: A lowercase string containing the concatenated title and text.
    """
    data = json.loads(document)
    # Extract the title and text from document json, and make it lowercase
    return f"{data['title']} + ' ' + {data['text']}".lower()

def extract_query_text(query):
    """ Extracts the title from a JSON-formatted query string.

    Given a string representing a query in the original json format (with keys _id, text, and metadata),
    the function extracts the text and converts it to lowercase.

    Args:
        query (str): A JSON-formatted string representing a query with keys _id, text, and metadata.
    
    Returns:
        str: A lowercase string containing the query text.
    """
    data = json.loads(query)
    # Extract the text from query json, and make it lowercase
    return f"{data['text']}".lower()

def remove_stopwords(tokens):
    """ Removes stopwords from a list of tokens.

    This function uses the set of stopwords defined globally in the Initialization section of the code.
    Any token from the set of stopwords is filtered out, as well as any token that does not have
    at least one English character. It can be used for both documents and queries.

    Args:
        tokens (list): The list of tokens to be filtered.

    Returns:
        list: The list of tokens with stopwords removed.
    """
    filtered_words = []
    for token in tokens:
        # Take out stopwords, special characters, and numbers
        # Removes anything without at least one character from the English alphabet
        if token not in stop_words and any(char.isalpha() for char in token):
            filtered_words.append(token)
    return filtered_words

def stem(tokens):
    """ Stems the list of tokens using NLTK's PorterStemmer.

    This function uses NLTK's PorterStemmer to stem each token in the provided
    list of tokens. It can be used for both documents and queries.

    Args:
        tokens (list): The list of tokens to be stemmed.

    Returns:
        list: The list of stemmed tokens.
    """
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))
    return stemmed_tokens

def preprocess_document_title_and_text(document):
    """ Processes a JSON-formatted document string by setting all characters to lowercase,
    tokenizing, removing stopwords, and stemming. Extracts both title and text.

    Args:
        document (str): The JSON-formatted document string to be processed.

    Returns:
        tuple:
            int: Number of tokens.
            list: List of processed tokens.
    """
    text_document = extract_document_title_and_text(document)
    tokenized_document = word_tokenize(text_document) # Uses NLTK's function
    filtered_document = remove_stopwords(tokenized_document)
    stemmed = stem(filtered_document)
    return (len(stemmed), stemmed)

def preprocess_document_title(document):
    """ Processes a JSON-formatted document string by setting all characters to lowercase,
    tokenizing, removing stopwords, and stemming. Extracts title only.

    Args:
        document (str): The JSON-formatted document string to be processed.

    Returns:
        tuple:
            int: Number of tokens.
            list: List of processed tokens.
    """
    text_document = extract_document_title(document)
    tokenized_document = word_tokenize(text_document) # Uses NLTK's function
    filtered_document = remove_stopwords(tokenized_document)
    stemmed = stem(filtered_document)
    return (len(stemmed), stemmed)

def preprocess_query(query):
    """ Processes a JSON-formatted query string by setting all characters to lowercase,
    tokenizing, removing stopwords, and stemming. Extracts text.

    Args:
        query (str): The JSON-formatted query string to be processed.

    Returns:
        list: List of processed tokens.
    """
    text_query = extract_query_text(query)
    tokenized_query = word_tokenize(text_query) # Uses NLTK's function
    filtered_query = remove_stopwords(tokenized_query)
    return stem(filtered_query)

###################
# Step 2: Indexing
###################

def create_inverted_index(documents):
    # Keys are words in vocabulary, values are pairs of document id and count
    inverted_index = dict()

    for document_id, content in documents.items():
        text = content[1]
        # Count the occurrences of each term in the current document's text
        counter = Counter(text)
        for term, count in counter.items():
            if term not in inverted_index:
                inverted_index[term] = [1, [(document_id, count)]]
            else:
                inverted_index[term][0] += 1
                inverted_index[term][1].append((document_id, count))

    return inverted_index

###############################
# Step 3: Retrieval and Ranking
###############################

def bm25(term, document_id, documents, inverted_index, avg_dl):
    """ Desc.

    Args:
        term (str): The term used to calculate BM25 score.
        document_id (int): The id of the document used to calculate the BM25 score.
        documents (dict): The list of all documents.
        inverted_index (dict): The inverted index.

        "dog" : (2, [(d1, 5), (d2, 7)])
    
    Returns:
        list: 
    """
    N = len(documents)
    tf = 0
    for current_id, count in inverted_index[term][1]:
        if current_id == document_id:
            tf = count
            break
    df = inverted_index[term][0]
    dl = documents[document_id][0]
    avdl = avg_dl
    k1 = 1.5 # come back to this
    b = 0.5 # come back to this
    return (tf * math.log((N - df + 0.5) / (df + 0.5))) / (k1 * ((1 - b) + (b * dl) / avdl) + tf)

def bm25_matrix(documents, inverted_index, avg_dl):
    matrix = dict()
    for term, _ in inverted_index.items():
        matrix[term] = dict()
        for document_id, _ in documents.items():
            matrix[term][document_id] = bm25(term, document_id, documents, inverted_index, avg_dl)
    return matrix

def rank(query, documents, matrix):
    """ Desc.

    Args:
        query (str): example.
        inverted_index (dict): example.
    
    Returns:
        list: A list of tuples in the form (document_id, BM25_score)
    """
    scores = {document_id: 0 for document_id, _ in documents.items()}

    for term in query:
        if term in inverted_index:
            containing_documents = inverted_index[term][1]
        else:
            continue
        for document, _ in containing_documents:
            if document not in scores:
                scores[document] = matrix[term][document] # Remove this later
            else:
                scores[document] += matrix[term][document]

    return sorted(scores.items(), key=lambda item: item[1], reverse=True)

##############
# Entry Point
##############

if __name__ == "__main__":
    # Params
    corpus_dir = "./scifact/"
    corpus_filename = "corpus.jsonl"
    corpus_path = corpus_dir + corpus_filename

    query_dir = "./scifact/"
    query_filename = "queries.jsonl"
    query_path = query_dir + query_filename

    start_time = time.time()
    # Read in the corpus and queries and preprocess (step 1)
    
    # Documents stored in dictionary with key: document id, value: (length, list of document terms) (list of document terms includes terms from both title and text)
    documents = dict()

    # Read in corpus
    with open(corpus_path, 'r', encoding="utf-8") as corpus:
        for document in corpus:
            # Load in the document in json format
            data = json.loads(document)
            # Preprocess document text before saving
            documents[data["_id"]] = preprocess_document_title_and_text(document)

    # Dictionary with key: query id, value: query tokens
    queries = dict()

    # Read in corpus
    with open(query_path, 'r', encoding="utf-8") as query_corpus:
        for query in query_corpus:
            # Load in the query in json format
            data = json.loads(query)
            # Preprocess query text before saving
            queries[data["_id"]] = preprocess_query(query)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Preprocessing time: {elapsed_time: .4f} second")
    
    # Create inverted index (step 2)
    start_time = time.time()

    inverted_index = create_inverted_index(documents)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Inverted index creation time: {elapsed_time: .4f} second")

    start_time = time.time()
    doc_length_sum = 0
    for document_id, _ in documents.items():
        doc_length_sum += documents[document_id][0]
    avdl = doc_length_sum/len(documents)

    # Perform retrieval and ranking
    # Compute the BM25 score between every document and every term in the vocabulary
    matrix = bm25_matrix(documents, inverted_index, avdl)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"BM25 matrix creation time: {elapsed_time: .4f} second")

    # Write the top 100 ranked documents for every test query to an output file
    start_time = time.time()
    with open("Results.txt", "w") as file:
        for query_id, query_content in queries.items():
            if (int(query_id) % 2 == 1) :
                # Obtain the ranked documents for the current query
                ranked_documents = rank(query_content, documents, matrix)

                # Take the top 100 documents and add them to the file
                for i in range(100):
                    document_id = ranked_documents[i][0]
                    document_rank = i + 1
                    document_score = ranked_documents[i][1]
                    tag = "run_1"
                    file.write(f"{str(query_id)} Q0 {str(document_id)} {str(document_rank)} {str(document_score)} {tag}\n")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Query ranking time: {elapsed_time: .4f} second")