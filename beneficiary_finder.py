import re

file_reader=open("New-stats/report.txt","r")
txt=file_reader.read()
beneficiaries=re.findall(r"\d\.\s.+\D",txt)
file_reader.close()

file_writer=open("New-stats/beneficiaries.txt","w")
for beneficiary in beneficiaries:
    file_writer.write(beneficiary[3:])
file_writer.close()

print(beneficiaries)