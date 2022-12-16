import os  # Importo "os" para ir limpiando la pantalla

# Lista de clientes por defecto
clientes = [
    [0, 'Mario', 'Lopez', '12345678A', 19, 'Español', 616554477, 'mario.lopezl@campuspf.es', 1000],
    [1, 'Vladis', 'Slavev', '12345678B', 18, 'Bulgaro', 616455477, 'vladis.algo@campuspf.es', 2000],
    [2, 'Pablo', 'Vara', '12345678C', 19, 'Japones', 616545477, 'pablo.vara@campuspf.es', 3000],
    [3, 'Fernando', 'Dorado', '12345678D', 19, 'Español', 616554477, 'fernando.dorado@campuspf.es', 4000]
]


class Cliente:  # Generación de la clase Cliente

    def __init__(self, nombre, apellido, dni, edad, nacionalidad, telefono, email, monedero):  # Constructor
        #  Construimos toda la sucesion de valores que vamos a usar en la clase
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.telefono = telefono
        self.email = email
        self.monedero = monedero

    def crearCliente(self):  # Función para crear cliente
        id = int(clientes[-1][0]) + 1  # con esto sacamo el último id para que no haya duplicados de id

        x = [id, self.nombre, self.apellido, self.dni, self.edad, self.nacionalidad, self.telefono,
             self.email, self.monedero]  # Sentencia que ordena los valores para meterlos en una lista
        clientes.append(x)  # Método que los va agregando a la lista.
        # Con esto podemos ir añadiendo usuarios mientras está ejecutándose


class Clientes:  # Generación de la clase Clientes
    def __init__(self):  # Constructor
        self.clientes = clientes  # construimos la lista como self para usarla
        for i in self.clientes:  # bucle for va por la lista uno a uno guardándolos en "i"
            print(i)  # Va imprimiendo los valores por pantalla uno a uno

    @staticmethod  # Creamos el método estatico para que no necesite los argumentos del constructor
    def getClientes():  # definimos el nombre de la funcion sin parametros
        return clientes  # devolvemos la lista para usarla en otro documento

    @staticmethod  # Creamos el método estatico para que no necesite los argumentos del constructor
    def logIn():  # definimos el nombre de la funcion sin parametros
        for i in clientes:  # bucle for para que nos muestre solo el id y nombre
            print(f"{i[0]} {i[1]}")  # print de los valores de la lista con las posiciones de id y nombre
        while True:  # bucle while para hacerlo a prueba de fallos
            try:  # try intenta realizar el fragmento de codigo para que no se pare la aplicacion si da error

                # variable para guardar la opcion
                x = input('\nElije un cliente con el que iniciar sesion por "id": ')

                # condicion para evitar que se pueda elejir un cliente inexistente
                if int(x) > int(clientes[-1][0]):
                    print('\nEl cliente que has introducido no existe, prueba de nuevo')  # print de error
                else:  # si la condicion de arriba no se cumple pasamos al else
                    os.system('cls')
                    # variable para guardar el nombre del usuario
                    user = clientes[int(x)][1]
                    print(f'\nHas iniciado sesion como: {user}')  # comunicamos con un print el usuario en uso
                    return user  # devolvemos user al documento principal

            except ValueError:  # si el try da error por cualquier motivo nos saltaría el mensaje de abajo
                print('\nSolo admitimos números sin decimales, porfavor introduzca algo valido')
