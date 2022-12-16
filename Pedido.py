# imports de las clases que se traen listas de otros documentos
from Productos import Productos
from Cliente import Clientes
# importo random para generar numeros aleatorios (referencia)
import random

pedidos = [  # lista de pedidos
    [0, 'Mario', 'Tomate', 10436231, 4],
    [1, 'Jose', 'Tomate', 10457502, 4],
    [2, 'Pepe', 'Tomate', 10023463, 4],
    [3, 'Mario', 'hilo', 12023404, 11]
]


class Pedido:  # creacion clase Pedido
    def __init__(self, id_producto):  # constructor
        self.id_producto = id_producto  # valor a construir

    def crearPedido(self, usuario, ):  # definimos crear Pedido con el parametro usuario
        id = int(pedidos[-1][0]) + 1  # aquí sacamos el último id para que no haya duplicados
        y = Productos.getProductos()  # Guardo la lista Productos en la variable "y" para después
        producto = y[self.id_producto][1]  # guardo en producto la segunda posición de productos en la fila del ID
        total = y[self.id_producto][3]  # aquí en total el precio del producto relacionado con él, id
        while True:  # blucle while para que pueda ir probando
            # en referencia guardo un número aleatoria para ponérsela a los pedidos
            referencia = random.randrange(1000000, 9999999)
            try:  # try intenta realizar el fragmento de codigo para que no se pare la aplicacion si da error
                x = [id, usuario, producto, referencia, total]  # Codificacion de formato en lista
                pedidos.append(x)  # añadimos x a la lista de pedidos

                # confirmacion de que se ha realizado con exito
                print(f'\nSe ha creado el pedido con la referencia {referencia} y han sido {total} en total')
                break  # fin del bucle
            except ValueError:  # si el try da error por cualquier motivo nos saltaria el mensaje de abajo
                print('\nCalculando referencia')


class Pedidos:  # creacion clase Pedidos
    def __init__(self):  # constructor
        self.pedidos = pedidos  # elemento a construir

        for i in self.pedidos:  # bucle para listar tabla pedidos
            print(i)  # filas de pedidos

    @staticmethod  # Creamos el método estatico para que no necesite los argumentos del constructor
    def sacarFacturaSms():  # definimos la funcion
        clientes = Clientes.getClientes()  # guardo la lista clientes en variable clientes
        while True:  # bucle para el try
            try:  # try intenta realizar el fragmento de codigo para que no se pare la aplicacion si da error
                x = int(input('\nElige un pedido al cual sacar factura por "id": '))  # variable para guardar el id
                y = pedidos[x][1]  # variable para guardar el nombre del usuario asociado al pedido
                contador = 0  # contador para ir por la lista comparando
                while True:  # bucle comparador

                    # comparando la variable "i" con tabla clientes posicion basada en contador
                    if y != clientes[contador][1]:  # si no es concordante se suma 1 al contador
                        contador += 1  # se suma 1 al contador hasta que encuentre una concordacia
                    else:  # concordancia encontrada!
                        cliente = clientes[contador][5]  # guardamos el resultado correcto en la variable cliente
                        break  # fin del bucle

                # si la variable x no es igual al último id de pedios no dejará seleccionarlo
                if int(x) > int(pedidos[-1][0]):  # condicion para la variable "x" contiene él, id seleccionado
                    print('\nEl pedido que has introducido no existe, prueba de nuevo')
                else:  # si el if no se cumple enviará la factura con la referencia marcada
                    print(f'\nLa factura con referencia "{pedidos[int(x)][3]}" ha sido enviada')
                    print('También se ha enviado un SMS a la referencia anterior')

                    if cliente.lower() == 'españa':  # condicion para ver si la nacionalidad es de España con minusculas
                        print('\nLa factura se ha generado con el 21% de iva nacional')  # se aplica el impuesto ESP
                    else:  # se aplica el impuesto internacional
                        print('\nLa factura se ha generado con el 10% de impuesto internacional')

                    input('\nPulsa "Enter" para continuar')  # enter para continuar
                    break  # fin bucle

            except ValueError:  # si el try da error por cualquier motivo nos saltaría el mensaje de abajo
                print('\nSolo admitimos números sin decimales, por favor introduzca algo valido')
