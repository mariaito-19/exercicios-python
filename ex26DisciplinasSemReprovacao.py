def DisciplinasqÑReprovaramAlunos(disciplina,resultado):
    nomes = []
    posicao_disciplina=0

    while posicao_disciplina<len(disciplina):
        codigDisc = disciplina[posicao_disciplina][0]

        posicao_resultado=0
        Reprovou=0
        while posicao_resultado<len(resultado):
            if codigDisc == resultado[posicao_resultado][1]:
                if resultado[posicao_resultado][4] < 5:
                    Reprovou +=1
            posicao_resultado+=1
        
        if Reprovou == 0:
            nomes.append(disciplina[posicao_disciplina][1])
        posicao_disciplina+=1
    return nomes

