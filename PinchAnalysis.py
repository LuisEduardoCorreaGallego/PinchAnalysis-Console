#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: PinchAnalysis
Description: None
Category: Chemical Engineering
Requested Elements: File text with streams information
Author: Luis Eduardo Correa Gallego <luise.correa@udea.edu.co>, 1.10.18
Code base: johannes <info@numex-blog.com>, 10.03.18
Created on: 1/10/2018
Last modification: 2/10/2018
Used IDE: PyCharm Professional Edition
License: MIT License (http://opensource.org/licenses/MIT)
"""
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

# Load data from text file
IN_array = np.loadtxt('Data.txt', skiprows=1, unpack=False)

# Set units for temperature and heat flow
T_units = "°F"
Q_units = "BTU/h"

# Generate stream list from information on text file
streamList = {}
for i in range(0, len(IN_array)):
        streamList["Stream_{0}".format(i+1)]=list(IN_array[i])
locals().update(streamList)
IN = list(streamList.values())

# Separating data by type: heat flow,
#                          start temperature,
#                          target temperature
#                          dT_min
Data = [[IN[i][0] for i in range(len(IN))],
        [IN[i][1] for i in range(len(IN))],
        [IN[i][2] for i in range(len(IN))],
        [IN[i][3] for i in range(len(IN))]]
Q_dot = Data[0]
T_in = Data[1]
T_out = Data[2]
dT_min = Data[3]

# Get hot and cold stream index
hotStreamIndex = []
coldStreamIndex = []

for i in range(len(IN)):
    if IN[i][1] > IN[i][2]:
        hotStreamIndex.append(i)
    elif IN[i][1] < IN[i][2]:
        coldStreamIndex.append(i)

# Calculate source and sink heat flow
Q_dot_source = 0

for i in range(len(hotStreamIndex)):
    Q_dot_source = Q_dot_source + IN[hotStreamIndex[i]][0]  

Q_dot_sink = 0

for i in range(len(coldStreamIndex)):
    Q_dot_sink = Q_dot_sink + IN[coldStreamIndex[i]][0]

# Shifted temperature and heat capacity flow hot stream    
for i in range(len(hotStreamIndex)):
    deltaT = 0.5*IN[i][3]
    row = hotStreamIndex[i]
    IN[row].append(IN[row][1] - deltaT) 
    IN[row].append(IN[row][2] - deltaT)
    IN[row].append(IN[row][0]/(IN[row][5]- IN[row][4]))

# Shifted temperature and heat capacity flow cold stream
deltaT = 0

for i in range(len(coldStreamIndex)):
    deltaT = 0.5*IN[i][3]
    row = coldStreamIndex[i]
    IN[row].append(IN[row][1] + deltaT)
    IN[row].append(IN[row][2] + deltaT)
    IN[row].append(IN[row][0]/(IN[row][5]- IN[row][4]))

# Get temperatures and intervals
temperatures = []
for i in range(len(IN)):
    temperatures.append(IN[i][4])
    temperatures.append(IN[i][5])

# Get sorting index
tempInd = np.argsort(temperatures)
# Get rid of duplicates
temperatures = set(temperatures)
temperatures = list(temperatures)
# Sort temperatures
temperatures.sort(reverse=True)

# Set cascade temperatures
cascade = []
cascadeSink = []
cascadeSource = []

for i in range(len(temperatures)-1):
    cascade.append([])
    cascadeSink.append([])
    cascadeSource.append([])
    cascade[i].append(temperatures[i]) 
    cascadeSink[i].append(temperatures[i])
    cascadeSource[i].append(temperatures[i])
    cascade[i].append(temperatures[i+1]) 
    cascadeSink[i].append(temperatures[i+1])
    cascadeSource[i].append(temperatures[i+1])

#===
for i in range(len(cascade)):
    cascade[i].append(cascade[i][0] - cascade[i][1]) 
    cascadeSink[i].append(cascade[i][0] - cascade[i][1]) 
    cascadeSource[i].append(cascade[i][0] - cascade[i][1]) 
    C_source = 0
    C_sink = 0
    for j in range(len(IN)):
        if (cascade[i][0] <= IN[j][4]) and (cascade[i][1] >= IN[j][5]) and (IN[j][6] < 0):
            C_source = C_source + IN[j][6]
    for j in range(len(IN)):     
        if (cascade[i][0] > IN[j][4]) and (cascade[i][1] < IN[j][5]) and (IN[j][6] > 0):
            C_sink =C_sink + IN[j][6]
    cascade[i].append(C_source + C_sink)
    cascade[i].append(cascade[i][3] * cascade[i][2])  
    cascadeSink[i].append(C_sink)  
    cascadeSink[i].append(cascadeSink[i][3] * cascadeSink[i][2])
    cascadeSource[i].append(C_source)  
    cascadeSource[i].append(cascadeSource[i][3] * cascadeSource[i][2])

heatFlow = 0
ptCascade = []
ptCascade.append(heatFlow)

for i in range(len(cascade)):
    heatFlow = heatFlow - cascade[i][4]
    ptCascade.append(heatFlow)

# Calculate recovered and remaining heat flow
if [n for n in ptCascade if n<0]:
    Q_dot_rem = min([n for n in ptCascade if n<0])
else:
    Q_dot_rem =0
Q_dot_rec = Q_dot_sink - abs(Q_dot_rem)

heatFlow = abs(Q_dot_rem)
ptCascade = []
ptCascade.append(heatFlow)

for i in range(len(cascade)):
    heatFlow = heatFlow - cascade[i][4]
    ptCascade.append(heatFlow)

# Prepare plot for source
heatFlowSource = []
tempSource = []

heatFlowSource.append(0.) 

for i in reversed(cascadeSource):
    if i[4] < 0:
        heatFlowSource.append(heatFlowSource[-1] + i[4]*-1.) 
        tempSource.append(i[0] + deltaT)
        tempSource.append(i[1] + deltaT)

# Get rid of duplicates
tempSource = set(tempSource)
tempSource = list(tempSource)
# Sort temperatures
tempSource.sort(reverse=False)

# Prepare plot for sink
heatFlowSink = []
tempSink = []
# Generating heat flow cascade
# The last element of cascade corresponds to start of sink
heatFlowSink.append(ptCascade[-1])

for i in reversed(cascadeSink):
    if i[4] > 0:
        heatFlowSink.append(heatFlowSink[-1] + i[4]) 
        tempSink.append(i[0] - deltaT)
        tempSink.append(i[1] - deltaT)
           
# Get rid of duplicates
tempSink = set(tempSink)
tempSink = list(tempSink)
# Sort temperatures
tempSink.sort(reverse=False)

# Prepare plots
# Figure 1
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig1.canvas.set_window_title('Composite curves')
# Figure 2
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
fig2.canvas.set_window_title('Grand composite curve')
# Figure 3
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
fig3.canvas.set_window_title('Table 3')
# Figure 4
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
fig4.canvas.set_window_title('Table 1')
# Figure 5
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
fig5.canvas.set_window_title('Table 2')

# Plot cycles sink
# Axe 1
ax1.plot(heatFlowSink, tempSink,
         'b', linewidth=2)
ax1.plot(heatFlowSource, tempSource,
         'r', linewidth=2)
ax1.axvline(x=min(heatFlowSource), color='k', linestyle='--', linewidth=0.8)
ax1.axvline(x=min(heatFlowSink), color='k', linestyle='--', linewidth=0.8)
ax1.axvline(x=max(heatFlowSource), color='k', linestyle='--', linewidth=0.8)
ax1.axvline(x=max(heatFlowSink), color='k', linestyle='--', linewidth=0.8)
ax1.text(1.05*min(heatFlowSource), max(tempSource),
         'Hot composite curve', color='red', fontsize=9)
ax1.text(1.05*min(heatFlowSink), min(tempSink),
         'Cold composite curve', color='blue', fontsize=9)
ax1.minorticks_on()
ax1.grid(which='BOTH', ls=':')
ax1.grid(True)
ax1.set_xlabel('Heat flow ('+Q_units+')')
ax1.set_ylabel('Temperature ('+T_units+')')
# Save the figure
fig1.savefig('Pinch_CompositeCurve.png')

# Axe 2
ax2.plot(ptCascade, temperatures,
         'r', linewidth=1.2, label="_nolegend_")
ax2.set_xlim([min(ptCascade), None])
ax2.axvline(x=min(ptCascade), color='k',
            linestyle='-', linewidth=2)
for k in range(len(temperatures)):
    x_1 = min(ptCascade); x_2 = ptCascade[k]
    y_1 = temperatures[k]; y_2 = y_1
    x = [x_1, x_2]
    y = [y_1, y_2]
    ax2.plot(x, y,
             linestyle='--',
             color='k',
             linewidth=0.7,
             label="_nolegend_")
    ax2.text(x_2, y_2,
             str(ptCascade[k]),
             verticalalignment='bottom',
             horizontalalignment='left',
             fontsize=7,
             fontweight='bold',
             label="_nolegend_",
             wrap=True, rotation=39)
    if ptCascade[k] == 0:
        ax2.axhline(y=temperatures[k],
                    linestyle='--',
                    color='blue',
                    linewidth=0.9,
                    label="$T_{pinch} \ =$"+str(temperatures[k])+' '+T_units)
        ax2.legend(loc="best")
    else:
        pass

ax2.minorticks_on()
ax2.grid(which='BOTH',ls=':')
ax2.grid(True)
ax2.set_xlabel('Heat flow ('+Q_units+')')
ax2.set_ylabel('Temperature ('+T_units+')')
# Save the figure
fig2.savefig('Pinch_GrandCompositeCurve.png')

# Axe 4
ax4.axes.get_xaxis().set_visible(False)
ax4.axes.get_yaxis().set_visible(False)
colLabels = ('$T_{in} \ ($'+T_units+')',
             '$T_{out} \ ($'+T_units+')',
             '$Q \ ($'+Q_units+')')
cellText_2 = []
for k in range(len(T_in)):
    cellText_2.append([T_in[k], T_out[k], Q_dot[k]])

table_4 = ax4.table(cellText=cellText_2,
                    colLabels=colLabels,
                    colLoc='center', rowLoc='left',
                    loc='center', cellLoc='left')

conditionals_2 = [(j, k) == (0, 0),
                  (j, k) == (0, 1),
                  (j, k) == (0, 2)]
for j in range(0, len(T_in)+1):
    for k in range(0, 3):
        if any(conditionals_2):
            table_4._cells[(j, k)].set_facecolor("lightgray")
        else:
            pass

fig4.patch.set_visible(False)
ax4.axis('off')
fig4.savefig('Pinch_StreamData.png')

# Axe 5
ax5.axes.get_xaxis().set_visible(False)
ax5.axes.get_yaxis().set_visible(False)
colLabels = ('$T_{in} \ ($'+T_units+')',
             '$T_{out} \ ($'+T_units+')',
             '$T_{in, \ shifted} \ ($'+T_units+')',
             '$T_{out, \ shifted} \ ($'+T_units+')')
cellText_3 = []
for k in range(len(T_in)):
    cellText_3.append([T_in[k], T_out[k], IN[k][4], IN[k][5]])

table_5 = ax5.table(cellText=cellText_3,
                    colLabels=colLabels,
                    colLoc='center', rowLoc='left',
                    loc='center', cellLoc='left')

conditionals_5 = [(j, k) == (0, 0),
                  (j, k) == (0, 1),
                  (j, k) == (0, 2),
                  (j, k) == (0, 3),
                  (j, k) == (0, 4)]
for j in range(0, len(T_in)+1):
    for k in range(0, 4):
        if any(conditionals_5):
            table_5._cells[(j, k)].set_facecolor("lightgray")
        else:
            pass

fig5.patch.set_visible(False)
ax5.axis('off')
fig5.savefig('Pinch_ShiftedTemperatures.png')

# Axe 3
ax3.axes.get_xaxis().set_visible(False)
ax3.axes.get_yaxis().set_visible(False)
colLabels = ('Temperature ('+T_units+')',
             'Heat flow ('+Q_units+')')
cellText = []
for k in range(len(temperatures)):
    cellText.append([temperatures[k], ptCascade[k]])

table_3 = ax3.table(cellText=cellText,
                    colLabels=colLabels,
                    colLoc='center', rowLoc='left',
                    loc='center', cellLoc='left')

conditionals_3 = [(j, k) == (0, 0),
                  (j, k) == (0, 1)]
for j in range(0, len(temperatures)+1):
    for k in range(0, 2):
        if any(conditionals_3):
            table_3._cells[(j, k)].set_facecolor("lightgray")
        else:
            pass

fig3.patch.set_visible(False)
ax3.axis('off')
fig3.savefig('Pinch_HeatCascade.png')

plt.tight_layout()
plt.show()
