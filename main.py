#  Importacion de librerias importantes para el funcionamiento de la aplicacion
import os  # Para limpiar la pantalla
import unittest
from Cliente import Cliente, Clientes
from Productos import Producto, Productos
from Pedido import Pedido, Pedidos

os.system('cls')  # Lipieza de pantalla
usuario = Clientes.logIn()   # Funcion logIn para inciar sesion
sesion = f'+---------<[{usuario}]>---------+'  # estandarte indicador de usuario
input("\nPulsa enter para continuar")  # input de enter para continuar

while True:  # bucle para que la aplicacion funcione todo el tiempo
    os.system('cls')  # Limpieza de pantalla
    print(sesion)
    print('\n- 1: Cambiar usuario         -')
    print('\n- 2: Crear cliente           -')
    print('\n- 3: Mostrar clientes        -')
    print('\n- 4: introducir producto     -')     # Este bloque de prints sirve
    print('\n- 5: Mostrar productos       -')     # para que el usuario vea el menu
    print('\n- 6: Crear pedido            -')
    print('\n- 7: Mostrar pedidos         -')
    print('\n- 8: Procesar factura / SMS  -')
    print('\n- 0: Salir                   -')
    print('------------------------------')

    print('\nSi introduce mal un dato o deja alguna funcion a medias le sacara del programa')  # Advertencia

    opc = int(input("\nIntroduce una accion(con el numero): "))  # input de opcion para elegir el programa

    match opc:  # Match opc que es la variable de encima para elejir opcion
        case 1:  # caso de que sea 1
            os.system('cls')
            usuario = Clientes.logIn()  # se vuelve a ejecutar la funcion login para cambiar el usuario
            sesion = f'+---------<[{usuario}]>---------+'  # nuevo estandarte de indicacion de sesion
            input("\nPulsa enter para continuar")  # input de enter para continuar
        case 2:  # caso de que sea 2
            os.system('cls')
            # print informativo de lo que va a ocurrir
            print('introduce: Nombre, Apellido, DNI, Edad, nacionalidad, Codigo postal, Telefono, Email y Dinero '
                  'disponible \nSeparado por "enter" entre cada dato\n')

            # Sucesion de inputs para llenar los campos de la funcion
            nombre = input('Nombre: ')
            apellidos = input('Apellidos: ')
            dni = input('DNI con letra: ')
            edad = int(input('Edad (solo numeros): '))
            nacionalidad = input('nacionalidad: ')
            tl = int(input('telefono (solo numeros): '))
            email = input('Email: ')
            presupuesto = int(input("Dinero disponible (solo numeros): "))

            # clase constructora Cliente con funcion crearCliente para añadir clientes a la lista
            Cliente(nombre, apellidos, dni, edad, nacionalidad, tl, email, presupuesto).crearCliente()
        case 3:  # caso de que sea 3
            os.system('cls')
            # print informativo sobre los campos de la tabla
            print('id  Nombre   Apellido    DNI    Edad  Nacionalidad    Telefono       Email               Banca\n')

            # la clase Clientes tiene en el constructor que imprime la lista ordenada for filas
            Clientes()

            # input de enter para continuar
            input('\nPulsa enter para continuar')
        case 4:  # caso de que sea 4
            os.system('cls')
            # print informativo de lo que va a suceder
            print('introduce: Nombre del producto, tipo e objeto y precio \nSeparado por "enter" entre cada dato\n')

            # Sucesion de inputs para llenar los campos de la funcion
            nombre = input('Nombre: ')
            tipo = input('tipo: ')
            precio = float(input('Precio (solo numeros): '))

            # clase constructora Producto con funcion crearProducto para añadir productos a la lista
            Producto(nombre, tipo, precio).crearProducto()
        case 5:  # caso de que sea 5
            os.system('cls')
            # print informativo sobre los campos de la tabla
            print('Id Producto Tipo Precio\n')

            # la clase Productos tiene en el constructor que imprime la lista ordenada for filas
            Productos()

            # input de enter para continuar
            input('\nPulsa enter para continuar')
        case 6:  # caso de que sea 6
            while True:  # bucle para poder ir elijiendo varios productos
                os.system('cls')

                # clase Productos para mostrar el listado de estos
                Productos()
                producto = int(input('\nQue producto deseas? por id: '))  # variable que guarda el producto deseado
                # En esta variable guardo la lista de productos en una variable para manipularla en este documento

                # Aquí construllo el pedido con el constructor Pedido y con crearPedido lo añado a lista de pedidos
                Pedido(producto).crearPedido(usuario)
                x = input('Desea realizar otro pedido? si/no: ')  # Variable para saber si quieres seguir o no
                # el .lower sirve para poner la opcion en minusculas
                if x.lower() == 'no':  # condicion para ver si decides que no quieres seguir
                    break  # Rompe el bucle
        case 7:  # caso de que sea 7
            os.system('cls')
            # print informativo de los valores de la tabla
            print('Id Nombre Producto Referencia Precio\n')

            # clase Pedidos que lista los pedidos en orden
            Pedidos()
            input('\nPulsa enter para continuar')  # input de enter para continuar

        case 8:  # caso de que sea 7
            os.system('cls')
            Pedidos()  # Listado de Pedidos
            Pedidos.sacarFacturaSms()  # Funcion para realizar las facturas y SMS aqui tambien se cobra la nacionalidad
        case _:  # caso alternativo para salir de la aplicacion
            break
