# PID en Python

**Desarrollador:** Jorge Peñaloza  
**Correo de contacto:** [jorge.penaloza.guerra@gmail.com](mailto:jorge.penaloza.guerra@gmail.com)

Este repositorio ofrece una implementación de un controlador PID en Python, desarrollado íntegramente por Jorge Peñaloza. El objetivo es permitir a los usuarios aplicar control de procesos de manera sencilla sin tener que escribir todo el algoritmo desde cero.

## Archivos en el repositorio:

- `pid.py`: Contiene la implementación principal del controlador PID.
- `modelodiscreto.py`: Proporciona un modelo discreto utilizado en el ejemplo.
- `ejemplo_pid2.py`: Un ejemplo práctico de cómo usar la biblioteca PID y visualizar los resultados con `matplotlib`.

## Uso:

Para utilizar la biblioteca PID, simplemente importa las clases y funciones necesarias desde `pid.py` y `modelodiscreto.py` en tu script de Python y sigue el ejemplo proporcionado en `ejemplo_pid2.py`.

```python
from modelodiscreto import *
from pid import *
import matplotlib.pyplot as plt

# Configuración inicial
x = []
y = []
x.append(0)
y.append(0)

# Configura tu controlador PID aquí
pid = PID()
pid.AjusteGanancias(0.09,0.5,0,1)
pid.AjusteLimitesError(-1000,1000)
pid.AjusteLimitesSalida(0,100)
pid.AjusteReferencia(60)
pid.ActualizaEntrada(0)

# Visualización con matplotlib
fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')

for i in range(1,100):
    x.append(i)
    y.append(y_primerorden_fc(pid.Salida, 1,  10,  10, y[-1]))
    pid.ActualizaEntrada(y[-1])
    pid.Calcular()
    ax.cla()
    plt.plot(x,y)
    plt.pause(1)
    time.sleep(1)
