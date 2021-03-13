"""
ID: smaylni1
LANG: PYTHON3
PROB: friday
"""

f = open('friday.in', 'r')
years = int(f.read())
f.close()

week_counts = [0, 0, 0, 0, 0, 0, 0]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

def counter(days_, week_counts, months, febr):
    global days
    for j in range(12):
        if (j == 1):
            days_ += 12
            week_counts[days_ % 7] += 1
            days_ += febr - 12
        else:
            days_ += 12
            week_counts[days_ % 7] += 1
            days_ += months[j] - 12
    days = days_
    return week_counts

for i in range(1900, 1900 + years, 1):
    if (i % 100 == 0):
        if (i % 400 == 0):
            counter(days, week_counts, months, 29)
        else:
            counter(days, week_counts, months, 28)
    elif (i % 4 == 0):
        counter(days, week_counts, months, 29)
    else:
        counter(days, week_counts, months, 28)

result = str(week_counts[5]) + ' ' + str(week_counts[6])

for i in range(5):
    result = result + ' ' + str(week_counts[i])

print(week_counts)

f = open('friday.out', 'w')
f.write(result + '\n')
f.close()
