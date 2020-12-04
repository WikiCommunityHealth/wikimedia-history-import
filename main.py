from sys import argv
from pymongo import MongoClient
import pprint

from utils.raw_obj.raw_obj import get_raw_obj
from utils.parsers.parse_obj import parse_raw_obj

INPUT = argv[1] + '.tsv'

print('Input is: ', INPUT)

print('Connectiong to mongo...')
connection = MongoClient('localhost', 27017)
print('Connected to mongo')

print('Starting everything')
count = 0
users, pages, revisions = [None] * 50000, [None] * 100000, [None] * 500000 
ui, pi, ri = 0, 0, 0
with open(INPUT, 'r') as file:
    for line in file:
        remove_newline = line[0:(len(line) - 1)]
        parts = remove_newline.split('\t')
        raw_obj = get_raw_obj(parts)
        (type, result) = parse_raw_obj(raw_obj)
        if type == 'revision':
            revisions[ri] = result
            ri += 1
            if (ri >= 500000):
                ri = 0
                connection.wikimedia_history_it.revisions.insert_many(revisions)
                revisions = [None] * 500000 
        elif type == 'page':
            pages[pi] = result
            pi += 1
            if (pi >= 100000):
                pi = 0
                connection.wikimedia_history_it.pages.insert_many(pages)
                pages = [None] * 100000 
        elif type == 'user':
            users[ui] = result
            ui += 1
            if (ui >= 50000):
                ui = 0
                connection.wikimedia_history_it.users.insert_many(users)
                users = [None] * 50000 
if ui > 0:
    connection.wikimedia_history_it.users.insert_many(users[0:ui])
if pi > 0:
    connection.wikimedia_history_it.pages.insert_many(pages[0:pi])
if ri > 0:
    connection.wikimedia_history_it.revisions.insert_many(revisions[0:ri])

print('Finished')
