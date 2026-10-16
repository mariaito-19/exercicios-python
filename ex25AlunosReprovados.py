def ListaAlunosReprovados(alunos, resultado):
    nomes = []

    posicao_alunos = 0
    while posicao_alunos<len(alunos):
        RA = alunos[posicao_alunos][0]

        posicao_resultado=0
        while posicao_resultado<len(resultado):
            if resultado[posicao_resultado][0]==RA:
                if resultado[posicao_resultado][4] < 5:
                    if alunos[posicao_alunos][1] not in nomes:
                        nomes.append(alunos[posicao_alunos][1])
            posicao_resultado+=1
        posicao_alunos+=1
    return nomes