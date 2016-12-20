from datetime import datetime


dates = []
dates.append('Jun 1 2005  1:33PM')
dates.append('Aug 28 1999 12:00AM')
from datetime import datetime
for d in dates:
date = datetime.strptime(d, '%b %d %Y %I:%M%p')
print (type(date))
print (date)