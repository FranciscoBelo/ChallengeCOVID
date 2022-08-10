from re import A
import psycopg2;
import json;
import csv;

from datetime import date
#Connections
conn = psycopg2.connect(
    host="XXXX",
    database="XXXX",
    user="XXXX",
    password="XXXX")

cursor = conn.cursor()


def loadjson(conn,fileName):
    with open(fileName) as json_data:
        #load data in record_list
        record_list = json.load(json_data)
        # enumerate over the record
        for i, record_dict in enumerate(record_list):
        # iterate over the values of each record dict object
            values = []
            columns = list(record_dict.keys())
            sql_string = 'INSERT INTO {} '.format('datacovid14') + "(" + ', '.join(columns) + ") VALUES "
            for col_names, val in record_dict.items():
                if type(val) == str:
                    #remove spaces
                    val = val.replace("'", "''")
                    val = "'" + val + "'"
                values += [ str(val) ]
                # join the list of values
            sql_string += "(" + ', '.join(values) + ")"
            #execute quety one by one
            cursor.execute(sql_string)
conn.commit()




#def loadcsv(conn, fileName):
    ## Function for Load csv file in Database
with open('countries of the world.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # Skip the header row.
    for row in reader:
        #In any cases i have a spaces in file and i need load clearValues
        clearList = list(map(lambda n: n.strip(), row))
        #Debug
        print(clearList)
        cursor.execute(
        "INSERT INTO countrys VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s)",
        clearList
        )
conn.commit()

#loadcsv(conn,'countries of the world.csv')
#loadjson(conn,'opendatacovid19.json')



#Function for Pipeline

#Control table to extract new data in json file;
#It's an Extract per day , the possible solution is a batch or run is code in pipeline for example datafactory;
#The check json file function has a new year_weak for the country
#Example South Sudan, 2022-02 if you have 2022-02 in the json file you will insert new information in the table;


with open('opendatacovid19.json') as json_data:
        record_list = json.load(json_data)
        cursor.execute('select * from controltablecovid14')
        ctrtable = cursor.fetchall()
        for i in range(0 ,len(ctrtable)):
            for j in range(0,len(record_list)):
                if(ctrtable[i][1] == record_list[j]['country'] and ctrtable[i][0] == record_list[j]['year_week'] ):
                    #print(record_list[j])
                    values = []
                    columns = list(record_list[j].keys())
                    sql_string = 'INSERT INTO {} '.format('datacovid14') + "(" + ', '.join(columns) + ") VALUES "
                    for col_names , val in record_list[j].items():
                        #print(val)
                        if type(val) == str:
                            #remove spaces
                            val = val.replace("'", "''")
                            val = "'" + val + "'"
                        values += [ str(val) ]
                        # join the list of values
                    sql_string += "(" + ', '.join(values) + ")"
                    cursor.execute(sql_string)
                # update control table with recet weak_year
                sql_update = 'update  controltablecovid14 set year_weak = {0} where country = {1}'.format(date.today().strftime("%Y-%V"),record_list[j]['country'])
conn.commit()

