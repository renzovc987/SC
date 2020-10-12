import string
import re
def nueva_cl(clave, lenght):
    key=""
    i=0
    j=0
    for i in range(lenght):
        if i>0 and (i%len(clave)==0):
            j=0
        key=key+clave[j]
        j=j+1
    return key
ab={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,
    'N':13,'Ñ':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,
    'Z':26}
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
tamp = len(palabra)
tamc = len(clave)
tamr = tamp - tamc
palabra = palabra.upper()
nueva_clave = nueva_cl(clave,tamp)
nueva_clave = nueva_clave.upper()  
r = ""
c=0
if(modulo==27):
    for i in range(tamp):
        c =(ab.get(palabra[i])+ab.get(nueva_clave[i]))
        c = (c%modulo)
        for j in ab:
            if ab.get(j)==c:
                r = r + j
elif(modulo==191):
    for i in range(tamp):
       c = int((ord(palabra[i])+ord(nueva_clave[i]))%modulo)
       r = r + chr(c)
print(r)
    
    
    
