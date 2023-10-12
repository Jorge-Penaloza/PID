import time
class PID:
    def __init__(self):
        self.Kp = 0 
        self.Ki = 0 
        self.Kd = 0 
        self.SampleTime = 1
        self.TiempoActual = time.time()
        self.TiempoAnterior = time.time()
        self.Referencia = 0
        self.Entrada = 0
        self.UltimaEntrada = 0
        self.Salida = 0
        self.SalidaMaxima = 0
        self.SalidaMinima = 0
        self.ErrorAcumulado = 0
        self.EacumMaximo = 0
        self.EacumMinimo = 0
        self.ModeloIdeal = False
    def Calcular(self):
        self.TiempoActual = time.time() 
        TiempoDeMuestreo = self.TiempoActual - self.TiempoAnterior
        #print("TM", TiempoDeMuestreo)
        if TiempoDeMuestreo > self.SampleTime:
            #print("entre")
            error = self.Referencia - self.Entrada
            self.ErrorAcumulado += error
            if not self.ModeloIdeal:
                #print("entr??")
                if self.ErrorAcumulado > self.EacumMaximo:
                    self.ErrorAcumulado = self.EacumMaximo
                if self.ErrorAcumulado < self.EacumMinimo:
                    self.ErrorAcumulado = self.EacumMinimo
            #DiferencialDeError = self.Entrada - self.UltimaEntrada
            DiferencialDeError = error - self.UltimaEntrada
            self.Salida = self.Kp*error 
            self.Salida += self.Ki*self.ErrorAcumulado 
            self.Salida += self.Kd*DiferencialDeError
            if not self.ModeloIdeal:
                #print(self.modelo_ideal)
                if self.Salida > self.SalidaMaxima:
                    self.Salida = self.SalidaMaxima
                elif self.Salida < self.SalidaMinima:
                    self.Salida = self.SalidaMinima
            #self.UltimaEntrada = self.Entrada
            self.UltimaEntrada = error
            self.TiempoAnterior = self.TiempoActual
    def AjusteReferencia(self, SetPoint):
        self.Referencia = SetPoint
    def AjusteGanancias( self, kp, ki, kd, SampleTime, inverso = False):
        if kp >= 0 and ki >= 0 and kd >= 0:
            self.Kp = kp
            self.Ki = ki*SampleTime
            self.Kd = kd/SampleTime
            self.SampleTime = SampleTime
            if inverso == True:
                self.Kp = -self.Kp
                self.Ki = -self.Ki
                self.Kd = -self.Kd
    def AjusteLimitesError(self, error_minimo, error_maximo):
        if error_minimo < error_maximo:
            self.EacumMinimo = error_minimo
            self.EacumMaximo = error_maximo
            if not self.ModeloIdeal:
                if self.ErrorAcumulado > self.EacumMaximo:
                    self.ErrorAcumulado = error_maximo
                elif self.ErrorAcumulado < self.EacumMinimo:
                    self.ErrorAcumulado = error_minimo
    def AjusteLimitesSalida(self, salida_minimo, salida_maximo):
        if salida_minimo < salida_maximo:
            self.SalidaMaxima = salida_maximo
            self.SalidaMinima = salida_minimo
            if not self.ModeloIdeal:
                if self.Salida > salida_maximo:
                    self.Salida = salida_maximo
                elif self.Salida < salida_minimo:
                    self.Salida = salida_minimo
    def ActualizaEntrada(self, entrada):
        self.Entrada = entrada
    def AjusteModeloIdeal(self, modelo_ideal):
        self.ModeloIdeal = modelo_ideal
        #print("self.ModeloIdeal",self.ModeloIdeal)
