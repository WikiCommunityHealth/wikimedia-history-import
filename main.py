from sys import argv
from pymongo import MongoClient

from utils.raw_obj.raw_obj import get_raw_obj
from utils.parsers.parse_obj import parse_raw_obj

INPUT = argv[1] + '.tsv'

print('Input is: ', INPUT)

print('Connectiong to mongo...')
connection = MongoClient('localhost', 27017)
print('Connected to mongo')

print('Starting everything')
count = 0
users, pages, revisions = [], [], []
with open(INPUT, 'r') as file:
    for line in file:
        remove_newline = line[0:(len(line) - 1)]
        parts = remove_newline.split('\t')
        raw_obj = get_raw_obj(parts)
        (type, result) = parse_raw_obj(raw_obj)
        if type == 'revision':
            revisions.append(result)
        elif type == 'page':
            pages.append(result)
        elif type == 'user':
            users.append(result)
        count += 1
        if (count == 500000):
            count = 0
            connection.wikimedia_history_it.revisions.insert_many(revisions)
            revisions = []
            connection.wikimedia_history_it.pages.insert_many(pages)
            pages = []
            connection.wikimedia_history_it.users.insert_many(users)
            users = []
connection.wikimedia_history_it.revisions.insert_many(revisions)
revisions = []
connection.wikimedia_history_it.pages.insert_many(pages)
pages = []
connection.wikimedia_history_it.users.insert_many(users)
users = []
print('Finished')
