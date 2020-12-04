from sys import argv
import json
import time

from utils.raw_obj.raw_obj import get_raw_obj
from utils.parsers.parse_obj import parse_raw_obj

INPUT = argv[1] + '.tsv'

print('INput', INPUT)

OUTPUT_REVISIONS = "revisions.json"
OUTPUT_PAGES = "pages.json"
OUTPUT_USERS = "users.json"

print(time.time())

with open(INPUT, 'r') as file, open(OUTPUT_REVISIONS, 'w') as revisions, open(OUTPUT_PAGES, 'w') as pages, open(OUTPUT_USERS, 'w') as users:
    for line in file:
        remove_newline = line[0:(len(line) - 1)]
        parts = remove_newline.split('\t')
        raw_obj = get_raw_obj(parts)
        (type, result) = parse_raw_obj(raw_obj)
        if type == 'revision':
            revision = json.dumps(result)
            revisions.write(revision)
            revisions.write('\n')
        elif type == 'page':
            page = json.dumps(result)
            pages.write(page)
            pages.write('\n')
        elif type == 'user':
            user = json.dumps(result)
            users.write(user)
            users.write('\n')

print(time.time())
