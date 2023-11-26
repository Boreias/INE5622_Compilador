import sys
sys.path.append('../..')

from reservados import *
from tabela_sintaxica import *
import time

def analise_lexica(codigo):
    elementos = []
    tipo = []
    texto = ''
    tabela_simbolos = dict()

    i = 0
    while i < len(codigo):
        if codigo[i] in NUMEROS or codigo[i] == '.':
            for j in range(i, len(codigo)):
                if codigo[j] in NUMEROS or codigo[j] == '.':
                    texto += codigo[j]
                else:
                    i = j - 2
                    break

            if texto.find('.') >= 0:
                tipo.append('float_constant')
            else:
                tipo.append('int_constant')

            elementos.append(texto)
            i = j + 1
        elif codigo[i] == '"':
            texto += '"'
            i += 1
            for j in range(i, len(codigo)):
                if codigo[j] != '"':
                    texto += codigo[j]
                else:
                    texto += '"'
                    break
            elementos.append(texto)
            tipo.append('string_constant')
            i = j + 1
        elif codigo[i] not in SIMBOLOS_RESERVADOS and codigo[i] != ' ' and codigo[i] != '\t' and codigo[i] != '\n' and codigo[i] != '.':
            for j in range(i, len(codigo)):
                if codigo[j] not in SIMBOLOS_RESERVADOS and (codigo[j] != ' ' or (j + 1 < len(codigo) and codigo[j:j+2] == ' [')) and codigo[j] != '\t' and codigo[j] != '\n' and codigo[j] != '.':
                    texto += codigo[j]
                else:
                    i = j - 2
                    break

            if texto.find(' ') >= 0:
                texto = texto[:texto.find(' ')]
            if texto.find('[') >= 0:
                texto = texto[:texto.find('[')]

            if texto in PALAVRAS_RESERVADAS:
                tipo.append(texto)
            else:
                tipo.append('ident')
                if texto not in tabela_simbolos.keys():
                    tabela_simbolos[texto] = 1
                else:
                    tabela_simbolos[texto] += 1

            elementos.append(texto)
            i = j
        else:
            if codigo[i] != ' ' and codigo[i] != '\t' and codigo[i] != '\n':
                if i+1 < len(codigo) and codigo[i+1] == '=':
                    tipo.append(codigo[i:i+2])
                    elementos.append(codigo[i:i+2])
                    i += 1
                else:
                    tipo.append(codigo[i])
                    elementos.append(codigo[i])
            i += 1
        texto = ''

    imprime_tabela_simbolos(tabela_simbolos)

    return tipo, elementos

def analise_sintaxica(entrada):
    pilha = ['$', 'PROGRAM']
    entrada.append('$')

    i = 0
    try:
        while len(pilha) > 0:
            while pilha[len(pilha) - 1] != entrada[i]:
                valor = pilha[len(pilha) - 1]
                pilha.pop()
                auxiliar = []

                for j in range(len(TABELA_SINTAXICA[valor][entrada[i]]) - 1, -1, -1):
                    auxiliar.append(TABELA_SINTAXICA[valor][entrada[i]][j])

                pilha += auxiliar

            pilha.pop()
            if i < len(entrada) - 1:
                i += 1
        return True

    except KeyError:
        print('Erro sintático')
        print('A pilha de derivações encontra-se atualmente da seguinte maneira:')
        print(pilha)
        print('O símbolo do analisador sintático que acarretou no problema é: ' + valor)
        print('O valor da entrada que deu problema é: ' + entrada[i])
        return False

def imprime_tabela_simbolos(tabela):
    print('Tabela de Símbolos:')
    for k in tabela.keys():
        print('O identificador ' + k + ' aparece ' + str(tabela[k]) + ' vez(s) no código')


if __name__ == '__main__':
    nome_arquivo = input('Digite o nome do arquivo a ser analisado: ')
    tempo_inicial = time.time()
    try:
        arquivo = open(nome_arquivo, 'r', encoding='utf-8')
        codigo = arquivo.read()

        tipo, elementos = analise_lexica(codigo)

        resultado = analise_sintaxica(tipo)

        if resultado:
            print('Código compilado')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    tempo_final = time.time()
    print('O tempo de compilação foi de ' + str((tempo_final - tempo_inicial)) + ' segundos')
