 #PinchAnalysis
Esta herramienta permite realizar cálculos correspondientes al análisis pinch,
en el cual se busca efectuar integración energética a corrientes en un proceso
químico.

##Instalación
Para instalar esta aplicación, se pueden llevar a cabo algunas de las siguientes
opciones:

- ###Instalación vía PIP
  Esta aplicación cuenta con distribución disponible en PIP a través de la
  siguiente estructura:
  
  pip install PinchAnalysis
  
- ###Instalación vía clonación de repositorio
  El repositorio respectivo en github le permitirá clonar el contenido de esta
  aplicación.
  
##Opciones de cálculo y visualización
Esta herramienta en sí misma utiliza la clase *pinchStream* para poder efectuar
los cálculos. Es necesario crear la instancia de la clase para el archivo de
texto plano que alberga las información requerida para las corrientes. El nombre
del archivo puede corresponder a cualquiera, recomendándose utilizar nombres
cortos.

###Métodos disponibles para el análisis de corrientes
La clase pinchStream tiene los siguientes métodos integrados:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', 'cascadeTable', 'compositeCurve',
'drawCascade', 'drawIntervals', 'drawStreams', 'grandCompositeCurve',
'initialGridDiagram', 'shiftedTemperatures', 'streamData']

###cascadeTable
Este método permite visualizar la tabla correspondiente a la cascade de flujo de
calor para las corrientes analizadas.
