def NomeMaiorNota( resultado, alunos):
    posicao=1
    notaMaior=resultado[0]
    while posicao<len(resultado):
        if notaMaior[4]<resultado[posicao][4]: notaMaior=resultado[posicao]
        posicao+=1
    
    RA = notaMaior[0]

    posicao=0
    while posicao<len(alunos):
        if alunos[posicao][0] == RA:
            return alunos[posicao][1]
        posicao+=1
