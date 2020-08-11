

reverse_lookup_table = [
    ['\x52', '\x09', '\x6a', '\xd5', '\x30', '\x36', '\xa5', '\x38',
        '\xbf', '\x40', '\xa3', '\x9e', '\x81', '\xf3', '\xd7', '\xfb'],
    ['\x7c', '\xe3', '\x39', '\x82', '\x9b', '\x2f', '\xff', '\x87',
        '\x34', '\x8e', '\x43', '\x44', '\xc4', '\xde', '\xe9', '\xcb'],
    ['\x54', '\x7b', '\x94', '\x32', '\xa6', '\xc2', '\x23', '\x3d',
        '\xee', '\x4c', '\x95', '\x0b', '\x42', '\xfa', '\xc3', '\x4e'],
    ['\x08', '\x2e', '\xa1', '\x66', '\x28', '\xd9', '\x24', '\xb2',
        '\x76', '\x5b', '\xa2', '\x49', '\x6d', '\x8b', '\xd1', '\x25'],
    ['\x72', '\xf8', '\xf6', '\x64', '\x86', '\x68', '\x98', '\x16',
        '\xd4', '\xa4', '\x5c', '\xcc', '\x5d', '\x65', '\xb6', '\x92'],
    ['\x6c', '\x70', '\x48', '\x50', '\xfd', '\xed', '\xb9', '\xda',
        '\x5e', '\x15', '\x46', '\x57', '\xa7', '\x8d', '\x9d', '\x84'],
    ['\x90', '\xd8', '\xab', '\x00', '\x8c', '\xbc', '\xd3', '\x0a',
        '\xf7', '\xe4', '\x58', '\x05', '\xb8', '\xb3', '\x45', '\x06'],
    ['\xd0', '\x2c', '\x1e', '\x8f', '\xca', '\x3f', '\x0f', '\x02',
        '\xc1', '\xaf', '\xbd', '\x03', '\x01', '\x13', '\x8a', '\x6b'],
    ['\x3a', '\x91', '\x11', '\x41', '\x4f', '\x67', '\xdc', '\xea',
        '\x97', '\xf2', '\xcf', '\xce', '\xf0', '\xb4', '\xe6', '\x73'],
    ['\x96', '\xac', '\x74', '\x22', '\xe7', '\xad', '\x35', '\x85',
        '\xe2', '\xf9', '\x37', '\xe8', '\x1c', '\x75', '\xdf', '\x6e'],
    ['\x47', '\xf1', '\x1a', '\x71', '\x1d', '\x29', '\xc5', '\x89',
        '\x6f', '\xb7', '\x62', '\x0e', '\xaa', '\x18', '\xbe', '\x1b'],
    ['\xfc', '\x56', '\x3e', '\x4b', '\xc6', '\xd2', '\x79', '\x20',
        '\x9a', '\xdb', '\xc0', '\xfe', '\x78', '\xcd', '\x5a', '\xf4'],
    ['\x1f', '\xdd', '\xa8', '\x33', '\x88', '\x07', '\xc7', '\x31',
        '\xb1', '\x12', '\x10', '\x59', '\x27', '\x80', '\xec', '\x5f'],
    ['\x60', '\x51', '\x7f', '\xa9', '\x19', '\xb5', '\x4a', '\x0d',
        '\x2d', '\xe5', '\x7a', '\x9f', '\x93', '\xc9', '\x9c', '\xef'],
    ['\xa0', '\xe0', '\x3b', '\x4d', '\xae', '\x2a', '\xf5', '\xb0',
        '\xc8', '\xeb', '\xbb', '\x3c', '\x83', '\x53', '\x99', '\x61'],
    ['\x17', '\x2b', '\x04', '\x7e', '\xba', '\x77', '\xd6', '\x26',
        '\xe1', '\x69', '\x14', '\x63', '\x55', '\x21', '\x0c', '\x7d']
]


def decrypt(enc, key):
    rounds = 0
    if len(key) == 16:
        rounds = 9


def normal_round():
    pass


def final_round():
    pass


def add_round_key():
    pass


def substite(byte, table):
    row = byte >> 4
    column = byte & 15
    return table[row][column]


def jumble_rows(matrix, enc=True):
    if enc:
        r = range(4)
    else:
        r = range(3,-1,-1)
    return [[matrix[i][(i*j)%4] for j in r] for i in range(4)]
    


def jumble_columns():
    pass
