def KMP(haystack, needle):
    # el primer paso es desarrollar el lps basado en el needle
    lps = [0] * len(needle)
    i = 0  # puntero inicial
    j = 1  # puntero actual

    while j < len(needle):
        if needle[i] == needle[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        elif i == 0:
            lps[j] = 0
            j += 1
        else:
            i = lps[i-1]

    i = 0  # puntero para haystack
    j = 0  # puntero para needle

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
        if j == len(needle):
            return i - len(needle)
    return -1


print(KMP("babababananabana", "banana"))
