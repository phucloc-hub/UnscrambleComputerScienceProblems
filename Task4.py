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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

texters_number_list = list() 
for i in range(len(texts)):
    texters_number_list.append(texts[i][0])
    texters_number_list.append(texts[i][1])

texters = set(texters_number_list)
callers = set()
call_recievers = set()
for i in range(len(calls)):
    callers.add(calls[i][0])
    call_recievers.add(calls[i][1])

telemarkerters = callers - (texters | call_recievers)
print("These numbers could be telemarketers:")

for number in sorted(telemarkerters):
    print(number)