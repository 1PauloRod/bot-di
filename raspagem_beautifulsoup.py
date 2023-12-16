import datetime
import re
from io import BytesIO
from time import sleep

from PIL import Image
import requests
from bs4 import BeautifulSoup

from config import SITE_DI, CANAIS_AVISOS_TESTE, TEMPO_ESPERA_SALVAR_IMG, SITE_SEMINARIO_GRADUACAO
from utils import converte_data_post, remove_acentos_string

"""
    Módulo para realizar a raspagem de postagens do site do DI usando BeautifulSoup.
"""


'''def identifica_canal(titulo_post: str) -> int:
    """
        Identifica o canal do Discord em que a postagem será publicada com base no título.

        :param
            titulo_post (str): O título da postagem.

        :return
            int: O ID do canal do Discord.
    """
    if (("seminário" in titulo_post or "defesa" in titulo_post) and
            ("mestrado" in titulo_post or "doutorado" in titulo_post)):
        return CANAIS_AVISOS_TESTE["defesas_mestrado_doutorado"]
    elif "seminário" in titulo_post and "graduação" not in titulo_post:
        return CANAIS_AVISOS_TESTE["seminarios_pos"]
    elif "seminário" in titulo_post and "graduação" in titulo_post and "pós" not in titulo_post:
        return CANAIS_AVISOS_TESTE["seminarios_graduacao"]

    return CANAIS_AVISOS_TESTE["aviso_gerais"]


def captura_postagens_site(urls_ignorar: list[str] = None, baixar_imagens: bool = True) -> list[list]:
    """
        Captura todas as postagens da página principal do site do DI, exceto as que foram passadas por parâmetro.

        :param
            urls_ignorar (list[str], optional): Lista de URLs a serem ignoradas. Padrão é None.
            baixar_imagens (bool, optional): Define se as imagens devem ser baixadas. Padrão é True.

        :return
            list[list]: Uma lista contendo listas com os dados de cada postagem capturada.
    """
    if not urls_ignorar:
        urls_ignorar = []

    postagens_capturadas = []
    html_texto = requests.get(SITE_DI).text
    soup = BeautifulSoup(html_texto, 'lxml')
    cards_imagem = soup.find_all('div', class_="card-noticia col")

    for post in cards_imagem:
        imagem = post.find('img')
        link = post.find('a')

        if link and 'href' in link.attrs:
            url_post = link['href']

            if url_post not in urls_ignorar:
                processado = 0
                id_mensagem = 0
                titulo_post = post.find('div', class_='titulo-noticia').text.strip().lower()
                data_post = converte_data_post(post.find('div', class_='date').text)
                id_canal_post = identifica_canal(titulo_post)
                id_postagem = re.findall(r'/(.*?)/', url_post)[-1] \
                    if re.findall(r'/(.*?)/', url_post) else None
                if imagem and baixar_imagens:
                    img_url = imagem['src']
                    img_response = requests.get(img_url)
                    if img_response.status_code == 200:
                        img = Image.open(BytesIO(img_response.content))
                        nome_arq = id_postagem.replace('-', '_')
                        dir_img = rf"{nome_arq}.png"
                        img.save(dir_img)
                        sleep(TEMPO_ESPERA_SALVAR_IMG)  # espera para imagem ser baixada

                postagens_capturadas.append([id_postagem, processado, url_post, id_canal_post, id_mensagem, data_post])

    return postagens_capturadas'''

def captura_informacao_tabela_seminario_graduacao(urls_ignorar: list[str] = None) -> list[list]:
    """
           Captura todas as postagens ta tabela de seminários de graduação do site do DI, exceto as que foram passadas por parâmetro.

           :param
               urls_ignorar (list[str], optional): Lista de URLs a serem ignoradas. Padrão é None.

           :return
               list[list]: Uma lista contendo listas com os dados de cada postagem capturada.
       """
    if not urls_ignorar:
        urls_ignorar = []

    postagens_capturadas = []
    id_canal_post = CANAIS_AVISOS_TESTE["seminarios_graduacao"]

    html_texto = requests.get(SITE_SEMINARIO_GRADUACAO).text
    soup = BeautifulSoup(html_texto, 'html.parser')
    tabela = soup.find('tbody')
    linhas = tabela.find_all('tr')
    for i in range(1, len(linhas)):
        td = linhas[i].find_all('td', {'dir': 'ltr'})
        a_tags = td[1].find_all('a')
        for a_tag in a_tags:
            url = a_tag.get('href').replace("%3D", "=")
            match = re.search(r'http[s]?://(?:www\.)?youtube\.com/watch\?v=[^&]+', url)
            if match:
                url_post = match.group()

                if url_post not in urls_ignorar:
                    processado = 0
                    id_mensagem = 0
                    data = td[0].text.replace('.', "").split('/')
                    dia = data[0]
                    mes = data[1]
                    ano = datetime.datetime.now().year
                    data_post = converte_data_post("quinta-feira, {} de {} de {} às 18:00".format(dia, mes, ano))
                    postagem = re.match(r'^(.*?)( - .*)?$', td[1].text)
                    palestrante = postagem.group(1).strip().replace(" ", "-").replace(".", "")
                    descricao = postagem.group(2).strip(" -").replace(" ", "-").replace(",", "").replace('"', '')
                    id_postagem = remove_acentos_string(descricao) + "-" + remove_acentos_string(palestrante)
                    postagens_capturadas.append([id_postagem, processado, url_post, id_canal_post, id_mensagem, data_post])

    return postagens_capturadas




