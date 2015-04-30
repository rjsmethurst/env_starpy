import numpy as np 
import matplotlib.pyplot as plt 
from astropy.tables import Table

""" The data table from Yang et al. (2007), ApJ, 671, 153, provided at this address: http://gax.shao.ac.cn/data/Group.html
provides a group number and if the galaxy is central or not. It does not tell you how many galaxies are
in the group that the given galaxy is in. This code is to extract that information from the data."""

group_data = g = Table.read('galaxy_groups.txt')

N = N.zeros(len(g))

for n in range(len(g)):
	N[j] = len(np.where(g['group id'] == g['group id'][j])[0])

nn = Column(N, name='N galaxy in group')
g.add_column(nn, index=5)

print g