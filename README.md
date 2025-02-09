# Assignment 1: Information Retrieval System

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
of each of the main stages in the programs. Specifics on algorithms, data structures, and optimizations will be
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



#### Step 1: Preprocessing

#### Step 2: Indexing

#### Step 3: Retrieval and Ranking

#### Top 100 Results

### Trec Processor (Cleaning trec.tsv)

## How to Run

### Dependencies

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