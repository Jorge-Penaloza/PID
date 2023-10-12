# Calculo secuencial de sistema de primer orden discreto
#       dy(t)
#   A1* ----   + A0*y(t) = x(t)
#        dt
def y_primerorden(x_t, dt, a1, a0, y_anterior ):
    return (dt*x_t + a1*y_anterior)/(a1 + a0*dt)

# Calculo secuencial de sistema de primer orden discreto forma control
#        dy(t)
#   Tau* ----   + y(t) = k*x(t)
#         dt
def y_primerorden_fc(x_t, dt, tau, k, y_anterior ):
    return (k*x_t + (tau/dt)*y_anterior)/(tau/dt + 1)