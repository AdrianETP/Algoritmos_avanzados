from collections import Counter
import os
import heapq
import pickle


class HuffmanNode:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(probabilities):
    # Crear una cola de prioridad (heap) de nodos Huffman iniciales
    heap = [HuffmanNode(char, freq, None, None)
            for char, freq in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Tomar los dos nodos con las frecuencias más bajas
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Crear un nuevo nodo que representa la combinación de los dos nodos anteriores
        combined_node = HuffmanNode(None, left.freq + right.freq, left, right)

        # Agregar el nuevo nodo al heap
        heapq.heappush(heap, combined_node)

    # El último nodo en el heap es la raíz del árbol de Huffman
    huffman_tree = heap[0]

    return huffman_tree


def build_huffman_codes(node, code, huffman_codes):
    if node.char is not None:
        huffman_codes[node.char] = code
    if node.left is not None:
        build_huffman_codes(node.left, code + "0", huffman_codes)
    if node.right is not None:
        build_huffman_codes(node.right, code + "1", huffman_codes)


def encode_text(text, huffman_codes):
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text


def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree
    return decoded_text


def calculate_probabilities(text):
    # Elimina acentos y caracteres no deseados
    # Convierte todo a minúsculas para tratar las letras mayúsculas y minúsculas de manera igual
    text = text.lower()
    # Elimina caracteres no alfanuméricos excepto espacios
    text = ''.join(e for e in text if e.isalnum() or e.isspace())

    # Calcula las frecuencias de los caracteres en el texto
    char_frequencies = Counter(text)

    # Calcula las probabilidades dividiendo las frecuencias por la longitud del texto
    total_chars = len(text)
    char_probabilities = {
        char: freq / total_chars for char, freq in char_frequencies.items()}

    return char_probabilities


lines = ""
with open("texto.txt") as texto:
    lines = texto.read()
probabilities = calculate_probabilities(lines)
tree = build_huffman_tree(probabilities)
huffman_codes = {}
build_huffman_codes(tree, "", huffman_codes)

text = ''.join(e for e in lines if e.isalnum() or e.isspace())
text = text.lower()
binary = encode_text(text, huffman_codes)
print(binary)

binfile = open("binary.bin", "w")

binfile.write(binary)

while True:
    print("selecciona una opcion del menu:")
    print("1. encodificar un input")
    print("2. decodificar un input")
    print("3. Salir")
    choice = input("option: ")

    if int(choice) == 1:
        inp = input("escribe el texto: ")
        print(encode_text(inp, huffman_codes))
    elif int(choice) == 2:
        inp = input("escribe el texto: ")
        print(decode_text(inp, tree))
    else:
        break
