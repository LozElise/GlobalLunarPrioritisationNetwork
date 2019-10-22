import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#choose mineral rank and water rank
mineralrank = 1
waterrank = 2

#load data
Terrainfile = 'Terrain.xlsx'
Waterfile = 'Water.xlsx'
Ironfile = 'Iron.xlsx'

Terrain_data = pd.read_excel(Terrainfile)
Water_data = pd.read_excel(Waterfile)
Iron_data = pd.read_excel(Ironfile)

Terrain_data = np.array(Terrain_data)
Water_data = np.array(Water_data)
Iron_data = np.array(Iron_data)


#look at the mineral data - where is the ones above 100
Mineralthres = 10
N = len(Iron_data)
for i in range(N):
    for j in range(N+1):
        if Iron_data[i,j] < Mineralthres:
            Iron_data[i,j] = 0.0
            
#what is limit of the rover - inclination
Terrainthres = 125
N = len(Terrain_data)
Terrain_data2 = Terrain_data
for i in range(N):
    for j in range(N+1):
        if Terrain_data[i,j] < Terrainthres and Terrain_data[i,j] >  142:
            Terrain_data2[i,j] = 0.0

                        
#what is limit of the rover - inclination
Waterthres = 80
N = len(Water_data)
for i in range(N):
    for j in range(N+1):
        if Water_data[i,j] > Waterthres:
            Water_data[i,j] = 0.0

#overlap

X = np.arange(0, len(Terrain_data))
Y = np.arange(0, len(Terrain_data)+1)
gridx, gridy = np.mgrid[0:len(Terrain_data), 0:len(Terrain_data)+1]
"""

plt.pcolormesh(gridx,gridy,Terrain_data2,cmap='YlOrBr')
plt.pcolormesh(gridx,gridy,Iron_data,cmap='Greens')

plt.colorbar()
plt.axis('equal')
plt.show()

gridx, gridy = np.mgrid[0:len(Terrain_data), 0:len(Terrain_data)+1]
plt.figure()
plt.contour(gridy, gridx, Terrain_data2, cmap='YlOrBr')
plt.ylabel('Position Unit')
plt.xlabel('Position Unit')
plt.title('Acceptable Terrain Data')
plt.grid()
plt.legend()
plt.axis('equal')
"""

plt.figure()
plt.pcolormesh(gridy, gridx, Water_data, cmap='Blues')
plt.pcolormesh(gridy, gridx, Iron_data, cmap='Greys', alpha=0.3)
plt.contour(gridy, gridx, Terrain_data2, cmap='YlOrBr')

plt.ylabel('Position Unit')
plt.xlabel('Position Unit')
plt.title('Terrain Mapping with Water')
plt.grid()
plt.show()

