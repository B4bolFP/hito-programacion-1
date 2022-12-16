productos = [  # Lista de productos
    [0, 'Tomate', 'Hortaliza', 4],
    [1, 'Berengena', 'Hortaliza', 2],
    [2, 'Pan', 'Horneados', 1],
    [3, 'Hilo', 'Costura', 11]
]


class Producto:  # iniciamos la clase Producto
    def __init__(self, nombre, tipo, precio):  # constructor
        self.nombre = nombre  # elemento a construir
        self.tipo = tipo  # elemento a construir
        self.precio = precio  # elemento a construir

    def crearProducto(self):  # definimos crearProducto
        id = int(productos[-1][0]) + 1  # Sacamos el último id de la lista productos para que no haya duplicados
        x = [id, self.nombre, self.tipo, self.precio]  # construimos la entrada de la lista
        productos.append(x)  # añadimos la entrada a la lista


class Productos:  # iniciamos la clase Productos
    def __init__(self):  # constructo
        for i in productos:  # bucle para sacar la tabla linea a linea
            print(i)  # la linea

    @staticmethod  # Creamos el método estatico para que no necesite los argumentos del constructor
    def getProductos():  # definimos getProductos
        return productos  # devolvemos la tabla productos para usar en otro documento
