import datetime
import re

now = str(datetime.datetime.now())
now = now.split()[0]
now = now.split("-")
month = now[1]
day = now[2]
year = now[0]
date = f"{month}/{day}/{year}"

if(re.search("(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d",date)):
    print(date)