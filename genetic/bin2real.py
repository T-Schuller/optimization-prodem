from bin2dec import bin2dec

def bin2real (s):
    r=0
    for i in range(len(s)):
        r = r + bin2dec(s[-i])*2**(i-1)
    return r