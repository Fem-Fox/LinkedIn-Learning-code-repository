
def encodeString(stringVal):
    # Your code goes here.
    list_compressed =''
    count = 1
    for index in range(1, len(stringVal)):

        if stringVal[index] == stringVal[index-1]:
            count += 1
        else:

            list_compressed += f'{stringVal[index-1]} {count}.'
            count = 1
        
    list_compressed += f'{stringVal[-1]} {count}'

    list_compressed = list_compressed.split(".")
    
    list_compressed = [item.split(" ") for item in list_compressed]

    
    for i in range(0, len(list_compressed)):

        list_compressed[i][1] = int(list_compressed[i][1])

    final_list_compressed = [tuple(item) for item in list_compressed]
    return final_list_compressed
    
    
    



def decodeString(encodedList):
    # Your code goes here.
    decoded_string = ''
    for item in encodedList:
        list_sub_tuple= list(item)
        decoded_string += f'{list_sub_tuple[0]*(list_sub_tuple[1])}'

    return decoded_string



print(decodeString(encodeString('AAAAABBBBAAA')))



'''
[('A',5),('B',4),('A',3)]
'''