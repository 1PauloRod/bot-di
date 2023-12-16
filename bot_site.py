import os
from json import loads

from discord_webhook import DiscordWebhook
from config import WEBHOOKS_URL, CANAIS_AVISOS_TESTE
from banco_dados import BancoDiscordia


class BotSite:
    """
        Classe para publicar postagens do site no canal do Discord e atualizar o banco de dados.
    """

    def __init__(self):
        self.dados_postagem = None
        self.nome_arquivo = None

    def __deleta_imagem(self) -> None:
        """
            Deleta a imagem no diretório corrente, se existir.
        """
        diretorio = os.listdir()
        if self.nome_arquivo in diretorio:
            os.remove(self.nome_arquivo)
            print(f'O {self.nome_arquivo} foi removido.')
        else:
            print(f'{self.nome_arquivo} arquivo não existe')

    def __publica_post_site(self) -> None:
        """
            Publica a postagem do site no canal do Discord e deleta a imagem da postagem baixada, se houver.
        """
        id_postagem, processado, link_noticia, canal_id, mensagem_id, data_hora_postagem = self.dados_postagem
        self.nome_arquivo = f"{id_postagem.replace('-', '_')}.png"
        try:
            webhook = DiscordWebhook(url=WEBHOOKS_URL[canal_id])
            webhook.set_content(f'*Para mais informações, acesse:* {link_noticia}\n')

            # adiciona imagem se houver
            if self.nome_arquivo in os.listdir():
                with open(self.nome_arquivo, 'rb') as arq:
                    webhook.add_file(arq, 'imagem.png')
                    response = webhook.execute()
            else:
                response = webhook.execute()  # o webhook.execute tem que ser feito com a imagem aberta, caso ela exista

            if response.status_code == 200:
                response_content = response.content.decode().replace("'", '"')
                json_content = loads(response_content)
                mensagem_id = int(json_content['id'])
                processado = 1

                self.dados_postagem = [id_postagem, processado, link_noticia, canal_id, mensagem_id,
                                       data_hora_postagem]
            else:
                self.dados_postagem = None
        except Exception as ex:
            print(ex)
        finally:
            if self.nome_arquivo:
                self.__deleta_imagem()

    def processa_post_site(self, dados_postagem: list) -> int:
        """
            Processa uma postagem do site, publicando-a no canal do Discord e atualizando o banco de dados.

            :param
                dados_postagem (list): Os dados da postagem a ser processada.
        """
        try:
            self.dados_postagem = dados_postagem
            self.__publica_post_site()
            if self.dados_postagem:
                bd = BancoDiscordia()

                if self.dados_postagem[3] == CANAIS_AVISOS_TESTE['seminarios_graduacao']:
                    bd.atualiza_postagem_graduacao(self.dados_postagem)
                else:
                    bd.atualiza_postagem_site(self.dados_postagem)

            return 1
        except Exception as ex:
            print(ex)
            return -1


