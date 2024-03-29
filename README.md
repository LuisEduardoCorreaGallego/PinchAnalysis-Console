# PinchAnalysis - Heat Integration Analysis [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/LuisEduardoCorreaG )
This application allows calculate heat integration for heat exchangers.

## Installation
For installing this application [download the most recent wheel file](https://github.com/LuisEduardoCorreaGallego/PinchAnalysis/tree/master/PinchAnalysis%200.5/PinchAnalysis%200.5/dist) and use:

**```pip install PinchAnalysis-VERSION-py3-none-any.whl```**

## Usage
This application uses the pinchStream class, which requires attaching a plain text file to the folder where the application is hosted. This class allows to visualize the specifications of the streams and the table of shifted temperatures as well as to generate the composite curve, the grand composite curve and the corresponding heat flow cascade.

## Required information
The plain text file must have the following information:

* <a href="https://www.codecogs.com/eqnedit.php?latex=\dot{Q}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dot{Q}" title="\dot{Q}" /></a>
* <a href="https://www.codecogs.com/eqnedit.php?latex=T_{min}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}" title="T_{in}" /></a> or <a href="https://www.codecogs.com/eqnedit.php?latex=T_{start}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{start}" title="T_{start}" /></a>
* <a href="https://www.codecogs.com/eqnedit.php?latex=T_{min}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}" title="T_{out}" /></a> or <a href="https://www.codecogs.com/eqnedit.php?latex=T_{target}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{target}" title="T_{target}" /></a>
* <a href="https://www.codecogs.com/eqnedit.php?latex={\Delta&space;T}_{min}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\Delta&space;T}_{min}" title="{\Delta T}_{min}" /></a>

The corresponding plain text file will be in the next way:

**```Q_dot T_start T_target dT_min```**

## How to manipulate the application?

First, the instance of the class is generated using the pinchStream notation ('Data'):

```python
pinchStream('Data')
```

It should be noted that the string 'Data' corresponds to the name of the plain text file. If you want to work on multiple plain text files that contain streams information, their names must vary only numerically, that is, if there is a second file on which you want to perform calculations, it should be called 'Data2' and so on consecutively.

The available options for the pinchStream class are the following:

```python
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cascadeTable', 'compositeCurve', 'drawCascade', 'grandCompositeCurve', 'shiftedTemperatures', 'streamData']
```

The following are the basic formats to perform the respective calculations:

```python
pinchStream('Data') # Create the instance for Data.txt file
pinchStream('Data').streamData() # Show the information of the streams for Data.txt
pinchStream('Data').shiftedTemperatures() # Show the shifted temperature table for Data.txt
pinchStream('Data').compositeCurve() # Show the composite curve for Data.txt
pinchStream('Data').grandCompositeCurve() # Show the grand composite curve for Data.txt
pinchStream('Data').drawCascade() # Draw the heat flow cascade for Data.txt
pinchStream('Data2') # Create the instance for Data2.txt file
```

### Calculations


The elements generated for each method of the pinchStream class are detailed below.

Method | Functionality | Arguments
------------ | ------------- | -------------
```streamData``` | It displays a table with the information for streams | Default: T_units='°C', Q_units='kW'
```drawStreams``` | Draw the corresponding streams| Default: Data='1', T_units='°C', Q_units='kW'
```shiftedTemperatures``` | Draw the shifted temperatures| Default: T_units='°C', Q_units='kW'
```initialGridDiagram``` | Draw the initial grid diagram (development)| Default: Data='1', T_units='°C', Q_units='kW'
```drawIntervals``` | Draw the intervals of temperature| Default: Data='1', T_units='°C', Q_units='kW'
```cascadeTable``` | Display the energy cascade | Default: Data='1', T_units='°C', Q_units='kW'
```compositeCurve``` | Draw the composite curve| Default: Data='1', T_units='°C', Q_units='kW'
```grandCompositeCurve``` | Draw the grand composite curve| Default: Data='1', T_units='°C', Q_units='kW'
```drawCascade``` | Draw the energy cascade| Default: Data='1', T_units='°C', Q_units='kW'

### Calculation examples

**First example**

**Example 15.2 (Data.txt)** _[Adapted from Analysis, Synthesis and Design of Chemical Processes, Richard Turton, Richard C. Baille, Wallace B. Whiting, Joseph A. Shaeiwitz, page 525]_
In a process, there are a total of six streams that require heating and cooling. These are listed below along with their thermal and flow data. A stream is referred to as "hot" if it requires cooling, and "cold" if it requires heating. The temperature of the stream is not used to define whether it is "hot" or "cold".

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Hot | 300 | 150 | 1200 |
2 | Hot | 150 | 50 | 200 |
3 | Hot | 200 | 50 | 450 |
4 | Cold | 190 | 290 | -500 |
5 | Cold | 90 | 190 | -800 |
6 | Cold | 40 | 190 | -600 |

Generate the tables corresponding to the specifications of the streams, the temperatures of interval and the cascade of heat flow as well as the graphs of cumulative enthalpies and grand composite.

#### Specifications for streams
Create the plain text file with the requires information. Specifications are displayed as a table.

![StreamData](specifications1.png)

#### Shifted temperatures
Calculate the temperatures corrected by the minimum approach. The shifted temperatures are displayed as a table.

![StreamData](shiftedTemperatures1.png)

#### Diagram for streams
Draw the streams with corresponding information

![StreamData](1_drawStreams.jpg)

#### Initial grid diagram
Draw the initial grid diagram

![StreamData](1_initialGridDiagram.jpg)

#### Intervals of temperature
Draw the intervals for shifted temperatures

![StreamData](1_drawIntervals.jpg)

#### Heat flow cascade
Calculate the corresponding heat flow cascade

![StreamData](cascadeTable1.png)

#### Cumulative enthalpies
Elaborate the graph of cumulative enthalpies

![StreamData](compositeCurve1.jpg)

#### Grand composite curve
Elaborate the grand composite graphic

![StreamData](Pinch_GrandCompositeCurve.jpg)

**Second example**

**Table 1.1 (Data2.txt)** _[Adapted from Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy, Ian C. Kemp, page 4]_

Given the following data:

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Cold | 20 | 135 | 230 |
2 | Hot | 170 | 60 | 330 |
3 | Cold | 80 | 140 | 240 |
4 | Hot | 150 | 30 | 180 |

Generate the tables corresponding to the specifications of the streams, the temperatures of interval and the cascade of heat flow as well as the graphs of cumulative enthalpies and grand composite.

#### Specifications for streams
Create the plain text file with the requires information. Specifications are displayed as a table.

![StreamData](specifications2.PNG)

#### Shifted temperatures
Calculate the temperatures corrected by the minimum approach. The shifted temperatures are displayed as a table.

![StreamData](shiftedTemperatures2.PNG)

#### Diagram for streams
Draw the streams with corresponding information

![StreamData](2_drawStreams.jpg)

#### Initial grid diagram
Draw the initial grid diagram

![StreamData](2_initialGridDiagram.jpg)

#### Intervals of temperature
Draw the intervals for shifted temperatures

![StreamData](2_drawIntervals.jpg)

#### Heat flow cascade
Calculate the corresponding heat flow cascade

![StreamData](cascadeTable2.PNG)

#### Cumulative enthalpies
Elaborate the graph of cumulative enthalpies

![StreamData](2_CompositeCurve.jpg)

#### Grand composite curve
Elaborate the grand composite graphic

![StreamData](2_grandCompositeCurve.jpg)

**Third example**

**Exercise 3.6 (Data3.txt)** _[Adapted from PINCH ANALYSIS FOR ENERGY AND CARBON FOOTPRINT REDUCTION: User Guide to Process Integration for the Efficient Use of Energy, Ian C. Kemp, Jeng Shiun Lim, third edition, page 60]_
Calculate the hot and cold composite curves, problem table, grand composite curve, hot and cold utility targets and pinch temperature for the problem with stream data given in the table below at a global <img src="https://render.githubusercontent.com/render/math?math=\Delta T_{min}"> of 10 °C, using a calculator, your own spreadsheet or the spreadsheet supplied with the book.

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Hot | 200 | 50 | 450 |
2 | Hot | 240 | 100 | 210 |
3 | Hot | 120 | 119 | 300 |
4 | Cold | 30 | 200 | 680 |
5 | Cold | 50 | 250 | 400 |


#### Specifications for streams
Create the plain text file with the requires information. Specifications are displayed as a table.

![StreamData](specifications3.PNG)

#### Shifted temperatures
Calculate the temperatures corrected by the minimum approach. The shifted temperatures are displayed as a table.

![StreamData](shiftedTemperatures3.PNG)

#### Diagram for streams
Draw the streams with corresponding information

![StreamData](3_drawStreams.jpg)

#### Initial grid diagram
Draw the initial grid diagram

![StreamData](3_initialGridDiagram.jpg)

#### Intervals of temperature
Draw the intervals for shifted temperatures

![StreamData](3_drawIntervals.jpg)

#### Heat flow cascade
Calculate the corresponding heat flow cascade

![StreamData](cascadeTable3.PNG)

#### Cumulative enthalpies
Elaborate the graph of cumulative enthalpies

![StreamData](3_CompositeCurve.jpg)

#### Grand composite curve
Elaborate the grand composite graphic

![StreamData](3_grandCompositeCurve.jpg)

**Fourth example**

**6.6 Worked Case Study and Example for Total Site Problem Algorith (DataA.txt and DataB.txt)** _[Adapted from PINCH ANALYSIS FOR ENERGY AND CARBON FOOTPRINT REDUCTION: User Guide to Process Integration for the Efficient Use of Energy, Ian C. Kemp, Jeng Shiun Lim, third edition, page 249]_
Consider a total site case with two plants, i.e., Plant A and Plant B. The process stream data for the two plants are given in tables below. For Plant A, use <img src="https://render.githubusercontent.com/render/math?math=\Delta T_{min}"> of 10 °C and for Plant B use <img src="https://render.githubusercontent.com/render/math?math=\Delta T_{min}"> of 20 °C.

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Hot A1H | 210 | 110 | 2500 |
2 | Hot A2H | 160 | 60 | 4000 |
3 | Cold A1C | 60 | 120 | 6000 |
4 | Cold A2C | 50 | 200 | 4500 |

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Hot B1H | 220 | 60 | 400 |
2 | Hot B2H | 250 | 100 | 300 |
3 | Hot B3H | 170 | 105 | 1300 |
4 | Cold B1C | 40 | 180 | 700 |
5 | Cold B2C | 60 | 260 | 500 |


#### Problem Tables

![StreamData](cascadeTable4A.PNG)
![StreamData](cascadeTable4B.PNG)

#### Grand Composite Curves

![StreamData](4A_grandCompositeCurve.jpg)
![StreamData](4B_grandCompositeCurve.jpg)

**Fifth example**

**Table 3.2 (Data5.txt)** _[Adapted from CHEMICAL ENGINERING DESIGN: Principles, Practice and Economics of Plant and Process Design, GAVIN TOWLER, RAY SINNOTT, page 125]_

Given the following data:

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Hot | 180 | 60 | 360 |
2 | Hot | 150 | 30 | 120 |
3 | Cold | 20 | 135 | 230 |
4 | Cold | 80 | 140 | 270 |

Generate the tables corresponding to the specifications of the streams, the temperatures of interval and the cascade of heat flow as well as the graphs of cumulative enthalpies and grand composite.

#### Specifications for streams
Create the plain text file with the requires information. Specifications are displayed as a table.

![StreamData](specifications5.PNG)

#### Shifted temperatures
Calculate the temperatures corrected by the minimum approach. The shifted temperatures are displayed as a table.

![StreamData](shiftedTemperatures5.PNG)

#### Diagram for streams
Draw the streams with corresponding information

![StreamData](5_drawStreams.jpg)

#### Initial grid diagram
Draw the initial grid diagram

![StreamData](5_initialGridDiagram.jpg)

#### Intervals of temperature
Draw the intervals for shifted temperatures

![StreamData](5_drawIntervals.jpg)

#### Heat flow cascade
Calculate the corresponding heat flow cascade

![StreamData](cascadeTable5.PNG)

#### Cumulative enthalpies
Elaborate the graph of cumulative enthalpies

![StreamData](5_CompositeCurve.jpg)

#### Grand composite curve
Elaborate the grand composite graphic

![StreamData](5_grandCompositeCurve.jpg)

**Sixth example**

**Ejemplo 9.1 (Data6.txt)** _[Adapted from DISEÑO DE PROCESOS EN INGENIERÍA QUÍMICA, Arturo Jiménez Gutiérrez, Editorial Reverté, S.A., page 205]_

Se quieren usar dos corrientes calientes y una corriente fría para diseñar una red de intercambiadores de calor. La siguiente tabla proporciona los datos del problema.

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | H1 | 200 | 80 | 240 |
2 | H2 | 180 | 30 | 1050 |
3 | C1 | 70 | 170 | 1000 |

Considerando un valor de <img src="https://render.githubusercontent.com/render/math?math=\Delta T_{min}"> de 10 °C, use el método del punto de pliegue para integrar la máxima cantidad de calor entre las corrientes.

#### Specifications for streams
Create the plain text file with the requires information. Specifications are displayed as a table.

![StreamData](specifications6.PNG)

#### Shifted temperatures
Calculate the temperatures corrected by the minimum approach. The shifted temperatures are displayed as a table.

![StreamData](shiftedTemperatures6.PNG)

#### Diagram for streams
Draw the streams with corresponding information

![StreamData](6_drawStreams.jpg)

#### Initial grid diagram
Draw the initial grid diagram

![StreamData](6_initialGridDiagram.jpg)

#### Intervals of temperature
Draw the intervals for shifted temperatures

![StreamData](6_drawIntervals.jpg)

#### Heat flow cascade
Calculate the corresponding heat flow cascade

![StreamData](cascadeTable6.PNG)

#### Cumulative enthalpies
Elaborate the graph of cumulative enthalpies

![StreamData](6_CompositeCurve.jpg)

#### Grand composite curve
Elaborate the grand composite graphic

![StreamData](6_grandCompositeCurve.jpg)

**Seventh example**

**2. Problem Statement (Data7.txt)** _[Adapted from Introduction to Pinch Technology, Rokni Masoud, Tehcnical University of Denmark, page 3]_

A typical industrial process may consist of several numbers of hot and cold process streams which may demand cooling and heating respectively. Heat exchangers can be used to recover some of the heat demand while external heaters and coolers can be used to achieve the temperature demand for the process strams. Suppose an industrial plant with hot and cold process strams as shown in the following table.

Stream | Condition | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{in}&space;\&space;(^{}\circ&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}&space;\&space;(^{}\circ&space;C)" title="T_{in} \ (^{}\circ C)" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out}&space;\&space;(^{\circ}&space;C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}&space;\&space;(^{\circ}&space;C)" title="T_{out} \ (^{\circ} C)" /></a>| <a href="https://www.codecogs.com/eqnedit.php?latex={\dot{Q}}_{available}&space;\&space;(kW)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\dot{Q}}_{available}&space;\&space;(kW)" title="{\dot{Q}}_{available} \ (kW)" /></a>
------------ | ------------- | ------------- | ------------- | ------------- |
1 | Cold | 90 | 420 | 3300 |
2 | Cold | 170 | 350 | 5760 |
3 | Cold | 200 | 390 | 5510 |
4 | Hot | 440 | 140 | 8100 |
4 | Hot | 510 | 300 | 5040 |

Generate the tables corresponding to the specifications of the streams, the temperatures of interval and the cascade of heat flow as well as the graphs of cumulative enthalpies and grand composite.

#### Specifications for streams
Create the plain text file with the requires information. Specifications are displayed as a table.

![StreamData](specifications7.PNG)

#### Shifted temperatures
Calculate the temperatures corrected by the minimum approach. The shifted temperatures are displayed as a table.

![StreamData](shiftedTemperatures7.PNG)

#### Diagram for streams
Draw the streams with corresponding information

![StreamData](7_drawStreams.jpg)

#### Initial grid diagram
Draw the initial grid diagram

![StreamData](7_initialGridDiagram.jpg)

#### Intervals of temperature
Draw the intervals for shifted temperatures

![StreamData](7_drawIntervals.jpg)

#### Heat flow cascade
Calculate the corresponding heat flow cascade

![StreamData](cascadeTable7.PNG)

#### Cumulative enthalpies
Elaborate the graph of cumulative enthalpies

![StreamData](7_CompositeCurve.jpg)

#### Grand composite curve
Elaborate the grand composite graphic

![StreamData](7_grandCompositeCurve.jpg)

## Donation 
If this project has helped you reduce your study or research time, please support me to keep improving even more :)
