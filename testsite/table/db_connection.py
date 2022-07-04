import xml.etree.ElementTree as ET
import gspread
import psycopg2
import requests

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

sa = gspread.service_account(filename='F:/Projects/googletopostgres/testsite/table/creds.json')
hostname = 'localhost'
database = 'testdatabase'
username = 'postgres'
pwd = 'qwerty123'
port_id = 5432


def databasecreation():
    conn = psycopg2.connect(user=username, password=pwd)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'testdatabase'")
    exists = cur.fetchone()
    if not exists:
        cur.execute('CREATE DATABASE testdatabase')
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


def databaseupdate(dollar, google):
    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:

            with conn.cursor() as cur:
                cur.execute('''DROP TABLE IF EXISTS test''')
                create_script = ''' CREATE TABLE IF NOT EXISTS test (
                id       SERIAL PRIMARY KEY,
                заказ_№ varchar(40) NOT NULL,
                стоимость_в_$ int,
                срок_поставки varchar(30),
                стоимость_в_RUB int) '''

                cur.execute(create_script)

                insert_script = 'INSERT INTO test (заказ_№, стоимость_в_$, срок_поставки, стоимость_в_RUB) VALUES (%s, %s, %s, %s)'
                for i in range(1, len(google)):
                    if google[i][1] == '' and google[i][2] == '' and google[i][3] == '':
                        continue
                    else:
                        if google[i][2] == '':
                            google[i][2] = 0
                        insert_value = (
                            google[i][1], int(google[i][2]), google[i][3], (round(int(google[i][2]) * dollar)))
                        cur.execute(insert_script, insert_value)
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def updatetable():
    # get rub/$ exchange rate from XML string
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)
    treeOne = ET.fromstring(r.text)
    z = treeOne.findtext('.//*[@ID="R01235"]/Value')
    dollar = float(z.replace(',', '.'))

    # get google spreadsheets update
    sh = sa.open('Копия test')
    wks = sh.worksheet('Лист1')
    google = wks.get_all_values()

    databasecreation()
    databaseupdate(dollar=dollar, google=google)
