from modelodiscreto import *
from pid import *
import matplotlib.pyplot as plt

x = []
y = []

x.append(0)
y.append(0)

pid = PID()
pid.AjusteGanancias(0.09,0.5,0,1)
pid.AjusteLimitesError(-1000,1000)
pid.AjusteLimitesSalida(0,100)
pid.AjusteReferencia(60)
pid.ActualizaEntrada(0)
#pid.AjusteModeloIdeal(True)

fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')

for i in range(1,100):
    x.append(i)
    y.append(y_primerorden_fc(pid.Salida, 1,  10,  10, y[-1]))
    pid.ActualizaEntrada(y[-1])
    pid.Calcular()
    print(i, y[-1])
    ax.cla()   # Clave clara
    #ax.bar(y, label='test', height=y, width=0.3)
    #ax.legend()
    plt.plot(x,y)
    plt.pause(1)
    time.sleep(1)

    


#plt.plot(x,y)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Función ')
#plt.show()
