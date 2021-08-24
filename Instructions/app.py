# ## Step 2 - Climate App
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import statistics
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
# * Use Flask to create your routes.
app = Flask(__name__)
# ### Routes
# * `/`
#   * Home page.
#   * List all routes that are available.
@app.route("/")
def home():
    return f"Welcome to our climate home page! <br/>Available Routes:<br/>Precipitation: /api/v1.0/precipitation <br/>Stations: /api/v1.0/stations <br/>Temperatures: /api/v1.0/tobs <br/>Temp Ranges: /api/v1.0/<start>` or `/api/v1.0/<start>/<end> <br/>(Replace start and end with the first and last date for the desired date range) <br/> (Dates are formatted as Year-mo-da)"
# * `/api/v1.0/precipitation`
#   * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
#   * Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    return "Welcome to our precipitation page!"
    session = Session(engine)
    results = session.query(measurement.prcp).all()
    session.close()
    all_temps = list(np.ravel(results))
    return jsonify(all_temps)
# * `/api/v1.0/stations`
#   * Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    return "Welcome to our stations page!"
    session = Session(engine)
    results = session.query(station.station).all()
    session.close()
    all_stationss = list(np.ravel(results))
    return jsonify(all_stations)
# * `/api/v1.0/tobs`
#   * Query the dates and temperature observations of the most active station for the last year of data.
#   * Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    return "Welcome to our temperature page!"
    session = Session(engine)
    results = session.query(measurement.date, measurement.tobs).filter_by(station="USC00519281").filter(measurement.date.between("2016-08-23", "2017-08-23"))
    session.close()
    results = results.sort_values(['date'], ascending=True)
    results.set_index('date')
    station_one = list(np.ravel(results))
    return jsonify(station_one)
# * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>` and `/api/v1.0/<start>/<end>")
def tobs_dates():
    return "Welcome to our climate home page!"
    start_date = start
    end_date = end
    results = session.query(measurement.date, measurement.tobs).filter_by(station="USC00519281").filter(measurement.date.between(start, end))
    session.close()
    results = results.sort_values(['date'], ascending=True)
    results.set_index('date')
    station_one = list(np.ravel(results))
    return jsonify(station_one)
## Hints

# * You will need to join the station and measurement tables for some of the queries.

# * Use Flask `jsonify` to convert your API data into a valid JSON response object.