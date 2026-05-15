def logger(fonction):
    def wrapper(*args, **kwargs):       # accepte tous les arguments
        print(f"Appel de {fonction.__name__} avec {args}")
        resultat = fonction(*args, **kwargs)   # transmet les arguments
        print(f"Résultat : {resultat}")
        return resultat
    return wrapper

@logger
def additionner(x, y):
    return x + y

additionner(3, 4)
# → Appel de additionner avec (3, 4)
# → Résultat : 7