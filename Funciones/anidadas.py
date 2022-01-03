def operacion():

    def deposito (cantidad, balance):
        return cantidad + balance
    
    def retiro (cantidad, balance):
         if cantidad <= balance:
            return balance - cantidad
 
    print(deposito(10,20))
    print(retiro(50,80))

operacion()
