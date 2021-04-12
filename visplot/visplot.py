"""
visplot.py

written by: Oliver Cordes 2021-04-11
changed by: Oliver Cordes 2021-04-12

"""


from astropy.visualization import time_support
import os, sys

# standard imports
import numpy as np
import matplotlib.pyplot as plt
import astropy

import astropy.coordinates as coord

from astropy.coordinates import AltAz

import datetime
from astropy.time import Time
from astropy import units as u
from astropy.timeseries import TimeSeries

# add the astropy plot style for matplotlib
from astropy.visualization import astropy_mpl_style, quantity_support, time_support
plt.style.use(astropy_mpl_style)
quantity_support()
time_support()


# load some additional observatories
import visplot.observatories
import visplot.sunrise


def day_visibility(obj, time_midnight, location, num_elements=100):
    sun_set = visplot.sunrise.sunset(location, time_midnight, sun_limit=-18.*u.deg)
    sun_rise = visplot.sunrise.sunrise(location, time_midnight, sun_limit=-18.*u.deg)
    #visplot.sunrise.checkplot(location, time_midnight)

    # it makes only sense to look for object altutdes during the night time 
    times = sun_set + np.linspace(0,1,num_elements)*(sun_rise-sun_set)

    alt = obj.transform_to(AltAz(obstime=times, location=location)).alt

    return min(alt), max(alt) 


def max_visibility(name, location, start_day):
    obj_coord = coord.SkyCoord.from_name(name)
    print(obj_coord)
    
    obs_time = Time(start_day)

    nr_days = 180
    deltas = np.arange(nr_days)*u.day
    times = obs_time + deltas
    maxs = np.zeros(nr_days)
    mins = np.zeros(nr_days)
    
    for i in range(nr_days):
        minv, maxv = day_visibility(obj_coord, times[i], location)
        maxs[i] = maxv/u.deg
        mins[i] = minv/u.deg

    print(maxs)
    fig, ax = plt.subplots()
    ax.set_ylim(0,90)
    ax.plot(times, maxs)
    plt.show()

"""
main function 
"""
def main():
    name = 'PG1605+072'
    name = 'HS0659+5734'
    location = visplot.observatories.CalarAlto()
    start_day = '2021-04-12'
    max_visibility(name, location, start_day)
