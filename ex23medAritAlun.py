def AlunosMediArit(aluno, resultado, valorDado):
    nomes = []

    posicao_aluno=0
    while posicao_aluno<len(aluno):
        RA_atual = aluno[posicao_aluno][0]

        soma = 0
        quantidade = 0
        posicao_resultado = 0
        while posicao_resultado < len(resultado):
            if resultado[posicao_resultado][0] == RA_atual:
                soma= soma + resultado[posicao_resultado][4]
                quantidade = quantidade + 1
            posicao_resultado +=1

        mediaArit = soma /quantidade
        if mediaArit==valorDado:
            nomes.append(aluno[posicao_aluno][1])
        posicao_aluno+=1
    return nomes