"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
year = 2016
month = 9
phone_and_time = dict()
for call,reci,at_time,dura_tele in calls:
    date = datetime.strptime(at_time, "%d-%m-%Y %H:%M:%S")
    if date.year == year and date.month == month:
        phone_and_time[call] += float(dura_tele)
        phone_and_time[reci] += float(dura_tele)
number_rs = ""
total_time_rs = 0.0
for key in phone_and_time:
    if total_time_rs < phone_and_time[key]:
	total_time_rs = phone_and_time[key]
	number_rs = key
print("{} spent the longest time, {} seconds, on the phone during 
September 2016.".format(number_rs,total_time_rs))