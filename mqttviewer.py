from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__)

@app.route("/data.json")
def data():
    connection = sqlite3.connect("/mnt/nas/mqttdata.db")
    cursor = connection.cursor()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/OG/t'")
    results1 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/EG/t'")
    results2 = cursor.fetchall()
    cursor.execute("select CAST(strftime('%s',timestamp) AS INT)*1000, value from table_data where topic='room/UG/t'")
    results3 = cursor.fetchall()
    #print results
    return json.dumps({'results1': results1, 'results2': results2, 'results3': results3})

@app.route("/temperatures.json")
def temperatures_data():
    connection = sqlite3.connect("/mnt/nas/mqttdata.db")
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

if __name__ == '__main__':
    app.run(
    debug=True,
    threaded=True,
    host='192.168.2.201'
)
