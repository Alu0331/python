import sys
from time import strptime, strftime
print(strftime("%H:%M:%S",strptime(input(),"%I:%M:%S%p")))

'''strptime translates to
"parse (convert) string to datetime object."


strftime translates to
"create formatted string for given time/date/datetime object according to specified format."'''