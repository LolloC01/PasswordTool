import string
from random import randint, shuffle

def gen_password(l: int) -> str:
    """generatore password

    Args:
        l (int): lunghezza della password richiesta

    Returns:
        str: password
    """

    #password -> Variabile dove inserisco la password
    password = ""
    #char -> variabile dove inserisco i caratteri da usare nella password
    char = []

    #genero la lista di caratteri da usare nella password
    s = string.ascii_letters + string.digits + string.punctuation

    #GENERATORE DELLA PASSWORD
    #estrae i caratteri da s in modo casuale
    for _ in range(l):
        x = randint(0,len(s)-1)
        char.append(s[x])

    #effettua lo shuffle dei caratteri della password
    shuffle(char)

    #trasforma la password da lista a stringa
    password = "".join(str(element) for element in char)

    #ritorna la password
    return password

print(gen_password(10))