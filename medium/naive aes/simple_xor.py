def xor(X, Y):
    return bytes([X[i] ^ Y[i] for i in range(len(X))])