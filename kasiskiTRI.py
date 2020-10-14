def kasisky (cadena):
    cads = []
    cads2 = []
    esp = []
    tam = len(cadena)
    for i in range(len(cadena)):
        tri = cadena[i:i+3]
        if(len(tri)==3):
            cads.append(tri)

    for i in range(len(cads)):
        contador = 0
        for j in range(i+1,len(cads)):
            if cads[i]==cads[j]:
                t = (cads[i],contador-2)
                cads2.append(t)
                contador = 0
            else:
                contador = contador + 1
                
    cads2=set(cads2)
    distancias =[]
    for i in cads2:
       distancias.append(i[1])

    distancias=sorted(distancias)
    
    return distancias

    
            
                
                
        

s="MAXYHGAVAPUUGZHEGZQOWOBNIPQKRNÑMEXIGONIICUCAWIGCTEAGMNOLRSZJNLWÑAWWIGLDDZSNIZDNBIXGZLAYMXÑCVEKIETMOEOPBEWPTNIXCXUIHMECXLNOCECYXEQPBWUFANIICÑJIKISCZUAILBGSOANKBFWUAYWNSCHLCWYDZHDZAQVMPTVGFGPVAJWFVPUOYMXCWERVLQCZWECIFVITUZSNCZUAIKBFMÑALIEGLBSZLQUXÑOHWOCGHNYWÑQKDANZUDIFOIMXNPHNUWQOKLMVBNNKRMKONDPDPNMIKAWOXMEEIVEKGBGSFHVADWPGOYMHOIUEEIPGOLENZBSCHAGKQTZDRÑMÑNWTUZIÑCMÑAXKQUWDLVANNIHLÑCQNWGEHIPGZDTZTÑNWÑEEWFUMGIÑXNTWXNVIXCZOAZSOQUVENDNFWUSZYHGLRACPGGUGIYWHOTRMZUGQQDDZIZFWHVVSHCUGOGIFKBXAXPBOBRDVDUCMVTKGIKDRSZLUQSDVPMXVIVEYMFGTEANIMQLHLGPQOHRYWCFEWFOISNÑPUAYINNÑXNÑPGKWGOILQGAFOILQTAHEIIDWMÑEÑXNEPRCVDQTURSK"
    
v=kasisky(s)
print(v)
                
