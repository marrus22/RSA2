# schematische implementierung des RSA-Algorithmus

#import benötigter funktionen
from sympy import prime # Primzahlen
from sympy import factorint # Primfaktorzerlegung
from sympy import mod_inverse # Kehrwert modulo einer Zahl

p = prime(1000)
print('p = ', p)
q = prime(2102)
print('q = ', q)
n = p * q
print('n = ', n)
# RSA kann positive ganze Zahlen kleiner N verschlüsseln

# e == encryption or public key
# e muss eine teilerfremde Zahl von phi
phi = (p-1)*(q-1)
print(factorint(phi))
e = 3 * 11 * 17 * 29 * 31
print('public_key = ', e)

# d == decryption or private key
# kehrwert von phi modulo e bedeutet phi^-1 * phi = 1 * (m*e), m = 1,2,3,...
d = mod_inverse(e, phi)
print('private_key = ', d)

# crypto function
def crypt (x,y,z):
    return x ** y % z
# crypt = lambda x, y, z: x ** y % z # mit lamda notation (anonyme funktion)
# wesentlich ist: (N ** e) ** d = N in modularer arithmetik zur basis n

# the number we want to encrypt
N = 42
print('Original_Nachricht = ', N)

# encryption
S = crypt(N, e, n)
print('Verschluesselte_Nachricht = ', S)

# decryption
Entschluesselte_Nachricht = crypt(S, d, n)
print('Entschluesselte_Nachricht = ', Entschluesselte_Nachricht)

# zwei anwendungen für RSA
#   verschlüselung: verschlüsselung mit public und entschlüsselung mit private public_key
#   verifizierung: sender schickt nachricht 2x, 1x ohne und einmal mit private key verschlüsseöt
#       empfänger kann mittels public key entschlüsseln, vergeichen und absender ident.
