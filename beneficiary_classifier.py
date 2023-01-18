import re
beneficiaries=[]

file_reader=open("New-stats/beneficiaries.txt","r")
beneficiaries=set(file_reader.readlines())
file_reader.close()

file_reader=open("New-stats/keywords_count.csv","r")
lines=file_reader.readlines()
classifiers=[]
for line in lines:
    keyword_count=line.split(",")
    classifiers.append(keyword_count[0])
file_reader.close()

classified_beneficiaries={}
for classifier in classifiers:
    classified_beneficiaries[classifier]=set()

included_beneficiaries=set()
for beneficiary in beneficiaries:
    for classifier in classifiers:
        if classifier in beneficiary.lower() and len(classifier)>1:
            classified_beneficiaries[classifier].add(beneficiary[:-1])
            included_beneficiaries.add(beneficiary[:-1])


file_writer=open("New-stats/classified_beneficiaries.csv","w")

for base_classifier in classified_beneficiaries:
    classified_beneficiaries_copy=dict(classified_beneficiaries)
    for classifier in classified_beneficiaries:
        if base_classifier!=classifier:
            intersection=classified_beneficiaries[base_classifier].intersection(classified_beneficiaries_copy[classifier])
            if len(intersection)!=0:
                classified_beneficiaries_copy[base_classifier]=classified_beneficiaries_copy[base_classifier].union(classified_beneficiaries_copy[classifier])
                classified_beneficiaries_copy.pop(classifier)
                break
    classified_beneficiaries[base_classifier]=classified_beneficiaries_copy[base_classifier]


for classifier in classified_beneficiaries:
    if len(classified_beneficiaries[classifier]):
        file_writer.write(",".join([classifier,str(len(classified_beneficiaries[classifier])),str(classified_beneficiaries[classifier]),"\n"]))
file_writer.close()


"""
for classifier in classified_beneficiaries:
    if len(classified_beneficiaries[classifier])>1:
        beneficiary_count=len(classified_beneficiaries[classifier])
        classifier_count.append([classifier,beneficiary_count])
        

        print(classifier,len(classified_beneficiaries[classifier]))
        print(classified_beneficiaries[classifier])
        pair=",".join([classifier,str(beneficiary_count)])
        file_writer.write(pair)
        file_writer.write("\n")
"""