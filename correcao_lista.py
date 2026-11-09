lista = ["Ana", "Carlos", "Pedro"]

nome_incorreto = input("Digite o nome incorreto: ")

if nome_incorreto in lista:
    nome_correto = input("Digite o nome correto: ")
    posição = lista.index(nome_incorreto)
    lista.insert(posição, nome_correto)
    lista.remove(nome_incorreto)
    print(f"\nO nome {nome_incorreto} foi substituído por {nome_correto}.")
    print("Lista atualizada: ", lista)
else:
    print(f"\nNome {nome_incorreto} não encontrado na lista.")


# Corrigindo posições na lista de uma corrida de atletismo

# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

# Exemplo de Entrada:

# Digite o nome incorreto: Carlos
# Digite o nome correto: João

# Saída esperada:

# O nome Carlos foi substituído por João.
# Lista atualizada: ['Ana', 'João', 'Pedro']
