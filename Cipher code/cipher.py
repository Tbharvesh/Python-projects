z='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789~!@#$%^&*_.'


def cipher():
    print('Enter text that you want to convert to code')
    p=str(input())
    n=len(p)
    j=''
    print('Set key')
    t=int(input())
    i=0
    while i<n:
        j=j+(z[((z.index(p[i])+t)%53)])
        i=i+1
    return j

def decipher():
    print('Enter code that you want to convert to text')
    p=str(input())
    n=len(p)
    j=''
    print('Enter key')
    t=int(input())
    i=0
    while i<n:
        j=j+(z[((z.index(p[i])+t)%53)])
        i=i+1
    return j
print(cipher())
print(decipher())