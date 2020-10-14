import string
import re
def autoclave(palabra, clave, modulo):
    res = ""
    ab={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,
    'N':13,'Ñ':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,
    'Z':26}
    if modulo == 27:
        i = 0
        move = 0
        while True:
            if len(palabra) == len(clave):
                break
            if len(clave) == i:
                clave = clave + res[move]
                move = move + 1
            c = ab.get(palabra[i]) + ab.get(clave[i])
            c = c % modulo
            for j in ab:
                if ab.get(j)==c:
                    res = res + j
            i = i + 1
    return res

palabra = input()
palabra = palabra.replace(' ','')
palabra = palabra.replace('á','a')
palabra = palabra.replace('é','e')
palabra = palabra.replace('í','i')
palabra = palabra.replace('ó','o')
palabra = palabra.replace('ú','u')
palabra = palabra.translate(str.maketrans('', '', string.punctuation))
clave = input()
modulo = int(input())
r = autoclave(palabra,clave,modulo)
print(r)

       

    
    
