import json
import time
from nltk.tokenize import word_tokenize

documents = []
with open("./scifact/corpus.jsonl", 'r', encoding="utf-8") as corpus:
    for document in corpus:
        data = json.loads(document)
        text = f"{data["title"]} {data["text"]}".lower()
        print(text)
        time.sleep(10)
        documents.append(word_tokenize(text))