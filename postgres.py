import psycopg2
import unicodecsv as csv

conn = psycopg2.connect(database = "tweettext", user = "postgres", password = "1234")
cursor = conn.cursor()

#f = open("/Users/michelleglewis/Downloads/ira_tweets_csv_hashed.csv", "rb")
userinput = input('Enter name of file ')
f = open(userinput, "rb")
df = csv.reader(f, encoding = 'utf-8')

labels = next(df)

list_of_types = ["int", "text", "text", "text", "text",  "text","text", "int", "int","int", "text","text", "int", "text", "text", "int", "int", "int", "text", "int", "int", "text", "text", "int", "int",  "int", "int", "text",  "text", "text", "text"]

cursor.execute("DROP TABLE table1;")
create_table_string = "CREATE TABLE IF NOT EXISTS table1("
for i in range(31):
    create_table_string += labels[i] + " " + list_of_types[i] + ", "
create_table_string = create_table_string[:-2]

create_table_string+= ");"


cursor.execute(create_table_string)
conn.commit()

