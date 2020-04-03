# setup environment

import pandas as pd
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse.corenlp import CoreNLPDependencyParser
from nltk.parse import CoreNLPParser

# startup CoreNLP server
print('Start CoreNLP Server with: java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 100000')
decision = input("Did you start the server? [Y/N]: ")

# Core Parser- save as df['parsed']
def core_parser(df, col):
    parse = []
    i = ""
    for i in range(len(df)):
        parse.append(i)
        parse[i] = next(parser.raw_parse(df[col].iloc[i]))
    return parse

# Dependency Parser- save as df['dep']
def dep_parser(df, col):
    dep = []
    i = ""
    for i in range(len(df)):
        dep.append(i)
        dep[i] = next(depr.raw_parse(df[col].iloc[i]))
    return dep

# import data
path = input("Path to Directory with File: ")
filename = input("Filename (.csv): ")

df = pd.read_csv(str(path) + '/' + str(filename))

if str(decision) == "Y":
    # start up parsers
    parser = CoreNLPParser('http://localhost:9000')
    depr = CoreNLPDependencyParser('http://localhost:9000') 
    df['parsed'] = core_parser(df, 'text')
    df['dep'] = dep_parser(df, 'text')
    df.to_csv(str(path) + '/' + filename[:-4] + '_parsed.csv', index=False)
    print("File written as" + str(path) + '/' + filename[:-4]+'_parsed.csv')
else:
    print("Okay. Goodbye.")


