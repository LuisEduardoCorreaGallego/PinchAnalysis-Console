# PinchAnalysis
This application allows calculate heat integration for heat exchangers.

## Usage
To use this application, it is necessary to attach a plain text file document with the information of each stream to analyze. The required information is the heat required in the stream, the inlet or start temperature, the exit or target temperature and the minimum approach. In the same way, the units of temperature and heat flow must be specified.

## Required information
The plain text file must have the following format and the same order:

* <a href="https://www.codecogs.com/eqnedit.php?latex=\dot{Q}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dot{Q}" title="\dot{Q}" /></a>
* <a href="https://www.codecogs.com/eqnedit.php?latex=T_{min}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{in}" title="T_{in}" /></a>
* <a href="https://www.codecogs.com/eqnedit.php?latex=T_{min}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out}" title="T_{out}" /></a>
* <a href="https://www.codecogs.com/eqnedit.php?latex={\Delta&space;T}_{min}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\Delta&space;T}_{min}" title="{\Delta T}_{min}" /></a>

### Calculation example
We have six streams with the following specifications:

Stream | Condition | T_in (°C) | T_out (°C) | Q_avalaible (kW)
------------ | ------------- | ------------- | ------------- | -------------
1 | Hot | 300 | 150 | 1200

