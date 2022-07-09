# Google-to-postgres case
Django+react js ASGI-app made for test assignment. 
Task was to make a python script that could get data from google sheets,
(https://docs.google.com/spreadsheets/d/11REUz1qelflIaaGOcoWVTAGZOfXiXim1-bBb5SeA-Uo/edit#gid=0)
and put it in database. The conditions were:
1.  Get data with the Google API.
2.  Add the data in the database as is, with the addition of the "cost in rubles" column.
    a. Need to create DB by yourself with postgreSQL.
    b. Get ruble exchange rate from bank of russia site https://www.cbr.ru/development/SXML/
3.  The script runs all the time to ensure that the data is updated online (rows in the Google Sheets table can be deleted, added and changed).
4.  Additions: Development of a one-page web application based on Django or Flask. Front-end React.

How it works: Firstly, whenever a change is made to google sheets, 
the Google API sends a POST request(webhook) to django backend. 
After the request, Django updates the database with the data from google sheets. 
After that, backend sends the data to the frontend react js through websocket connection and updates it in real time. 
