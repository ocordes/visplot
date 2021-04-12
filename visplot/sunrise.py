"""
visplot/sunrise.py

written by: Oliver Cordes 2021-04-12
changed by: Oliver Cordes 2021-04-12

"""

from astropy import units as u

from astropy.coordinates import get_sun, AltAz

import numpy as np

import matplotlib.pyplot as plt


astro_night = -18.*u.deg

def sunrise(location, day, sun_limit=0.*u.deg):
    time1 = day
    time2 = day + 12*u.hour

    count = 0
    diff = 1*u.deg
    while (abs(diff) > 1e-6*u.deg) and (count < 100):
        alt1 = get_sun(time1).transform_to(AltAz(obstime=time1, location=location)).alt
        alt2 = get_sun(time2).transform_to(AltAz(obstime=time2, location=location)).alt
    
        diff = (alt1-alt2)
        if (alt1+alt2)/2. < sun_limit:
            time1 = time1 + (time2 - time1)/2.
        else:
            time2 = time1 + (time2 - time1)/2.

        count += 1

    if count == 100:
        print(f'Warning: Algorithm does not finished!')

    return time1


def sunset(location, day, sun_limit=0.*u.deg):
    time1 = day
    time2 = day - 12*u.hour

    count = 0
    diff = 1*u.deg
    while (abs(diff) > 1e-6*u.deg) and (count < 100):
        alt1 = get_sun(time1).transform_to(
            AltAz(obstime=time1, location=location)).alt
        alt2 = get_sun(time2).transform_to(
            AltAz(obstime=time2, location=location)).alt

        diff = (alt1-alt2)
        if (alt1+alt2)/2. < sun_limit:
            time1 = time1 + (time2 - time1)/2.
        else:
            time2 = time1 + (time2 - time1)/2.

        count += 1

    if count == 100:
        print(f'Warning: Algorithm does not finished!')

    return time1


def checkplot(location, day):
    delta_midnight = np.linspace(-12, 12, 1000)*u.hour
    times = day + delta_midnight

    alt = get_sun(times).transform_to(AltAz(obstime=times, location=location)).alt

    fig, ax = plt.subplots()
    ax.plot(delta_midnight, alt)

    plt.show()
