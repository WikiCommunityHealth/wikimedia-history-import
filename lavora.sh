#!/bin/bash

FROM=2001
TO=2020

function lavora {
    YEAR=$1
    echo "FACENDO TUTTO PER L'ANNO $1"

    echo "Downloading..."
    curl https://dumps.wikimedia.org/other/mediawiki_history/2020-10/itwiki/2020-10.itwiki.${YEAR}.tsv.bz2 --output ${YEAR}.tsv.bz2
    echo -e "Downloaded $YEAR\n"

    echo "Extracting..."
    bzip2 -d ${YEAR}.tsv.bz2
    echo -e "Extracted $YEAR\n"

    echo "Jsonizing..."
    python main.py ${YEAR}
    echo -e "Jsonized $YEAR\n"

    echo "Importing..."
    mongoimport --db=wikimedia_history --collection=revisions --file=revisions.json
    mongoimport --db=wikimedia_history --collection=users --file=users.json
    mongoimport --db=wikimedia_history --collection=pages --file=pages.json
    echo "Imported $YEAR\n"

    echo "Removing..."
    rm ${YEAR}.tsv
    rm pages.json
    rm revisions.json
    rm users.json
    echo -e "Removed $YEAR\n"
}

for YEAR in `seq $FROM $TO`;
do
    lavora $YEAR
    echo -e "\n\n\n"
done

