def operacion(cantidad, balance, tipo='Deposito'):

    def deposito (cantidad, balance):
        return cantidad + balance
    
    def retiro (cantidad, balance):
         if cantidad <= balance:
            return balance - cantidad

 
    if tipo == "Deposito":
        return deposito(cantidad,balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)

resultado = operacion(10,30,'retiro')
print(resultado)

operacion()
