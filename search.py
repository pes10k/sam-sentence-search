#!/usr/bin/env python3

import pickle
import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', required=True,
                    help="The words or search terms to search for.")
parser.add_argument('-l', '--limit', type=int,
                    help="The maximum number of results to return (by default "
                         "returns all results).")
parser.add_argument('-p', '--punctuation', required=True, metavar='N',
                    nargs='+',
                    help="The punctuation charter(s) to use in the query.")
args = parser.parse_args()

escaped_query = re.escape(args.query)
escaped_punct = "|".join([re.escape(p) for p in args.punctuation])
pattern = "{}.*?(?:{})".format(escaped_query, escaped_punct)
query_expression = re.compile(pattern, flags=re.U | re.M | re.I)

data_set = pickle.load(open("corpus.pickle", 'rb'))

matches = []

for sentence in data_set:
    if query_expression.search(sentence):
        matches.append(sentence)
        if args.limit is not None and len(matches) >= args.limit:
            break

print("\n---\n".join(matches))
