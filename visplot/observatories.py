"""
visplot/observatories.py

written by: Oliver Cordes 2021-04-11
changed by: Oliver Cordes 2021-04-11

"""

import astropy.units as u
import astropy.coordinates as coord


def create_location(lat, lon, height):
    lat = coord.Latitude(lat, u.deg)
    lon = coord.Angle(lon, u.deg)

    return coord.EarthLocation(lat=lat, lon=lon, height=height*u.m)



def CalarAlto():
    lat = (37, 13, 25.00)
    #lat = (37, 13, 0)
    lon = (2, 32, 46.00)
    #lon = (2, 32, 0)
    height = 2158 # m
    height = 2168

    return create_location(lat, lon, height)
