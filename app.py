#import dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#Welcome/home page
@app.route("/")
def welcome():
    return (
        f"Welcome to my Hawaii Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start><end><br/>"
        )

#Precipitation page
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create the session (link) from Python to the DB
    session = Session(engine)

    # Query the precipitation amounts in the past year
    year_dates = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip_amts = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_dates).all()

    # Close the session
    session.close()

    # Create a dictionary of the date and precipitation data
    date_precip_dict = {}
    for entry in precip_amts:
        date_precip_dict[entry[0]] = entry[1]

    return jsonify(date_precip_dict)

#Stations page
@app.route("/api/v1.0/stations")
def stations():
    # Create the session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.name, Station.station).all()

    # Close the session
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

#Observed temperature page
@app.route("/api/v1.0/tobs")
def temps():
     # Create the session (link) from Python to the DB
    session = Session(engine)

    # Query the most active station
    #most_active = session.query(Measurement.station, func.count(Measurement.date)).\
       # group_by(Measurement.station).\
        #order_by(func.count(Measurement.date).desc()).first()

    #Query the dates for the past year
    year_dates = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the dates and temperature observations of the most active station for the last year of data.
    year_temp = session.query(Measurement.tobs).\
        filter(Measurement.date >= year_dates).\
        filter(Measurement.station == 'USC00519281').all()
    
    # Close the session
    session.close()

    # Convert list of tuples into normal list
    results = list(np.ravel(year_temp))

    return jsonify(results)

#Start date
@app.route("/api/v1.0/<start>")
def start(start):
     # Create the session (link) from Python to the DB
    session = Session(engine)

    temps = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),\
        func.avg(Measurement.tobs)).\
        group_by(Measurement.date).all()

    # Close the session
    session.close()

    # Convert list of tuples into normal list
    start_temps = list(np.ravel(temps))

    return jsonify(start_temps)

#Start/end date
@app.route("/api/v1.0/<start>/<end>")
def start_end(start2,end):
     # Create the session (link) from Python to the DB
    session = Session(engine)

        # Query the minimum, maximum, and average temperature from the start date
    temps2 = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).\
        group_by(Measurement.date).all()

    # Close the session
    session.close()

    # Convert list of tuples into normal list
    start_end_temps = list(np.ravel(temps2))

    return jsonify(start_end_temps)

# Adding a debugger
if __name__ == "__main__":
    app.run(debug=True)