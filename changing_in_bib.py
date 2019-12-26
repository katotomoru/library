# -*- coding: utf-8 -*-
import bibtexparser, os
from operator import itemgetter
from bibtexparser.customization import *

os.chdir(r"c:\users\lenovo\desktop")

normal_keys = {}

with open('normal_keys.bib', encoding="utf8") as normal_keys_file:
   #bib_str = normal_keys_file.read()
    bib_db = bibtexparser.load(normal_keys_file)

print ('len of normal keys bib: ', len(bib_db.entries))

noname = 0
#noyear = 0
duplicate = 0

for book in bib_db.entries:
    if 'title' not in book.keys():
        noname +=1
        k = ('%s %s %s' % (noname,'year', str(book.get('year'))))
        print('no title ', k, '\n', book)
    elif 'year' not in book.keys():
        #noyear += 1
        #k = ('%s %s' % (book.get('title'), noyear))
        k = str(book.get('title'))
    else:
        k = ('%s %s %s' % (str(book.get('title')), 'year', str(book.get('year'))))
    #print(k)
    if k in normal_keys.keys():
        duplicate += 1
        k = ('%s %s' % (str(duplicate), str(k)))
    normal_keys[k] = (book.get('ID'))

print ('len normal keys dict: ', len(normal_keys))

noname1 = 0
#noyear1 = 0
corrupted_keys = []
duplicate1 = 0

with open('shared.bib', encoding="utf8") as corrupted_keys_file:
    bib_db2 = bibtexparser.load(corrupted_keys_file)

print('len of shared with corrupted keys: ', len(bib_db2.entries))

for book in bib_db2.entries:
    if 'title' not in book.keys():
        noname1 +=1
        k = ('%s %s %s' % (noname1,'year', str(book.get('year'))))
        print('no title ', k, '\n', book)
    elif 'year' not in book.keys():
        k = str(book.get('title'))
    # noyear1 += 1
  #      k = ('%s %s' % str(book.get('title'), noyear))
    else:
        k = ('%s %s %s' % (str(book.get('title')), 'year', str(book.get('year'))))
    if k in corrupted_keys:
        duplicate1 += 1
        k = ('%s %s' % (str(duplicate1), str(k)))
    corrupted_keys.append(k)

    if k in normal_keys.keys() and book['ID'] != normal_keys.get(k):
        book['ID'] = normal_keys.get(k)

for key, value in normal_keys.items():
    if key not in corrupted_keys and (str(key).startswith(u'\d', 0, 2) is False):
        for book in bib_db.entries:
            if book.get('ID') == normal_keys.get(key):
                bib_db2.entries.append(book)
                #print (book)

print ('len of shared with cleaned keys: ', len(bib_db2.entries))

with open('shared2.bib', 'w', encoding='utf8') as shared_file:
   bibtexparser.dump(bib_db2, shared_file)