import numpy as np 
import matplotlib.pyplot as plt 
from astropy.tables import Table

""" The data table from Yang et al. (2007), provided at this address: http://gax.shao.ac.cn/data/Group.html
provides a group number and if the galaxy is central or not. It does not tell you how many galaxies are
in the group that the given galaxy is in. This code is to extract that information from the data."""

