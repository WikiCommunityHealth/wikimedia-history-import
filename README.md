# wikimedia-history-import
Import all the tsv wikimedia history dump to mongodb

## Repository purpose

The purpose of this repo is to import all the italian **tsv wikimedia history dump** in a **mongodb database**. The reference to the dump is [here](https://dumps.wikimedia.org/other/mediawiki_history/readme.html).

All the data in the tsv is preserved, but separated in **three collections** in base of the event_type: revisions, pages and users. The types are correctly parsed before inserting to mongodb, so the timestamps become dates, the comma-separated lists become arrays of strings, ecc. ecc.

## How was it made

The repo consists in only two files:
* `main.py`: It is a **python** script that given a tsv file creates three json files (one for collection) ready to be imported.
* `lavora.sh`: It is a **bash** script that for each year of the italian history dump, **downloads** the compressed file, **decompresses** it, **jsonizes** it through the python script, **imports** the json files through mongoimport and **deletes** the files that are no more needed.

## How to use it

Just execute `./lavora.sh`, after making it executable through `chmod +x lavora.sh`.

## Notes

You can choose which range of years to download modifing the `FROM` and `TO` variables in `lavora.sh`.

The script could take hours in order to finish.
