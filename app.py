from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper (ORM)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from IPython.display import display

def calc_temps(start_date, end_date):
    return(engine.execute('SELECT MIN(measurement.tobs), MAX(measurement.tobs), AVG(measurement.tobs) FROM measurement WHERE measurement.date BETWEEN "'+ start_date +'" AND "'+ end_date +'"'))
    
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the data as json"""
    prec_data_last_12m = engine.execute('SELECT measurement.date, measurement.prcp FROM measurement WHERE measurement.date > "2016-08-23"')
    data_dict = {}
    for row in prec_data_last_12m:
        data_dict[row[0]] = row[1]
    return jsonify(data_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return the data as json"""
    avlbl_stn = engine.execute('SELECT measurement.station FROM measurement GROUP BY measurement.station')
    stn_lst = [row[0] for row in avlbl_stn]
    return jsonify(stn_lst)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the data as json"""
    stns_count = engine.execute('SELECT measurement.station, COUNT (measurement.station) FROM measurement GROUP BY measurement.station ORDER BY COUNT (measurement.station) DESC')
    stns_count_lst = [row[0] for row in stns_count]
    tmp_last_12m_mas = engine.execute('SELECT measurement.date, measurement.tobs FROM measurement WHERE measurement.station LIKE "'+ stns_count_lst[0] + '%" AND measurement.date > "2016-08-23"')
    tmp_lst = []
    for row in tmp_last_12m_mas:
        tmp_lst.append(row[1])
    
    return jsonify(tmp_lst)

@app.route("/api/v1.0/<start>")
def start(start):
    """Return the data as json"""
    data = calc_temps(start,'2017-08-23')
    data_lst = {}
    names = ['Minimum Temperature','Maximum Temparature','Avgrage Temparature']
    for row in data :
        data = row
        for name,col in zip(names,data):
            data_lst[name] = col
    #print(data)
    return jsonify(data_lst)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    """Return the data as json"""
    data = calc_temps(start,end)
    data_lst = {}
    names = ['Minimum Temperature','Maximum Temparature','Avgrage Temparature']
    for row in data :
        data = row
        for name,col in zip(names,data):
            data_lst[name] = col
    #print(data)
    return jsonify(data_lst)

@app.route("/")
def welcome():
    return (
        f"<b>Welcome to Home page!</b><br/><br/>"        
        f"<b>Note:</b> Date range is between 2010-01-1 and 2017-08-23. Date must be entered in YYYY-MM-DD format.<br/><br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>" # Please enter "start" date (YYYY-MM-DD) manually
        f"/api/v1.0/start/end" # Please enter "start" and "end" dates (YYYY-MM-DD) manually
    )

if __name__ == "__main__":
    app.run(debug=True)