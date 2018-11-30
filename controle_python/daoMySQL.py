import pymysql as mysql
from configMySQL import config_mysql


def gravar_operacao(tipo_controle, operacao_realizada):
    try:
        db=mysql.connect(host=config_mysql.servidor_mysql,
                         user=config_mysql.login_mysql,
                         port=int(config_mysql.porta_banco),
                         passwd=config_mysql.senha_mysql,
                         db=config_mysql.nome_banco,
                         autocommit=True)
        
        cursor = db.cursor()

        cursor.execute("INSERT INTO historico_operacoes (tipo_controle, acao_executada) VALUES ('" + tipo_controle + "', '" +  operacao_realizada + "')")
    except Exception as e:
        print('Nao foi possivel gravar a operacao realizada.\nErro: ' + str(e))
    finally:
        db.close()


def listar_operacoes_realizadas():
    try:
        db=mysql.connect(host=config_mysql.servidor_mysql,
                         user=config_mysql.login_mysql,
                         port=int(config_mysql.porta_banco),
                         passwd=config_mysql.senha_mysql,
                         db=config_mysql.nome_banco,
                         autocommit=True)
        
        cursor = db.cursor()

        cursor.execute("SELECT * FROM historico_operacoes")

        listagem = cursor.fetchall()

        print('\nItens gravados em banco')
        print('---------------------------------------------------------------------------------------------------------------')

        for itens in listagem:
            print('Tipo Controle: ' + itens[1] + ' - Acao Executada: ' + itens[2] + ' - Data Operacao: ' + str(itens[3]))

        print('---------------------------------------------------------------------------------------------------------------')
    except Exception as e:
        print('Nao foi possivel consultar as operacaoes realizadas.\nErro: ' + str(e))
    finally:
        db.close()
