import mysql.connector
from mysql.connector import errorcode
from config import VERIFICA_BD_EXISTE, CRIA_DB, CRIA_TABELA, SCRIPT_INSERE_POSTAGEM_GRADUACAO, SCRIPT_BUSCA_POSTAGEM_GRADUACAO, SCRIPT_DELETA_POSTAGEM_GRADUACAO, SCRIPT_ATUALIZA_POSTAGEM_GRADUACAO, SCRIPT_BUSCA_POSTAGENS_GRADUACAO
import datetime

class BancoDiscordia:

    def inicia_banco(self) -> list:
        
        try:
            self._cria_banco()

            for table in CRIA_TABELA:
                self._cria_tabela(table)

        except Exception as err:
            print(err)
            return [-5]
        

    def insere_postagem_graduacao(self, postagem) -> list:
        try:
            
            id_postagem, processado, url, canal_id, mensagem_id, data_hora_postagem = postagem
            script = SCRIPT_INSERE_POSTAGEM_GRADUACAO % (id_postagem, processado, url, canal_id, mensagem_id,
                                                    data_hora_postagem)

            return self.__executa_script(script)
        
        except Exception as err:
            print(err)
            return [-5]
        
        
    def busca_postagem_graduacao(self, postagem) -> list:
        try:
            
            script = SCRIPT_BUSCA_POSTAGEM_GRADUACAO % postagem

            return self.__executa_script(script)
        
        except Exception as err:
            print(err)
            return [-5]
        
    
    def busca_postagens_graduacao(self) -> list:
        """
            Busca as postagens mais recentes do site no banco de dados.

            :return
                list: As postagens mais recentes encontradas ou uma lista com código de erro.
        """
        try:
            script = SCRIPT_BUSCA_POSTAGENS_GRADUACAO
            return self.__executa_script(script)
        except Exception as ex:
            print(ex)
            return [-5]
        

    def deleta_postagem_graduacao(self, postagem) -> list:
        try:
           
            script = SCRIPT_DELETA_POSTAGEM_GRADUACAO % postagem
        
            return self.__executa_script(script)
        
        except Exception as err:
            print(err)
            return [-5]
        
    def atualiza_postagem_graduacao(self, dados_postagem: list) -> list:
        """
            Atualiza uma postagem no banco de dados.

            :param
                dados_postagem (list): Os novos dados da postagem.

            :return
                list: O resultado da operação ou uma lista com código de erro.
        """
        try:
            postagem, processado, url, id_canal_postado, id_mensagem, data_postagem = dados_postagem
            script = SCRIPT_ATUALIZA_POSTAGEM_GRADUACAO % (postagem, processado, url, id_canal_postado,
                                                      id_mensagem, data_postagem, postagem)
            return self.__executa_script(script)
        except Exception as ex:
            print(ex)
            return [-5]

   


    @staticmethod
    def _cria_banco() -> list:

        try:
            cnx = mysql.connector.connect(host='botdidb', 
                                            user='root', 
                                            password='discordia')
            
            cursor = cnx.cursor()

            cursor.execute(VERIFICA_BD_EXISTE)

            result = cursor.fetchall()

            print(result)

            if result:
                print("Banco de dados já existe.")
            else:
                print("Criando banco de dados.")
                cursor.execute(CRIA_DB)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu de errado com o usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            else:
                print(err)
                return [-3]
            
        finally:
            if cnx:
                cnx.close()


    @staticmethod
    def _cria_tabela(table) -> list:
        
        try:
            cnx = mysql.connector.connect(host='botdidb', 
                                          user='root', 
                                          password='discordia', 
                                          database='DIscordIA')
        
            cursor = cnx.cursor()

            cursor.execute(table[0])

            result = cursor.fetchall()

            if result:
                print("Tabela {} já existe.".format(table[2]))
            else:
                print("Criando tabela {}.".format(table[2]))
                cursor.execute(table[1])

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("algo deu errado com usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            else:
                print(err)
                return [-3]
        finally:
            if cnx:
                cnx.close()

    
    @staticmethod
    def __executa_script(script) -> list:
    
        try:
            cnx = mysql.connector.connect(host='botdidb', 
                                          user='root', 
                                          password='discordia', 
                                          database='DIscordIA')

            cursor = cnx.cursor()
            cursor.execute(script)
            result = cursor.fetchall()
            cnx.commit()

            return result
        except mysql.connector.Error as err:
            if cnx:
                cnx.rollback()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com usuário e senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            elif err.errno == errorcode.ER_BAD_TABLE_ERROR: 
                print("Tabela de dados não existe.")
                return [-3]
            else:
                print(err)
                return [-4]
        finally:
            if cnx:
                cnx.close()
        

