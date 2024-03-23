def insertionSort (A):
    j = 1 #Como o insert sorte compara com o anterior o inicio do loop precisa ser um valor a frete do inicial
    chave = A[j]# Armazena o valor atual que irá ser ordenado
    for j in range (len(A)):
        i = j - 1 #i é o indice anterior que será utilizado para compara a sequência
        while i >= 0 and A[i] > chave: #Implementa as duas condições de parada do insetion sort que são o elemento chave ser o menor elemento da sequência ou ser maior que o elemento anerior
            A[i+1] = A[i] ##Atualiza o maior valor comparado até o momento
            i = i-1 #Movimenta o valor de comparação do vetor e possibilita o encerramento do while
        A[i+1] = chave #Como sempre ao final da interação do while subtrai-se 1 de i temos que somar 1 ao sair para que o posicionamento seja que gerou a saida ou o primeiro elemento da lista
    return A
    