def freqNome(L):
    if len(L)==0:
        return None
    else:
        posicao=1
        freqMenor=L[0]
        while posicao<len(L):
            if L[posicao][2]<freqMenor[2]: freqMenor=L[posicao]
            posicao+=1
        return freqMenor[0]
    
# Dada uma lista de registros (listona de listinhas), escreva uma função em Python que 
# resulta o nome da matéria com menor frequência. No caso da lista vir vazia, retorne None. 
# Assuma que não há mais de uma matéria com a mesma frequência, sendo esta a menor de 
# todas.
