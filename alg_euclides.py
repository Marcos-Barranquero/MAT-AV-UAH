""" Algoritmo extendido de euclides """


def imprimir_matriz(columna1, columna2):
    """ Dada una matriz definida por sus columnas, la imprime """
    print("-----------")
    print("(", columna1[0], ",", columna2[0], ")")
    print("(", columna1[1], ",", columna2[1], ")")
    print("(", columna1[2], ",", columna2[2], ")")
    print("-----------")


def inverso(numero, mod):
    resolucion(numero, 1, mod)


def alg_euclides_ext(n1, n2):
    """ Ejecuta la interpretación del algoritmo de euclides extendido """
    imprimir_matriz([n1, 1, 0], [n2, 0, 1])
    return alg_euclides_ext_aux([n1, 1, 0], [n2, 0, 1])


def alg_euclides_ext_aux(c1, c2):
    """ Realiza la interpretación matricial del algoritmo de euclides extendido. """
    a = c1[0]
    b = c2[0]
    if(a > b):
        multiplicador = -1*(a // b)
        c_aux = []
        nueva_c1 = []
        for valor in c2:
            c_aux.append(valor * multiplicador)

        for i in range(len(c_aux)):
            nueva_c1.append(c1[i] + c_aux[i])
        c1 = list(nueva_c1)

    if(b > a):
        multiplicador = -1*(b // a)
        c_aux = []
        nueva_c2 = []
        for valor in c1:
            c_aux.append(valor * multiplicador)

        for i in range(len(c_aux)):
            nueva_c2.append(c2[i] + c_aux[i])
        c2 = list(nueva_c2)

    imprimir_matriz(c1, c2)

    if(not(c1[0] == 0 or c2[0] == 0)):
        return alg_euclides_ext_aux(c1, c2)
    else:
        if(c1[0] == 0):
            return c2[1]
        else:
            return c1[1]


def resolucion(n1, b, n2):
    """ transforma una expresión k*n1 = b (mod n2) a k = b' (mod n2) """
    inverso = alg_euclides_ext(n1, n2)
    k = (b * inverso) % n2
    print("k = ", k, "(mod ", n2, ")")


def funcion(numero):
    """ Retorna el valor de P(x) sustituyendo x por el numero. """
    return (numero)**2 + 15*(numero)+8


def generar_tabla(mod):
    """ Genera la tabla de todos los posibles valores de la función en módulo mod """
    print("f(x)\tValor\tResto")
    for i in range(mod):
        valor = funcion(i)
        resto = valor % mod
        if(resto == 0):
            print(i, "\t", valor, "\t", resto, " < Válida")
        else:
            print(i, "\t", valor, "\t", resto)


def generar_tabla_soluciones(mod):
    for i in range(mod):
        if funcion(i) % mod == 0:
            print(i, " + k (mod", mod, ")")


# generar_tabla(3)
#resolucion(4, 4, 8)

#inverso(5, 13)

alg_euclides_ext(1976, 647)

# generar_tabla_soluciones(21)
