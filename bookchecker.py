# -*- coding: utf-8 -*-
import bibtexparser, os, re, time
start_time = time.time()

os.chdir(r"c:\users\lenovo\desktop")
books = []
year = re.compile(r'\.\d{4}$')

with open(u'Готово.txt', 'r', encoding='utf-8-sig') as textfile:
    for line in textfile:
        entry = {}
        if line.strip().endswith(u'.pdf'):
            line = line.strip()[:-4]
        if line.strip().split('.')[0].isdigit():
            line = ' '.join(line.strip().split('. ')[1:]) #delete index
        if ' - ' in line:
            entry['author'] = line.strip().split(' - ')[0]
            line = ''.join(line.strip().split(' - ')[1:])
        if year.search(line.strip()) != None:
            entry['year'] = str(year.search(line.strip()).group(0))[1:]
            line = ''.join(line.strip()[:-5])
        entry['title'] = ''.join((line.strip()))
            #if (x for x in entry.get('title').split() if x[0].isupper())
        entry['scanned'] = 'Y'
        entry['ENTRYTYPE'] = 'book'
        entry['ID'] = 'none'
        books.append(entry)
        #print (line.strip('.').split('-')[0])
print ('ready ', len(books))

print (time.time() - start_time)

with open('oya_lib_scanned.bib', encoding="utf8") as file:
    bib_db = bibtexparser.load(file)
print ('len of bib ', len(bib_db.entries))

for b in books:
    bib_db.entries.append(b)

print ('new len of bib ', len(bib_db.entries))

with open('new_oya_lib.bib', 'w', encoding='utf8') as f2:
   bibtexparser.dump(bib_db, f2)