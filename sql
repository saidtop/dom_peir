import sqlite3

con = sqlite3.connect('test1.db')
cursor = con.cursor()
cursor.execute("""
    DROP TABLE Singer
    """) 


cursor.execute("""
    CREATE TABLE Singer (
    id INT,
    name TEXT,
    data DATE,
    role TEXT,
    gender TEXT
    )
	""")
data_list = [(1,'Тейлор Свифт',1989-12-19,""" американская кантри-поп-исполнительница, автор песен и актриса. Второй альбом Свифт Fearless был выпущен в 2008 году и стал международным прорывом.
	""",'Женщина'),
(2,"Курбан",2021-12-12,"BAN FOR kurBAN",'мужыг'),
(3,"Даниил",1666-6-1,'пришел из будущего в прошлое которое является будущем o_O o_O ','пришелец'),
(4,"Said",1999-9-9,'sverxrazum',"galaktus"),
(5,"Sultanmurad",1111-1-1,'mydres pribivshi is daleka'," МУЖЫГГГ $_$ $_$")]
cursor.executemany("""INSERT INTO Singer VALUES 
    (?, ?, ?, ?, ?)""", data_list)
cursor.execute("SELECT * FROM Singer") 
print(cursor.fetchall()) 
con.commit() 
cursor.close() 
con.close() 
