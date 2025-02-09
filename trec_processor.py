import time
import csv

with open("./scifact/qrels/test.tsv", 'r', encoding="utf-8") as original_file:
    with open("./scifact/qrels/formatted_test.tsv", "w", newline='') as formatted_file:
        tsv_reader = csv.reader(original_file, delimiter="\t")
        tsv_writer = csv.writer(formatted_file, delimiter='\t')
        next(tsv_reader, None)
        for query in tsv_reader:
            query.insert(1, 0)
            if int(query[0]) % 2 == 1:
                tsv_writer.writerow(query)