import os
import sys  # not sure
# Definir un diccionario que mapea codones a aminoácidos
tabla_codones = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

# Definir funciones para leer archivos, traducir secuencias, buscar patrones y encontrar palíndromos


def leer_fasta(file_name):
    # Función para leer archivos en formato FASTA y extraer la definición y la secuencia
    entries = []
    defline = ''
    sequence = ''
    with open(file_name, 'r') as F:
        for line in F:
            if line.startswith('>'):
                if defline:  # si defline ya existe, se le agrega la sequencia a defline
                    entries.append((defline, sequence))
                    sequence = ''  # Reset de la sequencia
                defline = line.strip()
            else:
                sequence += line.strip()
        if defline:  # salvar la ultima entrada
            entries.append((defline, sequence))
    return entries


def leer_archivo(ruta_archivo):
    # Función para leer el contenido de un archivo y devolverlo como una cadena de texto
    if not os.path.exists(ruta_archivo):
        print(f"Error: {ruta_archivo} no existe.")
        return ""
    with open(ruta_archivo, 'r') as archivo:
        archivo.readline()
        secuencia = ''.join(archivo.readlines()).replace('\n', '')
    return secuencia


def traductor(secuencia, codones):  # codones es basicamente tabla_codones
    # Función para traducir una secuencia de ADN a una secuencia de aminoácidos utilizando la tabla de codones
    secuenciaA = []  # secuenciaAminoacido

    for i in range(0, len(secuencia), 3):
        codon = secuencia[i:i+3]

        if codon in codones:
            secuenciaA.append(codones[codon])

    return ''.join(secuenciaA)


def kmp_busqueda(texto, patron):
    # Implementación del algoritmo Knuth-Morris-Pratt para buscar un patrón en un texto
    def calcular_lps_array(patron, M, lps):
        longitud = 0
        lps[0] = 0
        i = 1
        while i < M:
            if patron[i] == patron[longitud]:
                longitud += 1
                lps[i] = longitud
                i += 1
            else:
                if longitud != 0:
                    longitud = lps[longitud - 1]
                else:
                    lps[i] = 0
                    i += 1

    M = len(patron)
    N = len(texto)
    lps = [0] * M
    indices = []
    j = 0
    calcular_lps_array(patron, M, lps)
    i = 0
    while i < N:
        if patron[j] == texto[i]:
            i += 1
            j += 1
        if j == M:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < N and patron[j] != texto[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices


def encontrar_palindromo_mas_largo(s):
    # Función para encontrar el palíndromo más largo en una cadena de texto utilizando programación dinámica
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k
    return s[start:start + max_length]


# Leer genomas desde archivos
ruta_genoma_wuhan = "SARS-COV-2-MN908947.3.txt"
ruta_genoma_texas = "SARS-COV-2-MT106054.1.txt"
genoma_wuhan = leer_archivo(ruta_genoma_wuhan)
genoma_texas = leer_archivo(ruta_genoma_texas)

# Verificar que los genomas se leyeron correctamente
if not genoma_wuhan or not genoma_texas:
    exit("Error leyendo los archivos de genomas.")

# Definir rutas de genes de interés
rutas_genes = {
    "M": "gen-M.txt",
    "ORF1ab": "gen-ORF1AB.txt",
    "S": "gen-S.txt",
}


# Encontrar y analizar proteínas


def obtener_codones_desde_aminoacidos(aminoacidos, genoma, codones):
    # funcion para obtener codones desde los aminoacidos
    i = 0
    indices = []
    codones_asociados = []
    while i < len(genoma) - 2:
        codon = genoma[i:i+3]
        if codones[codon] == aminoacidos[0]:
            traduccion = traductor(genoma[i:i+12], codones)
            if traduccion.startswith(aminoacidos):
                indices.append(i)
                codones_asociados.append(genoma[i:i+12])
        i += 3
    return indices, codones_asociados


proteinas_info = leer_fasta("seq-proteins.txt")


# Encontrar índices y palíndromos de los genes
print("===== Análisis de Génes =====")
for nombre_gen, ruta_gen in rutas_genes.items():
    gen = leer_archivo(ruta_gen)
    if not gen:
        continue  # Pasar al siguiente gen si no se pudo leer el archivo
    indices = kmp_busqueda(genoma_wuhan, gen)
    print(f"\nGen {nombre_gen}:")
    print(f"  - Índices de aparición: {indices}")
    print(f"  - Primeros 12 caracteres: {gen[:12]}")

    palindromo = encontrar_palindromo_mas_largo(gen)
    print(f"  - Palíndromo más largo: {palindromo}")
    print(f"  - Longitud del palíndromo: {len(palindromo)}")

    # Guardar palíndromos en archivos
    with open(f"palindromo_{nombre_gen}.txt", "w") as archivo:
        archivo.write(palindromo)

# Encontrar y analizar proteínas
print("\n===== Análisis de Proteínas =====")
for defline, secuencia_proteina in proteinas_info:
    # Extraemos el nombre de la proteína del defline
    nombre_proteina = defline.split()[0][1:]
    aminoacidos = secuencia_proteina[:4]
    indices, codones_asociados = obtener_codones_desde_aminoacidos(
        aminoacidos, genoma_wuhan, tabla_codones)
    for idx, codon in zip(indices, codones_asociados):
        print(f"\nProteína: {nombre_proteina}")
        print(f"  - Índices en el genoma: {idx}-{idx+len(codon)}")
        print(f"  - Primeros 4 aminoácidos: {aminoacidos}")
        print(f"  - Codones asociados: {codon}")


# Comparar genomas y encontrar diferencias
print("\n===== Comparación de Genomas =====")
diferencias = [(i, genoma_wuhan[i], genoma_texas[i]) for i in range(
    min(len(genoma_wuhan), len(genoma_texas))) if genoma_wuhan[i] != genoma_texas[i]]
iguales = [i for i in range(min(len(genoma_wuhan), len(
    genoma_texas))) if genoma_wuhan[i] == genoma_texas[i]]

for indice, base_wuhan, base_texas in diferencias:
    codon_wuhan = genoma_wuhan[indice:indice + 3]
    codon_texas = genoma_texas[indice:indice + 3]
    aminoacido_wuhan = tabla_codones.get(codon_wuhan, '-')
    aminoacido_texas = tabla_codones.get(codon_texas, '-')
    print(f"\nDiferencia en índice {indice}:")
    print(f"  - Wuhan: {base_wuhan} {codon_wuhan}({aminoacido_wuhan})")
    print(f"  - Texas: {base_texas} {codon_texas}({aminoacido_texas})")

print(f"\nÍndices donde son iguales: {iguales[:12]}...")
