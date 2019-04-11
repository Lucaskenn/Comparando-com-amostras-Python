listadeamostras = []

#pedindo para o usuário colocar uma amostra para o programa

ipt = input("Digite o valor das amostras ou 'comparar':")
listadeamostras.append(ipt)



#repetindo o processo até o usuário digitar "amostrar" 
while ipt != "comparar":
    ipt = input("Digite o valor das amostras ou 'comparar':")
    listadeamostras.append(ipt)


#o que acontece se ele digitar "amostrar"

if ipt == "comparar":

    #criando um contador para registrar o números de elementos da lista

    contador = 0

    for y in listadeamostras :
        contador = contador + 1


    #comparando os 2 primeiros elementos da lista para definir um maior e o menor inicial

    if listadeamostras[0] > listadeamostras[1]:
        maior = listadeamostras[0]
        menor = listadeamostras[1]

    else:
        maior = listadeamostras[1]
        menor = listadeamostras[0]


    #começando do terceiro elemento, comparando com o anterior e substituindo na variavel maior e menor

    for x in range (2, contador-1):
        if maior < listadeamostras[x]:
            maior = listadeamostras[x]
        
    for x in range (2,contador-1):
        if menor > listadeamostras[x]:
            menor = listadeamostras[x]

    #pedindo um valor para comparar com o maior e menor valor da lista

    valor = int(input("Digite um valor para comparar:"))



    if valor <= int(maior) and valor >= int(menor):
        print("O valor está no intervalo dos valores da amostra")

    else:
        print("O valor não está no intervalo dos valores da amostra")
        




