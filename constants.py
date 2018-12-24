'''
# constants
- Code By Michael Sherif Naguib
- license: MIT open source
- Date: 12/20/18
- @University of Tulsa
- Description: for storing constants of functions...
'''
# ========================== Predefined Transformations =======================
# Predefined Transformations: [MATRIX as [[A,B],[C,D]], SHIFTS as [X,Y], ROTATION ,PROBABILITY]
from numpy import array as na# NOT NP... NOTE: Numpy Array as na
from math import *

constants = {}

#Barnsley Fern
constants["bfern"] = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),0,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),0,0.07],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.07]
]

#Rose(like)
constants["rose"] = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),45,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),3,0.10],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.04]
]

#Koch Curve 
constants["koch"]=[
    [na([[0.3,0],[0,0.3]]),na([0,0]),0,0.25],
    [na([[0.16,0-0.23],[0.23,0.16]]),na([0.3,0]),0,0.25],
    [na([[0.16,0.23],[0-0.23,0.16]]),na([0.5,0.23]),0,0.25],
    [na([[0.3,0],[0,0.3]]),na([0.6,0]),0,0.25]
]

#Nathaniel's Galaxy
constants["natgalaxy"] = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),60,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),5,0.10],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.04]
]

#Serenpenski Triangle
constants["triangle"] = [
    [na([[0.5,0],[0,0.5]]),na([0,0]),0,0.33],
    [na([[0.5,0],[0,0.5]]),na([0.5,0]),0,0.33],
    [na([[0.5,0.0],[0.0,0.5]]),na([0.25,0.433]),0,0.34]
]

#The Golden Dragon: based off the golden ratio
constants["goldendragon"] = [
    [na([[0.62367,0-0.40337],[0.40337,0.62367]]),na([0,0]),0,0.5],
    [na([[0-0.37633,0-0.40337],[0.40337,0-0.37633]]),na([0.5,0]),0,0.5]
]
#Binary Tree (symetric ish ... the constants were adjusted...) 
constants["btree"]= [
    [na([[0.7,0],[0,0.7]]),na([0,1]),9,0.33],
    [na([[0.7,0],[0,0.7]]),na([0,1]),0-9,0.33],
    [na([[1,0],[0,1]]),na([0,0]),0,0.34]
]

#Golden Dragon Branch Variant
constants["branch"]=[
    [na([[0.62327,0-0.40337],[0.40337,0.62327]]),na([0,0]),32.8938,0.5],
    [na([[0-0.37633,0-0.40337],[0.40337,0-0.37633]]),na([1,0]),133.014178,0.5]
]
#Pentadentrite
constants["penta"]=pentadentrite=[
    [na([[0.341,0-0.071],[0.071,0.341]]),na([0,0]),0,0.17],
    [na([[0.038,0-0.346],[0.346,0.038]]),na([0.341,0.071]),0,0.17],
    [na([[0.341,0-0.071],[0.071,0.341]]),na([0.379,0.418]),0,0.17],
    [na([[0-0.234,0.258],[0-0.258,0-0.234]]),na([0.720,0.489]),0,0.17],
    [na([[0.173,0.302],[0-0.302,0.173]]),na([0.486,0.231]),0,0.16],
    [na([[0.341,0-0.071],[0.071,0.341]]),na([0.659,0-0.071]),0,0.16]
]

#Serenpenski Pentagon
constants["spentagon"]=pentadentrite=[
    [na([[0.382,0],[0,0.382]]),na([0,0]),0,0.2],
    [na([[0.382,0],[0,0.382]]),na([0.618,0]),0,0.2],
    [na([[0.382,0],[0,0.382]]),na([0.809,0.588]),0,0.2],
    [na([[0.382,0],[0,0.382]]),na([0.309,0.951]),0,0.2],
    [na([[0.382,0],[0,0.382]]),na([0-0.191,0.588]),0,0.2]
]

#Serenpenski Carpet
constants["scarpet"]= [
    [na([[1/3,0],[0,1/3]]),na([0,0]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([0,1/3]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([0,2/3]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([1/3,0]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([1/3,2/3]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([2/3,0]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([2/3,1/3]),0,1/8],
    [na([[1/3,0],[0,1/3]]),na([2/3,2/3]),0,1/8]
]

#Pythagorean Tree: (does not come out correctly...)
d=50
constants["pythagorean"] = [
    [
        na([[pow(cos(d),2),0-cos(d)*sin(d)],[cos(d)*sin(d),pow(cos(d),2)]]),
        na([0,1]),0,0.33
    ],
        [na([[pow(sin(d),2),cos(d)*sin(d)],[0-cos(d)*sin(d),pow(sin(d),2)]]),
        na([pow(cos(d),2),1 + cos(d)*sin(d)]),0,0.33
    ],
    [na([[1,0.0],[0.0,1]]),na([0,0]),0,0.34]
]

#Space Filling curve
constants["sfcurve"] = [
    [na([[0,0.5],[0-0.5,0]]),na([0,0.5]),0,0.25],
    [na([[0.5,0],[0,0.5]]),na([0,0.5]),0,0.25],
    [na([[0.5,0],[0,0.5]]),na([0.5,0.5]),0,0.25],
    [na([[0,0-0.5],[0.5,0]]),na([1,0]),0,0.25]
]

#Durer pentagon
r = (3 -sqrt(5))/2
constants["durer"] = [
    [na([[r,0],[0,r]]),na([0,0]),0,1/6],
    [na([[r,0],[0,r]]),na([0.618,0]),0,1/6],
    [na([[r,0],[0,r]]),na([0.809,0.588]),0,1/6],
    [na([[r,0],[0,r]]),na([0.309,0.951]),0,1/6],
    [na([[r,0],[0,r]]),na([0-0.191,0.588]),0,1/6],
    [na([[0-r,0],[0,0-r]]),na([0.691,0.951]),0,1/6]
]

#Koch Anti-Snowflake
constants["antisnow"] = [
    [na([[1/3,0],[0,1/3]]),na([0,0]),0,1/6],
    [na([[1/3,0],[0,1/3]]),na([1/3,sqrt(3)/3]),0,1/6],
    [na([[1/3,0],[0,1/3]]),na([2/3,0]),0,1/6],
    [na([[0-1/3,0],[0,0-1/3]]),na([1/2,sqrt(3)/6]),0,1/6],
    [na([[0-1/3,0],[0,0-1/3]]),na([5/6,sqrt(3)/6]),0,1/6],
    [na([[0-1/3,0],[0,0-1/3]]),na([2/3,sqrt(3)/3]),0,1/6],
]