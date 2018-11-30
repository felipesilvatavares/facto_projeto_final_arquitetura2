#encoding: utf-8

import serial
import sys
import time
import configMySQL
import daoMySQL


def main(porta_com):
    try:       
        menu_opcoes = '1 - Ligar Ar\n2 - Desligar Ar\n3 - Abrir Portao\n4 - Fechar Portao\n5 - Acender Luz\n6 - Desligar Luz\n7 - Listar Operacoes\n8 - Sair'
        opcao_escolhida = ''

        while (opcao_escolhida != 7):
            print(menu_opcoes)
            opcao_escolhida = (input("Digite o valor a ser enviado: "))
            executa_opcao_menu(opcao_escolhida, porta_com)
    finally:
        porta_com.close()


def executa_opcao_menu(opcao, porta_com):
    if (opcao == '1'):
        porta_com.write('ligarar'.encode())
        daoMySQL.gravar_operacao('Ar Condicionado','Ligar')
    elif (opcao == '2'):
        porta_com.write('desligarar'.encode())
        daoMySQL.gravar_operacao('Ar Condicionado','Desligar')
    elif (opcao == '3'):
        porta_com.write('abrirportao'.encode())
        daoMySQL.gravar_operacao('Portao','Abrir')
    elif (opcao == '4'):
        porta_com.write('fecharportao'.encode())
        daoMySQL.gravar_operacao('Portao','Fechar')
    elif (opcao == '5'):
        porta_com.write('acenderluz'.encode())
        daoMySQL.gravar_operacao('Luz','Acender')
    elif (opcao == '6'):
        porta_com.write('desligarluz'.encode())
        daoMySQL.gravar_operacao('Luz','Apagar')
    elif (opcao == '7'):
        daoMySQL.listar_operacoes_realizadas()
    elif (opcao == '8'):
        print('Aplicacao sera encerrada.')
        sys.exit(0)
    else:
        print('Opcao do menu invalida.')

porta_com = None

try:
    configMySQL.carregar_ini()

    porta_serial = (input("Informe a porta serial utilizada. Ex: COM0: "))
    porta_com = serial.Serial(porta_serial.upper(), 9600) 
    print('Iniciando comunicacao serial...\n')
    time.sleep(2)
except Exception as e:
    print('Nao foi possivel se conectar a porta informada. \nErro: ' + str(e))
    sys.exit(0)

main(porta_com)