"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
resultSet = set()
length_of_texts = len(texts)
length_of_calls = len(calls)
i = 0
while length_of_texts > i:
	resultSet.add(texts[i][0])
	resultSet.add(texts[i][1])
	i += 1
i = 0
while length_of_calls > i:
	resultSet.add(calls[i][0])
	resultSet.add(calls[i][0])
	i += 1
print("There are {} different telephone numbers in the records.".format(
    len(resultSet)))