import plotly.graph_objects as go
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'nugroho21',
    database = 'world'
)


query1 = '''select country.Name as Negara_ASEAN, country.Population as Populasi_Negara, GNP, city.Name as IbuKota, city.Population as Populasi_Ibukota from country inner join city
on country.Capital = city.ID where country.Name = 'Brunei' or country.Name ='Cambodia' or country.Name ='East Timor' or country.Name ='Indonesia' or country.Name ='Laos' or country.Name ='Malaysia' or country.Name ='Myanmar' or country.Name ='Philippines'or country.Name ='Singapore' or country.Name ='Thailand' or country.Name ='Vietnam' order by country.Name asc'''

df = pd.read_sql(query1, con=db)
negara = list(df['Negara_ASEAN'])
populasi = list(df['Populasi_Negara'])
gnp= list(df['GNP'])

x= negara
y1= populasi
y2= gnp

##-------------- Nomor 1 ------------
# plt.style.use('seaborn')
# for a,b in zip(x,y1):
#     plt.text(a,b, str(b), ha='center', size=6)
# plt.bar(x,y1,color=['red','green','black','yellow','blue','lightblue','lightgreen','pink','magenta','purple','orange'])
# plt.title('Populasi Negara ASEAN')
# plt.xlabel('Negara')
# plt.ylabel('Populasi')
# plt.xticks(rotation=45, size=6)
# plt.grid(True)
# plt.show()

##-------------- Nomor 2 ------------
# plt.style.use('seaborn')
# color = ['red','blue','green','yellow','lightgreen','lightblue','pink','purple','brown','lightgrey','orange']
# plt.pie(
#     y1, labels=x, colors=color,
#     startangle=360, counterclock=True,
#     autopct='%1.1f%%',
#     textprops={'color':'black'}
# )
# plt.title('Presentase Penduduk Asean')
# plt.show()

##-------------- Nomor 3 ------------
# plt.style.use('seaborn')
# for a,b in zip(x,y2):
#     plt.text(a,b, str(b), ha='center', size=6)
# plt.bar(x,y2,color=['red','green','black','yellow','blue','lightblue','lightgreen','pink','magenta','purple','orange'])
# plt.title('Pendapatan Bruto ASEAN')
# plt.xlabel('Negara')
# plt.ylabel('Populasi')
# plt.xticks(rotation=45, size=6)
# plt.grid(True)
# plt.show()


##--------------- Nomor 4 -------------
query2 = """
SELECT Name as Negara_ASEAN, surfacearea as Luas_Daratan
FROM country
WHERE Name in ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
ORDER BY Negara_ASEAN ASC;
"""

df = pd.read_sql(query2, con=db)

# ===PLOT

x = list(df['Negara_ASEAN'])
y = list(df['Luas_Daratan'])

warna = ['red', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'gold', 'lightblue', 'blue']
_,_,autotexts = plt.pie(y, labels=x, colors=warna,
    autopct = '%1f%%',
    textprops={'color':'black'})
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(6)
plt.title('Persentase Luas Daratan ASEAN')
plt.show()