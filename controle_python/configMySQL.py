import configparser

class config_mysql:
    servidor_mysql = None
    nome_banco = None
    porta_banco = 0
    login_mysql = None
    senha_mysql = None

def carregar_ini():
    try:
        print('Carregando arquivo ini....')

        arquivo_ini = configparser.ConfigParser()
        
        arquivo_ini.read("config.ini")
        dados_ini = arquivo_ini['banco']

        config_mysql.servidor_mysql = dados_ini['servidor']
        config_mysql.nome_banco = dados_ini['banco']
        config_mysql.porta_banco = dados_ini['porta']
        config_mysql.login_mysql = dados_ini['usuario']
        config_mysql.senha_mysql = dados_ini['senha']

        print('\nDados Conexao MySQL')
        print('---------------------')
        print(config_mysql.servidor_mysql)
        print(config_mysql.nome_banco)
        print(config_mysql.porta_banco)
        print(config_mysql.login_mysql)
        print(config_mysql.senha_mysql)
        print('---------------------\n')
    except Exception as e:
        print('Nao foi possivel carregar o arquivo ini de configuracao do banco mysql.\nErro: ' + str(e))

