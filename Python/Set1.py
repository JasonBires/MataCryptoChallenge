#CryptoPals Tip: Never operate on encoded strings, just the raw bytes. Encoding is for pretty printing
import base64
import array
import string
from collections import Counter
#challenge 1
def hex_to_base64(hexString):
    decodedHex = hexString.decode("hex")
    return base64.standard_b64encode(decodedHex)
#challenge 2
def fixedXOR(hexString1, hexString2):
    decodedHex1 = hexString1.decode("hex")
    decodedHex2 = hexString2.decode("hex")
    bytes1 = array.array("B", decodedHex1)
    bytes2 = array.array("B", decodedHex2)
    combo = array.array("B")
    for b1, b2 in zip(bytes1,bytes2):
        combo.append(b1^b2)
    xorString = combo.tostring()
    encodedXOR = xorString.encode("hex")
    return encodedXOR
#challenge 3
def breakSingleByteCipher(hexString):
    decodedHex = hexString.decode("hex")
    bytes = array.array("B", decodedHex)
    
    charsToCheck = string.printable
    charsToCheckArr = array.array("B", string.printable)
    bestCandidateList = []
    for char in charsToCheckArr:
        combo = array.array("B")
        for b in bytes:
            combo.append(b ^ char)
        xorString = combo.tostring()
        xorString = xorString.encode("ascii")
        #print "XORSTRING ", xorString, " XORSTRING", char
        freqs = Counter(xorString.split())
        bestCandidateList.append((char, len(freqs), xorString))
    bestCandidateList = sorted(bestCandidateList, key=lambda length:length[1], reverse=True)
    for cand, x in zip(bestCandidateList, range(8)):
        print "CHAR:", cand[0], "\nSTRING:", cand[2]
        
print breakSingleByteCipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")