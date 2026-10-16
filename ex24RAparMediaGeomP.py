# # Dadas 3 listas de registros (listonas de listinhas), uma de cada tipo, escreva uma função 
# em Python que resulta quantos dígitos pares tem nos RAs dos alunos cuja média 
# geométrica das notas seja igual a um valor também dado. Retorne None em caso de 
# impossibilidade de produzir o resultado. Pode-se deixar de colocar como parâmetro a(s) 
# lista(s) que lhe parecer(em) sem utilidade no exercício.

def RAparcomMediaGeomPondNotas(alunos,resultado, ValorDado, P):
    contagem=0
    posicao_aluno=0

    while posicao_aluno<len(alunos):
        RA = alunos[posicao_aluno][0]

        elevada = 1
        somaPesos = 0
        posicao_resultado=0
        while posicao_resultado<len(resultado):
            if RA == resultado[posicao_resultado][0]:
                elevada = elevada * resultado[posicao_resultado][4] ** P[posicao_resultado]
                somaPesos = somaPesos + P[posicao_resultado]
            
            posicao_resultado+=1
        medGeoPond = elevada ** ( 1/somaPesos)
        if medGeoPond == ValorDado:
            RA = str(RA)
            posicao_digito = 0
            while posicao_digito < len(RA):
                digito = int(RA[posicao_digito])
                if digito % 2 == 0:
                    contagem +=1
                posicao_digito +=1    
                    
        posicao_aluno+=1
    return contagem

    