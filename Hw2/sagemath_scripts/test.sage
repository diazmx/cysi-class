from sage.crypto.block_cipher.des import DES

des = DES()
P = 0x01A1D6D039776742
K = 0x7CA110454A1A6E57
C = des.encrypt(plaintext=P, key=K)
print(c.hex())
P = des.decrypt(ciphertext=C, key=K)
print(P.hex())
