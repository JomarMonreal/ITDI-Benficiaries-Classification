import nltk
import re
import quick_sorter
import statistics
from nltk.corpus import stopwords
stopwords=set(stopwords.words('english'))

def addEnter(text):
    return text+"\n"
def stringify_2d(list):
    for i in range(len(list)):
        list[i]=list[i][0] + "," + str(list[i][1])
    return list

#combine beneficiaries
file_reader=open("New-stats/beneficiaries.txt","r")
lines=file_reader.readlines()
beneficiaries=set()
for line in lines:
    line=line[:-1]
    line=re.sub(r"[^\s\w-]","",line)
    if line !="":
        beneficiaries.add(line.lower())
file_reader.close()

file_writer=open("New-stats/beneficiaries_sorted.txt","w")
for beneficiary in beneficiaries:
    file_writer.write(beneficiary+"\n")
file_writer.close()


#get keyworrds of classification
keywords=set()
for beneficiary in beneficiaries:
    keywords=keywords.union(set(beneficiary.split(" ")))
for stopword in stopwords:
    keywords.discard(stopword)
keywords.discard("")

#find the occurences of each keyword
file_reader=open("New-stats/beneficiaries_sorted.txt","r")
document=file_reader.read()
keywords_counts=[]
for keyword in keywords:
    keywords_counts.append([keyword,document.count(keyword)])
file_reader.close()

#compute for median
counts=[]
for keyword_count in keywords_counts:
    if keyword_count[1]!=1:
        counts.append(keyword_count[1])
print(statistics.median_high(counts))

#print keywords and count
file_writer=open("New-stats/keywords_count.csv","w")
quick_sorter.quickSort2D(keywords_counts,0,len(keywords_counts)-1)
keywords_counts=stringify_2d(keywords_counts)
keywords_counts=reversed(keywords_counts)
keywords_counts=map(addEnter,keywords_counts)
file_writer.writelines(keywords_counts)
file_writer.close()


