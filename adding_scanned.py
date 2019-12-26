# -*- coding: utf-8 -*-
import bibtexparser, os

os.chdir(r"c:\users\lenovo\desktop")

scanned = []

with open('shared.bib', encoding="utf8") as scanned_file:
    bib_db = bibtexparser.load(scanned_file)

for book in bib_db.entries:
    if 'scanned' in book.keys():
        if book.get('title') == None:
            k = ('%s %s' % (str(book.get('title')), str(book.get('year'))))
        else:
            k = str(book.get('title'))
        #if k in scanned: ##checking duplicates is not required
            #print (k)
        scanned.append(k)

with open('normal_keys.bib', encoding="utf8") as not_scanned_file:
    bib_db2 = bibtexparser.load(not_scanned_file)

for book in bib_db2.entries:
    if book.get('title') == None:
        k = ('%s %s' % (str(book.get('title')), str(book.get('year'))))
    else:
        k = book.get('title')
    if k in scanned:
        book['scanned'] = 'Y'

with open('oya_lib_scanned.bib', 'w', encoding='utf8') as shared_file:
   bibtexparser.dump(bib_db2, shared_file)