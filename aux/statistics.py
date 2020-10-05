
english_language_character_frequency = {
    b'E': 2.02,
    b'T': 9.10,
    b'A': 8.12,
    b'O': 7.68,
    b'I': 7.31,
    b'N': 6.95,
    b'S': 6.28,
    b'R': 6.02,
    b'H': 5.92,
    b'D': 4.32,
    b'L': 3.98,
    b'U': 2.88,
    b'C': 2.71,
    b'M': 2.61,
    b'F': 2.30,
    b'Y': 2.11,
    b'W': 2.09,
    b'G': 2.03,
    b'P': 1.82,
    b'B': 1.49,
    b'V': 1.11,
    b'K': 0.69,
    b'X': 0.17,
    b'Q': 0.11,
    b'J': 0.10,
    b'Z': 0.07
}


def how_close_to_english(string_in_bytes):
    stripped = remove_not_ascii_letter(string_in_bytes).upper()
    frequency = get_frequency(stripped)
    for i in range(65, 91):
        if bytes([i]) not in frequency:
            frequency[bytes([i])] = 0
    return vector_powered_distance(english_language_character_frequency, frequency)


def vector_powered_distance(vect1, vect2):
    acc = 0
    for key in vect1:
        acc += pow(vect1[key] - vect2[key], 2)
    return acc


def get_frequency(phrase):
    character_count = {}
    max_val = 0
    for c in phrase:
        if c not in character_count:
            character_count[bytes([c])] = 0
        tmp = character_count[bytes([c])] + 1
        if max_val < tmp:
            max_val = tmp
        character_count[bytes([c])] += 1

    characte_frequency = {key: value /
                          max_val for (key, value) in character_count.items()}
    return characte_frequency


def remove_not_ascii_letter(string):
    r = b''
    for c in string:
        if c >= 65 and c <= 90 or c >= 97 and c <= 122:
            r += bytes([c])
    return r


def most_close_to_english(l):
    all = list(map(how_close_to_english, l))

    best, index = 9999999999999999, 0
    for i in range(len(all)):
        if all[i] < best:
            best = all[i]
            index = i
    return l[index]
