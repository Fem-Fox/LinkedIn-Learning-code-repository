
'''
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
list_hexNumbers = ['0','1','2','3', '4','5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F']
# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    decNum = None
    if len(hexNum) == 3:
        if hexNum[0] in list_hexNumbers:
            if hexNum[1] in list_hexNumbers:
                if hexNum[2] in list_hexNumbers:
                    decNum = (16**2)*(hexNumbers[hexNum[0]]) + (16)*(hexNumbers[hexNum[1]]) + (hexNumbers[hexNum[2]])
                    return decNum
    
    if len(hexNum) == 2:
        if hexNum[0] in list_hexNumbers:
            if hexNum[1] in list_hexNumbers:
                decNum = (16)*(hexNumbers[hexNum[0]]) + (hexNumbers[hexNum[1]])
                return decNum

    if len(hexNum) == 1:
        if hexNum[0] in list_hexNumbers:
                decNum = hexNumbers[hexNum[0]]
                return decNum
                    
    return decNum
'''