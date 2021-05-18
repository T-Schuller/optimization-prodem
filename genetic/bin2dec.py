def bin2dec(binary): 
      
    binary1 = binary
    binary=int(binary) 
    decimal = 0
    i = 0
    n = 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal