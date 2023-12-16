from raspagem_beautifulsoup import captura_informacao_tabela_seminario_graduacao
from banco_dados import BancoDiscordia
from bot_site import BotSite
from config import TEMPO_ESPERA, TEMPO_ESPERA_ENTRE_POSTAGENS
from time import sleep



if __name__ == '__main__':

    bd = BancoDiscordia()
    bot_site = BotSite()
    bd.inicia_banco()

    while True:
         # postagens dos seminarios da graduaçao salvas no banco
        postagens_seminario_graduacao_banco = bd.busca_postagens_graduacao()
        urls_seminario_graduacao = [postagem[2] for postagem in postagens_seminario_graduacao_banco]
        
        
         # captura todas as postagens da tabela de seminários da graduação, exceto as que foram passadas por parametro
        postagens_seminario_graduacao_a_salvar = captura_informacao_tabela_seminario_graduacao(urls_seminario_graduacao)

         # insere as postagens novas de seminários da graduação no banco, a adiciona a lista com as postagens recentes que ja haviam no banco
        if postagens_seminario_graduacao_a_salvar:
            [bd.insere_postagem_graduacao(postagem) for postagem in postagens_seminario_graduacao_a_salvar]
            postagens_seminario_graduacao_banco.extend(postagens_seminario_graduacao_a_salvar)

        postagens = postagens_seminario_graduacao_banco


        # processa as postagens que ainda nao foram processadas
        for postagem in postagens:
            processado = postagem[4]
            if processado == 0:
                bot_site.processa_post_site(postagem)
                sleep(TEMPO_ESPERA_ENTRE_POSTAGENS)
            


        sleep(TEMPO_ESPERA)
    
    
    
   


    