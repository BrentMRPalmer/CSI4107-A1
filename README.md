# Assignment 1: Information Retrieval System

## Table of Contents
- [Names and Student Numbers](#names-and-student-numbers)
- [Distribution of Work](#distribution-of-work)
- [Functionality of Programs](#functionality-of-programs)
- [How to Run](#how-to-run)
- [Description of Algorithms, Data Structures, and Optimizations](#description-of-algorithms-data-structures-and-optimizations)
- [Vocabulary](#vocabulary)
- [Mean Average Precision (MAP) Score](#mean-average-precision-map-score)

## Names and Student Numbers
Brent Palmer (300193610) <br>
Jay Ghosh (300243766) <br>
Natasa Bolic (300241734)

## Distribution of Work
Brent Palmer
- Step 1: Preprocessing
- Step 2: Indexing
- Step 3: Retrieval and Ranking
- Cleaning test.tsv
- Refactoring and Optimizations
- Docstrings
- Report

Jay Ghosh
- Refactoring and Optimizations
- Docstrings
- Report

Natasa Bolic
- Step 1: Preprocessing
- Step 2: Indexing
- Step 3: Retrieval and Ranking
- Cleaning test.tsv
- Top 100 results and results.txt
- Running trec_eval

## Functionality of Programs

A detailed description of the functionality of our program is included below, divided by step of the project.

This section emphasizes a high-level description of the responsibilities, including the inputs and outputs,
of each of the main stages in the programs. A discussion of the algorithms, data structures, and optimizations will be
included in [Description of Algorithms, Data Structures, and Optimizations](#description-of-algorithms-data-structures-and-optimizations).

The code is split into two files.
- **golden_retriever.py**: The main python file that contains the entire information retrieval system, including preprocessing, indexing,
and retrieval and ranking.
- **trec_processor.py**: An additional file that is used to clean the Scifact `test.tsv` file.

### Golden Retriever

The main python file that contains the entire information retrieval system, including preprocessing, indexing,
and retrieval and ranking is called `golden_retriever.py`. It also reads in the Scifact dataset corpus and queries, 
and outputs the ranked results in `Results.txt`.

#### Entry Point (Main)

The `golden_retriever.py` file beings in main, where it first reads the arguments representing the file paths
of the corpus and the query. It then reads in, preprocesses (as described below in
[Step 1: Preprocessing](#step-1-preprocessing)), and stores all of the queries. The queries are passed to the 
`load_and_rank` method, which is the pipeline that preprocesses, indexes, and retrieves and ranks the documents.

The `load_and_rank` is called twice, once to rank the documents using the title and text of the documents (results saved 
in `Results.txt`), and again to rank the documents using only the titles (results saved in `Results_Title_Only.txt`).

Within `load_and_rank`, first the documents are read in and stored. Each document is preprocessed as described below in
[Step 1: Preprocessing](#step-1-preprocessing) as it is read in. Then, the inverted index is created as described below
in [Step 2: Indexing](#step-2-indexing). Afterwards, a matrix containing all of the BM25 scores for each query and document is
computed. Next, the documents are ranked for each of the queries. The matrix formation process and ranking is described in
[Step 3: Retrieval and Ranking](#step-3-retrieval-and-ranking). The results are saved in the `Results.txt` or `Results_Title_Only.txt`

#### Step 1: Preprocessing

The preprocessing pipeline requires some global data that should only be initialized once, so it is initialized 
at the start of the `golden_retriever.py` file. 

The preprocessing pipeline handles the preprocessing for both queries and documents. 

#### Step 2: Indexing

#### Step 3: Retrieval and Ranking

#### Top 100 Results

### Trec Processor (Cleaning trec.tsv)

## How to Run

### Dependencies

Install dependencies by running `pip install -r requirements.txt` in the root directory of the project.

The Scifact dataset is available [here](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scifact.zip).

### Execution Instructions
- Generate `Results.txt`, which contains the ranking results, by running `golden_retriever.py` with command line arguments.
    - Command Line Argument 1: The file path to the directory storing the `corpus.jsonl` and `queries.jsonl` files (default is `./scifact/`)
    - Command Line Argument 2: The name of the corpus json file (default `corpus.jsonl`)
    - Command Line Argument 3: The name of the query json file (default is `queries.jsonl`)
    - Example: `python golden_retriever.py ./scifact/ corpus.jsonl queries.jsonl`
- Clean the `Scifact` `qrels` file `test.tsv` by running `trec_processor.py` with command line arguments.
    - Command Line Argument 1: The file path of the original `test.tsv` file (default is `./scifact/qrels/test.tsv`)
    - Command Line Argument 2: The target file path of the `formatted_test.tsv` file that will be generated (default is `./scifact/qrels/formatted_test.tsv`)
    - Note: This "cleaning" filters the test file to only odd queries, as per the assignment instructions, and adds a `0` column, for compatibility
    with the `trec_eval` script.
    - Example: `python trec_processor.py ./scifact/qrels/test.tsv ./scifact/qrels/formatted_test.tsv`
- Evaluate the `Results.txt` against the `formatted_test.tsv` file using `trec_eval` script.
    - In a Unix environment, download, extract, and build the `trec_eval` script using the following commands:
    <pre>
    wget https://trec.nist.gov/trec_eval/trec_eval_latest.tar.gz
    tar -xvzf trec_eval_latest.tar.gz
    cd trec_eval-9.0.7/
    make</pre>
    - Once the `trec_eval` script is built, it can be used with the following command line arguments:
        - Command Line Argument 1: The file path of the `Results.txt` file
        - Command Line Argument 2: The file path of the `formatted_test.tsv` file
        - Example: `./trec_eval -m map /mnt/c/Season11/CSI4107/CSI4107-A1/scifact/qrels/formatted_test.tsv /mnt/c/Season11/CSI4107/CSI4107-A1/Results.txt`

## Description of Algorithms, Data Structures, and Optimizations

### Golden Retriever

#### Step 1: Preprocessing

This code begins by defining a global set of stopwords, a choice that provides constant-time membership checks (O(1) on average). The stopwords come from three sources: NLTK’s built-in English stopwords list, any custom words the user may specify, and a file of additional words (`provided_stopwords.txt`). By centralizing these words in a set, the code efficiently filters out common or uninformative terms during token processing, improving both performance and clarity in subsequent analyses.

To prepare raw text, the program relies on Python’s `json.loads` function, converting JSON-formatted strings into dictionaries. This step makes it straightforward to extract specific fields from each document or query, such as `title`, `text`, or `query` content. Once the relevant fields are identified, the code normalizes them by converting every character to lowercase. It then uses NLTK’s `word_tokenize` function to split the text into tokens, isolating each meaningful unit. After tokenization, the code applies a filtering procedure to remove any token found in the global `stop_words` set, as well as any token that lacks at least one alphabetical character. This filtration process ensures that numbers, punctuation, and other such elements do not pollute the final token list.

Finally, the code performs stemming using an NLTK `PorterStemmer` instance, reducing words to their base or root form. This transformation aims to unify variations of the same word—improving search or retrieval tasks where morphological differences should not matter. Dedicated functions, such as `preprocess_document_title_and_text`, `preprocess_document_title`, and `preprocess_query`, orchestrate this process. They each handle extraction of the relevant JSON fields (e.g., just `title` vs. `title` and `text`) and then pass the text through the lowercase, tokenize, remove-stopwords, and stem pipeline.

#### Step 2: Indexing

This code builds an inverted index by iterating through a corpus of preprocessed documents, where each document is indexed by its ID. For each document, the algorithm retrieves two things: the total number of tokens and the list of stemmed, stopword-filtered tokens. It then uses Python’s `Counter` class to count how many times each token appears within that document, allowing the index construction to also record term frequencies.

The resulting index is a dictionary in which each token maps to a list of two elements. The first element in this list is an integer denoting how many distinct documents contain that token, i.e. the document frequency. The second element is itself a list of tuples, where each tuple contains a document ID and the count of how many times that token appeared in that document.

#### Step 3: Retrieval and Ranking

The retrieval phase begins with `compute_bm25`, a function that calculates the BM25 score between a single term and a document. Inside `compute_bm25`, the algorithm first determines the term frequency (tf) for the chosen document by looking up the document’s token count in the inverted index. It then applies the classic BM25 formula (referencing Week 2 from the course website) which takes into account the document frequency. The adjustable hyperparameters `k1` and `b` control term frequency saturation and length normalization, respectively. We chose the values for them based on trial and error.

Next, `compute_bm25_matrix` computes BM25 scores for every term in the vocabulary against every document. It outputs a nested dictionary (the BM25 matrix) where the top-level keys are terms, and each term maps to a dictionary keyed by document ID: BM25 score pairs. This precomputation makes subsequent queries faster, since lookups require only a direct index access rather than repeated BM25 calculations.

The `rank` function then aggregates BM25 scores for a given query. It starts with a default score of zero for all documents, iterates over each query term, and sums that term’s BM25 score for any document that contains it. Documents that do not include the term are not updated. Finally, the function produces a sorted list of `(document_id, BM25_score)` tuples in descending order of their BM25 scores.

#### Top 100 Results

`load_and_rank` orchestrates the entire pipeline by reading and preprocessing the document corpus, constructing the inverted index, computing the BM25 matrix, and then processing each query by calling the `rank` function on those queries whose IDs are odd (`int(query_id) % 2 == 1`). It takes the top 100 ranked documents for each processed query and writes the output to a file. The output records the query ID, document ID, rank position, BM25 score, and a tag indicating whether the ranking included “text_included” or “title_only” data. 

### Trec Processor (Cleaning trec.tsv)

## Vocabulary

### How big was the vocabulary?

We ran `len(inverted_index)`...

### Sample of 100 tokens from the vocabulary

### First 10 answers to the first 2 queries

#### Query 1

#### Query 2

### Discussion of Results

## Mean Average Precision (MAP) Score

**Titles and Full Text:** 0.6310

**Titles Only Run:** 0.4023

### Discussion
