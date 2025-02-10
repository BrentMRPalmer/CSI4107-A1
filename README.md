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
of the corpus and the query. It then 

#### Step 1: Preprocessing

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

#### Step 2: Indexing

#### Step 3: Retrieval and Ranking

#### Top 100 Results

### Trec Processor (Cleaning trec.tsv)

## Vocabulary

### How big was the vocabulary?

### Sample of 100 tokens from the vocabulary

### First 10 answers to the first 2 queries

#### Query 1

#### Query 2

### Discussion of Results

## Mean Average Precision (MAP) Score

**Titles Only Run:** 0.6310

**Titles and Full Text:** 0.4023

### Discussion