def sumar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve su sumatoria

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: sumatoria de ambos numeros
    """
    try:
        return a + b
    except TypeError:
        print("Error, no se pueden realizar operaciones matematicas entre los datos indicados")
sumar("32", 5)

def restar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve el resultado de su resta

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: resultado de la resta
    """
    try:
        return a - b
    except TypeError:
        print("Error, no se pueden realizar operaciones matematicas entre los datos indicados")

def multiplicar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve su producto

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: producto de la multiplicacion
    """
    try:
        return a * b
    except TypeError:
        print("Error, no se pueden realizar operaciones matematicas entre los datos indicados")

def dividir(a: int, b: int) -> float:
    """obtiene dos numeros y devuelve el resultado de dividir el primero por el segundo

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: cociente de la division
    """
    try:
        return a / b
    except TypeError:
        print("Error, no se pueden realizar operaciones matematicas entre los datos indicados")
    except ZeroDivisionError:
        print("ERROR, division por cero")

def factorial(a: int) -> int:
    """obtiene un numero, devuelve su factorial

    Args:
        a (int): un numero

    Returns:
        int: factorial del numero
    """
    resultado = 1
    try:
        for i in range(1, a + 1):
            resultado *= i
        return resultado
    except TypeError:
        print("Error, no se pueden realizar operaciones matematicas con el dato indicado")
    