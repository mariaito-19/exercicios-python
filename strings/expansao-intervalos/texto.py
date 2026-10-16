def expasao (txt):
    tamanho=len(txt)
    posicao=0

    while posicao<tamanho:
        if txt[posicao]=='-' and \
             posicao!=0 and \
             posicao!=tamanho-1 and \
             txt[posicao-1]<txt[posicao+1]:
             meio=''
             inicio=txt[posicao-1]
             final=txt[posicao+1]
             while True:
                 inicio=chr(ord(inicio)+1)
                 if inicio==final: break
                 meio+=inicio
             txt=txt[:posicao]+meio+txt[posicao+1:]
             tamanho+=(len(meio)-1)
             posicao+=(len(meio)+1)
        else:
            posicao+=1
    return txt

print("|"+expasao("  PROGRAMAR É PRECISO  VIVER  NÃO É PRECISO   ")+"|")

# aula do professor:
# def semEspacosSuperfluos(frase):
#     while frase[0]==" ":
#         frase= frase[1:]

#     while frase[len(frase)-1]==" ":
#         frase=frase[0:len(frase)-1]
    
#     posicao=0
#     while posicao<len(frase)-1:
#         if frase[posicao]==" " and\
#         frase[posicao+1]==" ":
#             frase=frase[0:posicao]+frase[posicao+1:]
#         else:
#             posicao+=1
#     return frase
# print("|"+semEspacosSuperfluos("  PROGRAMAR É PRECISO  VIVER  NÃO É PRECISO   ")+"|")
