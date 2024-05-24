def sumar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve su sumatoria

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: sumatoria de ambos numeros
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Se intentó operar con datos que no son numeros enteros")
    
    return a + b

def restar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve el resultado de su resta

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: resultado de la resta
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Se intentó operar con datos que no son numeros enteros")
    
    return a - b
    
def multiplicar(a: int, b: int) -> int:
    """obtiene dos numeros y devuelve su producto

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: producto de la multiplicacion
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Se intentó operar con datos que no son numeros enteros")
    
    return a * b

def dividir(a: int, b: int) -> float:
    """obtiene dos numeros y devuelve el resultado de dividir el primero por el segundo

    Args:
        a (int): numero 1
        b (int): numero 2

    Returns:
        int: cociente de la division
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("ERROR: se intentó operar con datos que no son numeros enteros")
    
    if b == 0:
        raise ZeroDivisionError("ERROR: division por cero")

    return a / b

def factorial(a: int) -> int:
    """obtiene un numero, devuelve su factorial

    Args:
        a (int): un numero

    Returns:
        int: factorial del numero
    """
    if not isinstance(a, int):
        raise TypeError("Se intentó operar con datos que no son numeros enteros")
        
    if a == 0 or a == 1:
        resultado = 1
    else:
        resultado = a * factorial(a - 1)
    
    return resultado

print(factorial(5))