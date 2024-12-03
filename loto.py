class Participante:
    def __init__(self, nombre, saldo, numero_apuestas, apuestas_ganadas, apuestas_perdidas, indice_acierto):
        self.nombre = nombre
        self.saldo = saldo
        self.numero_apuestas = numero_apuestas
        self.apuestas_ganadas = apuestas_ganadas
        self.apuestas_perdidas = apuestas_perdidas
        self.indice_acierto = indice_acierto
        
    def crear_porteclado(self):
        self.nombre = input("nombre: ")
        self.saldo = float(input("saldo: "))
        self.numero_apuestas = int(input("numero apuestas: "))
        self.apuestas_ganadas = int(input("apuestas ganadas: "))
        self.apuestas_perdidas = int(input("apuestas perdidas: "))
        self.indice_acierto = float(input("indice acierto: "))     
        return (self)
        
    def resumen(self):
        print(f'Los datos del usuario son:\n'
              f'Nombre: {self.nombre}\n'
              f'Saldo: {self.saldo}\n'
              f'Numero Apuestas: {self.numero_apuestas}\n'
              f'Apuestas Ganadas: {self.apuestas_ganadas}\n'
              f'Apuestas Perdidas: {self.apuestas_perdidas}\n'
              f'Indice acierto: {self.indice_acierto}')
    
    def apuesta(self):
        self.numero_apuestas =self.numero_apuestas + 1
        euros_ganados = (float(input("introduce el saldo ganado: ")))
        if euros_ganados <= 0:
            self.saldo = self.saldo + euros_ganados
            self.apuestas_ganadas = self.apuestas_perdidas + 1
        else: 
            self.saldo = round(self.saldo + euros_ganados,2)
            self.apuestas_ganadas = self.apuestas_ganadas + 1
            
        self.indice_acierto = self.apuestas_ganadas/self.numero_apuestas


class Loterias():
    def __init__(self):

        self.lista_participantes = {}
        

    def añadir_participante_teclado(self, participante):
        nombre_c = input("nombre: ")
        saldo_c = float(input("saldo: "))
        numero_apuestas_c = int(input("numero apuestas: "))
        apuestas_ganadas_c = int(input("apuestas ganadas: "))
        apuestas_perdidas_c = int(input("apuestas perdidas: "))
        indice_acierto_c = float(input("indice acierto: "))     
        participante_c = Participante(nombre_c,saldo_c,numero_apuestas_c,apuestas_ganadas_c,apuestas_perdidas_c, indice_acierto_c)
        self.lista_participantes[participante_c.nombre]= [participante_c.saldo, participante_c.numero_apuestas, 
                                                          participante_c.apuestas_ganadas, 
                                                          participante_c.apuestas_perdidas,participante_c.indice_acierto]

    def añadir_participante(self, participante):

        self.lista_participantes[participante.nombre]= [participante.saldo, participante.numero_apuestas, 
                                                        participante.apuestas_ganadas, participante.apuestas_perdidas, 
                                                        participante.indice_acierto]

    def imprimir(self):
        for i, x in self.lista_participantes.items():
            print(i, x)
    
    def buscar_nombre(self,nombre):
        if nombre in self.lista_participantes:
            return True
        else:
            return False
        
    def modificar_saldo(self,nombre, saldo):
        self.lista_participantes[nombre][0]=saldo



bwin=Loterias()
participante = Participante("pepe", 0, 0, 0, 0, 0)
participante1 = Participante("juan", 0, 0, 0, 0, 0)
participante2 = Participante("pedro", 0, 0, 4, 0, 0)
bwin.añadir_participante(participante)
bwin.añadir_participante(participante1)
bwin.añadir_participante(participante2)
escoger = 1
while escoger != 0:
    print("***************************************")
    print("* Gestion de apuestas pulsa un numero *")
    print("* 1 crea un participante por teclado  *")  
    print("* 2 modificar saldo apuestas part     *")
    print("* 3 resumen bwin                      *")    
    print("* 4 resumen bwin                      *")  
    escoger = int(input("* 0 salir bwin                        * : "))
    
    if escoger == 1:
        participante = Participante("", 0, 0, 0, 0, 0)
        bwin.añadir_participante_teclado(participante)
    elif escoger == 2:
        nombre_modificar = input("que participante quieres modificar")
        if bwin.buscar_nombre(nombre_modificar) == True:
            saldo_modificar = int(input("que participante quieres modificar"))
            bwin.modificar_saldo(nombre_modificar,saldo_modificar)
        else:
            print("El nombre no esta en la lista") 
        
    elif escoger == 3:
        bwin.imprimir()
    elif escoger == 4:
        bwin.imprimir()
    else:
        print("Adios")
        

