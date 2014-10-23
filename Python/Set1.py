#CryptoPals Tip: Never operate on encoded strings, just the raw bytes. Encoding is for pretty printing
import base64
import array
import string
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
    freq = dict()
    for char in string.printable:
        hexChar = char.encode("hex") #get the ascii character to a hex
        
        
        
        stringXOR = hexXOR.decode("hex")
        print stringXOR
        for char in stringXOR:
            freq[char] += 1
        eFreq = (freq[e] + freq[E])/len(hexXor)
        print eFreq
       #if (eFreq > 10 and eFreq < 15)
        
print breakSingleByteCipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")