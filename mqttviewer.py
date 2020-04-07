from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__)
DB_PATH = "/mnt/nas/mqttdata.db"
HOST_IP = "192.168.2.201"

@app.route("/data.json")
def data():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/OG/t'")
    results1 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/EG/t'")
    results2 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/UG/t'")
    results3 = cursor.fetchall()
    #print results
    return json.dumps({'results1': results1, 'results2': results2, 'results3': results3})

@app.route("/humidities.json")
def humidities_data():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/OG/h'")
    results1 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/EG/h'")
    results2 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/UG/h'")
    results3 = cursor.fetchall()
    #print results
    return json.dumps({'results1': results1, 'results2': results2, 'results3': results3})

@app.route("/temperatures.json")
def temperatures_data():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/OG/t'")
    results1 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/EG/t'")
    results2 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/UG/t'")
    results3 = cursor.fetchall()
    #print results
    return json.dumps({'results1': results1, 'results2': results2, 'results3': results3})

@app.route("/graph")
def graph():
    return render_template('graph.html')

@app.route("/temperatures")
def temperatures():
    return render_template('temperatures.html')

@app.route("/humidities")
def humidities():
    return render_template('humidities.html')

if __name__ == '__main__':
    app.run(
    debug = True,
    threaded = True,
    host = HOST_IP
)
