import json
import time
from nltk.tokenize import word_tokenize

documents = []
with open("./scifact/corpus.jsonl", 'r', encoding="utf-8") as corpus:
    for document in corpus:
        data = json.loads(document)
        documents.append(word_tokenize(data["title"] + " " + data["text"]))
        print(word_tokenize(data["title"] + " " + data["text"]))
        time.sleep(10)
        print("\n\n\n\n\n\n\n\n\n\n")