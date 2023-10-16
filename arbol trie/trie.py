
class SuffixNodo:
    def __init__(self, valor, fin):
        # Agrega sus atributos
        self.hijos = []
        self.indices = []
        self.valor = valor
        self.fin = fin


class Nodo:
    def __init__(self, valor, fin):
        # Agrega sus atributos
        self.hijos = []
        self.valor = valor
        self.fin = fin


class Trie:
    #   Inicializa la raiz con un caracter nulo y False
    def __init__(self):
        self.raiz = Nodo("", False)

        # Que parametros necesita?
        # El nodo a partir del cual insertar
        # La cadena sufijo que se esta agregando
        # Un valor i para iterar en la cadena sufijo
        # El indice para saber donde inicia la cadena sufijo en la cadena
        # original (sirve para saber donde ocurre cada caracter)

    def insertar(self, nodo, i, index, cadena):
        # Cuando continua la recursividad?  Mientras i sea menor que la
        # longuitud de la cadena
        m = len(cadena)
        if i < m:

            # Revisa los hijos del nodo, para saber si uno coincide con
            # cadena[i]
            # Si encuentras uno, agrega a su lista de indices la posicion que
            # ocupa cadena[i] en la cadena original
            # Luego, realiza una llamada recursiva nueva para insertar el
            # siguiente caracter a partir del hijo
            # Y luego return
            for h in nodo.hijos:
                if h.valor == cadena[i]:
                    h.fin = i == (m-1)
                    self.insertar(h, i+1, index, cadena)
                    return

            #   Pero, si ningun hijo coincidio, crea un hijo nuevo con el
            # caracter cadena[i]
            #   El hijo nuevo necesita que calculemos sus atributos
            hijo_nuevo = Nodo(cadena[i], i == (m-1))

            # Agrega el hijo nuevo al padre
            nodo.hijos.append(hijo_nuevo)

            # Y por ultimo crea una nueva llamada recursiva
            # para insertar el caracter i+1 de cadena a partir del hijo donde
            # quedo cadena[i]
            self.insertar(hijo_nuevo, i+1, index, cadena)

        # Para busqueda recursiva (mas facil) necesitas pasar el nodo a
        # comparar.
        # Inicialemente, es la raiz
        # Para la siguiente llamada recursiva, sera el hijo que coincida con
        # cadena[i]
        # Asi que tambien habra que actualizar i
        # def buscar(self, nodo, cadena, i):
        # pass

    # una funcion para hacer el recorrido inorder del arbol

    def show_inorder(self, nodo):
        print("\nCaracter ", nodo.valor, "existe en: ",
              nodo.indices, "final", nodo.fin)
        print("\tHijos", [h.valor for h in nodo.hijos])

        for h in nodo.hijos:
            self.show_inorder(h)

    def word_search(self, word, i, node):
        m = len(word)
        if i < m:
            for h in node.hijos:
                if h.valor == word[i]:
                    return self.word_search(word, i+1, h)
        return node.fin


class SuffixTrie:
    #   Inicializa la raiz con un caracter nulo y False
    def __init__(self):
        self.raiz = Nodo("", False)

        # Que parametros necesita?
        # El nodo a partir del cual insertar
        # La cadena sufijo que se esta agregando
        # Un valor i para iterar en la cadena sufijo
        # El indice para saber donde inicia la cadena sufijo en la cadena
        # original (sirve para saber donde ocurre cada caracter)

    def insertar(self, nodo, i, index, cadena):
        # Cuando continua la recursividad?  Mientras i sea menor que la
        # longuitud de la cadena
        m = len(cadena)
        if i < m:

            # Revisa los hijos del nodo, para saber si uno coincide con
            # cadena[i]
            # Si encuentras uno, agrega a su lista de indices la posicion que
            # ocupa cadena[i] en la cadena original
            # Luego, realiza una llamada recursiva nueva para insertar el
            # siguiente caracter a partir del hijo
            # Y luego return
            for h in nodo.hijos:
                if h.valor == cadena[i]:
                    h.indices.append(index + i)
                    h.fin = i == (m-1)
                    self.insertar(h, i+1, index, cadena)
                    return

            #   Pero, si ningun hijo coincidio, crea un hijo nuevo con el
            # caracter cadena[i]
            #   El hijo nuevo necesita que calculemos sus atributos
            hijo_nuevo = SuffixNodo(cadena[i], i == (m-1))
            hijo_nuevo.indices.append(index + i)

            # Agrega el hijo nuevo al padre
            nodo.hijos.append(hijo_nuevo)

            # Y por ultimo crea una nueva llamada recursiva
            # para insertar el caracter i+1 de cadena a partir del hijo donde
            # quedo cadena[i]
            self.insertar(hijo_nuevo, i+1, index, cadena)

        # Para busqueda recursiva (mas facil) necesitas pasar el nodo a
        # comparar.
        # Inicialemente, es la raiz
        # Para la siguiente llamada recursiva, sera el hijo que coincida con
        # cadena[i]
        # Asi que tambien habra que actualizar i
        # def buscar(self, nodo, cadena, i):
        # pass

    # una funcion para hacer el recorrido inorder del arbol

    def show_inorder(self, nodo):
        print("\nCaracter ", nodo.valor, "existe en: ",
              nodo.indices, "final", nodo.fin)
        print("\tHijos", [h.valor for h in nodo.hijos])

        for h in nodo.hijos:
            self.show_inorder(h)

    def suffix_search(self, word, i, node):
        m = len(word)
        if i < m:
            for h in node.hijos:
                if h.valor == word[i]:
                    return self.suffix_search(word, i+1, h)
            return -1
        return [node.indices[j] - len(word)+1 for j in range(len(node.indices))]

        # Obten la longuitud de la palabra
palabra = "anabanana"
n = len(palabra)

# Obtene su lista de sufijos
sufijos = [palabra[i:] for i in range(n)]

# crea un arbol trie
strie = SuffixTrie()

# Agrega cada cadena sufijo al arbol
for i in range(len(sufijos)):
    strie.insertar(strie.raiz, 0, i, sufijos[i])


# para el diccionario de palabras es el mismo progedimiento con la exepcion de que aqui no vamos a usar los indices
palabras = ["casi", "casa", "cama", "camisa", "ave", "alce"]

wtrie = Trie()

for i in range(len(palabras)):
    wtrie.insertar(wtrie.raiz, 0, i, palabras[i])


print(wtrie.word_search("banco", 0, wtrie.raiz))
print(wtrie.word_search("hola", 0, wtrie.raiz))


print(strie.suffix_search("ana", 0, strie.raiz))
