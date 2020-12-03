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

    echo "Importing..."
    python main.py ${YEAR}
    echo -e "Imported $YEAR\n"

    echo "Removing..."
    rm ${YEAR}.tsv
    echo -e "Removed $YEAR\n"
}

for YEAR in `seq $FROM $TO`;
do
    lavora $YEAR
    echo -e "\n\n\n"
done

