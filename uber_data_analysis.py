import mysql.connector

mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        passwd = "password123",
        database = "uber"
        )

print (mydb)

import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import datetime
import time
from matplotlib import pyplot as plt

bigtable = mydb.cursor()
bigtable.execute("""select date_apr, count(date_apr) from bigtable group by date_apr 
                 union select date_may, count(date_may) from bigtable group by date_may 
                 union select date_jun, count(date_jun) from bigtable group by date_jun
                 union select date_jul, count(date_jul) from bigtable group by date_jul 
                 union select date_aug, count(date_aug) from bigtable group by date_aug""")

rows = bigtable.fetchall()

for r in rows:
    plt.bar(r[0],r[1])


plt.ylabel('# of trips')
plt.xlabel('date')
plt.xticks(rotation=90)
plt.title('uber rides')
plt.figure(1)
plt.show()   

april = mydb.cursor()
april.execute("SELECT date_apr, count(date_apr) from bigtable group by date_apr")
rows = april.fetchall()

for x in rows:
    a = (x[0]) 
    b = (x[1])
    plt.bar(a, b)
 
plt.ylabel('# of trips')
plt.xlabel('date_apr')
plt.xticks(rotation=90)
plt.title('uber rides')
plt.figure(1)
plt.show()   

may = mydb.cursor()
may.execute("select date_may, count(date_may) from bigtable group by date_may")
rows1 = may.fetchall()

for y in rows1:
    c = (y[0])
    d = (y[1])
    plt.bar(c,d)

plt.ylabel('# of trips')
plt.xlabel('date_may')
plt.xticks(rotation=90)
plt.title('uber rides')
plt.figure(1)
plt.show()

june = mydb.cursor()
june.execute("select date_jun, count(date_jun) from bigtable group by date_jun")
rows1 = june.fetchall()

for z in rows1:
    plt.bar(z[0],z[1])

plt.ylabel('# of trips')
plt.xlabel('date_jun')
plt.xticks(rotation=90)
plt.title('uber rides')
plt.figure(1)
plt.show()  

july = mydb.cursor()
july.execute("select date_jul, count(date_jul) from bigtable group by date_jul")
rows1 = july.fetchall()

for e in rows1:
    plt.bar(e[0],e[1])

plt.ylabel('# of trips')
plt.xlabel('date_jul')
plt.xticks(rotation=90)
plt.title('uber rides')
plt.figure(1)
plt.show()   

aug = mydb.cursor()
aug.execute("select date_aug, count(date_aug) from bigtable group by date_aug")
rows1 = aug.fetchall()

for q in rows1:
    plt.bar(q[0],q[1])

plt.ylabel('# of trips')
plt.xlabel('date_aug')
plt.xticks(rotation=90)
plt.title('uber rides')
plt.figure(1)
plt.show() 


