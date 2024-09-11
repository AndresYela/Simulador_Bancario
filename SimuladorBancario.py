__author__ = "Cristian Andres Yela Parra"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "cristian.yela@campusucc.edu.co"

'''----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------'''
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __cedula=''
    __nombre=''
    
    __cuentaCorriente = CuentaCorriente()
    __cuentaAhorros = CuentaAhorros()
    __cdt = CDT()
    
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    __method__='ConsignarCuentaCorriente'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo consignar un monto a la cuenta corriente'
    def ConsignarCuentaCorriente(self, monto):
        # Aqui inicia el metodo
        # self.__cuentaCorriente.saldo = self.__cuentaCorriente.saldo+monto
        self.__cuentaCorriente.ConsignarValor(monto)
        
    __method__='CalcularSaldoTotal'
    __params__='Ninguno'
    __returns__='Saldo Total'
    __descriptions__='Este metodo sumo el saldo de todas las cuentas'
    def CalcularSaldoTotal(self):
        # Aqui inicia el metodo
        total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__= 'Ahorrar'
    __params__='Nada'
    __returns__='Nada'
    __descriptions__='Este metodo transfiere el dinero de corriente a ahorros'

    def Ahorrar(self, monto):
        saldoTemporal = self.__cuentaCorriente.DarSaldo()
        self.__cuentaCorriente.RetirarValor(saldoTemporal)
        self.__cuentaAhorros.ConsignarValor(saldoTemporal)
    
    __method__= 'RetirarAhorro'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo permite retirar valor de la cuenta ahorros'

    def RetirarAhorro(self, monto):
        return self.__cuentaAhorros.RetirarAhorro()
    
    __method__='DarSaldocorriente'
    __params__='Nada'
    __returns__='Saldocorriente'
    __descriptions__='Este metodo permite retornar el saldo de la cuenta corriente'

    def DarsaldoCorriente(self):
        return self.__cuentaCorriente
    
    __method__= 'RetirarTodo'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo permite retirar todo el saldo de las cuentas corriente y ahorros'

    def RetirarTodo(self):
        SaldoTemporal = self.__cuentaCorriente.DarSaldo()
        self.__cuentaCorriente.RetirarValor(SaldoTemporal)
        self.__cuentaAhorros.RetirarValor.DarSaldo()
        self.__cuentaAhorros.RetirarValor(CuentaAhorros)

    __method__='DuplicarAhorro'
    __params__='duplicar'
    __returns__='Nada'
    __descriptions__='Este metodo permite duplicar el saldo de la cuenta ahorros'

    def DuplicarAhorro(self):
        return self.__cuentaAhorros.__saldo = self.__cuentaAhorros.saldo*2


    

    


    