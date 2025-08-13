p = 23 # this is the small prime
g = 5 # this is our generator

#Alice has a private key: 6 and a public key pow(g, a, p)
a = 6
A = pow(g, a, p)

b = 15
B = pow(g,b,p)

S_alice = pow(B, a, p)
S_bob = pow(A, b, p)

print(f"Shared Alice: {S_alice}, Shared Bob: {S_bob}")
