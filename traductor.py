import os, sys
import json

# Variables globals constants
FILESDIR = "arxius"
JSONFILE = "l-system.json"
HLINE = 32*"-"

"""
Crea una carpeta $dirname si no existeix
$dirname: string
"""
def create_dir(dirname):
    if not os.path.exists(FILESDIR):
        os.makedirs(FILESDIR)

"""
Guarda la variable $var en format JSON en el fitxer $fpath
$var: estructura de dades Python
$fpath: string
"""
def variable_to_json(var, fpath):
    print(f"[DEBUG]: Creant fitxer JSON {fpath}")
    with open(fpath, 'w') as fjson:
        json.dump(var, fjson)

"""
Retorna un diccionari Python amb les variables guardades dintre
el fitxer JSON $fpath
$fpath: string
"""
def json_to_variable(fpath):
    print(f"[DEBUG]: Carregant fitxer JSON {fpath}")
    jsondata = None
    with open(fpath, 'r') as fjson:
        jsondata = json.load(fjson)

    print(f"[DEBUG]: Dades carregades:\n"
          f"[DEBUG]: {jsondata}")
    return jsondata

def read_input():
    idata = {"N": int}

    N = input("Introdueix el nombre d'iteracions del L-System\n")
    try:
        N = int(N)
    except:
        print(f"[ERROR]: El nombre d'iteracions ha de ser un numero enter. "
              f"Nombre introduit: {N}")
        sys.exit(-1)

    idata["N"] = N

    return idata

if __name__ == '__main__':
    create_dir(FILESDIR)
    l_system = json_to_variable(FILESDIR + "/" + JSONFILE)
    idata = read_input()

    sentence = None
    axioma = l_system["axioma"]
    alfabet = l_system["alfabet"]
    N = idata["N"]

    reglesp = l_system["reglesp"]
    print(f"{HLINE}\n"
          f"[DEBUG]: INICIANT TRADUCCIO\n"
          f"[DEBUG]: Iteracions: {N}\n"
          f"[DEBUG]: Alfabet: {alfabet}\n"
          f"[DEBUG]: Regles de Produccio: {reglesp}\n"
          f"[DEBUG]: Axioma inicial: {axioma}")

    for i in range(1, N+1):
        sentence = ""
        for c in axioma:
            if c in reglesp:
                sentence = sentence + reglesp[c]
            else:
                sentence = sentence + c
        axioma = sentence
        print(f"[DEBUG]: Iteracio {i} | Axioma = {axioma}")

    print(HLINE)
    print(f"Resultat de la traducció amb {N} it.:\n"
          f"{axioma}")
    print(HLINE)

    sys.exit(0)



