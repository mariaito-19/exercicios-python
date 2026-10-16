def NomeDiscFreq(resultado,disciplina):
    posicao=1
    menorFreq = resultado[0]
    while posicao<len(resultado):
        if menorFreq[5]>resultado[posicao][5]: menorFreq=resultado[posicao]
        posicao+=1

    codigo = menorFreq[1]

    posicao=0
    while posicao<len(disciplina):
        if disciplina[posicao][0]==codigo:
            return disciplina[posicao][1]
        posicao+=1
