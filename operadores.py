def sumar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve su sumatoria

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: sumatoria de ambos numeros
    """
    return a + b

def restar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve el resultado de su resta

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: resultado de la resta
    """
    return a - b
    
def multiplicar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve su producto

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: producto de la multiplicacion
    """
    return a * b

def dividir(a: int, b: int) -> float:
    """obtiene dos numeros y devuelve el resultado de dividir el primero por el segundo

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: cociente de la division
    """
    return a / b

def factorial(a: int) -> int:
    """obtiene un numero, devuelve su factorial

    Args:
        a (int): un numero

    Returns:
        int: factorial del numero
    """
    resultado = 1

    for i in range(1, a + 1):
        resultado *= i
    return resultado
    