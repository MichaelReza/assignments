import csv
import json

"""
This program generates direct JSON literals from the source Netflix Prize movie file.
This allows us to pass the data directly into a `mongoimport`.
"""

# For simplicity, we assume that the program runs where the files are located.
MOVIE_SOURCE = 'movie_titles.csv'
with open(MOVIE_SOURCE, 'r+', encoding='iso-8859-1') as f:
    reader = csv.reader(f)
    for row in reader:
        id = row[0]
        year = None if row[1] == 'NULL' else int(row[1])
        title = ', '.join(row[2:])

        # Note the hardcoded empty `ratings` array—we’ll fill those in later.
        print(json.dumps({
            'id': id,
            'year': year,
            'title': title,
            'ratings': []
        }, ensure_ascii=False))  # ensure_ascii=False forces UTF-8 encoding.
