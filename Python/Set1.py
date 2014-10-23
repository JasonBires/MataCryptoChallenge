#CryptoPals Tip: Never operate on encoded strings, just the raw bytes. Encoding is for pretty printing
import base64
import array
def hex_to_base64(hexString):
    decodedHex = hexString.decode("hex")
    return base64.standard_b64encode(decodedHex)
    
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
    
def breakSingleByteCipher(hexString):
    
print fixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")