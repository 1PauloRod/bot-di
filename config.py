VERIFICA_BD_EXISTE = "SHOW DATABASES LIKE 'DIscordIA'"
CRIA_DB = "CREATE DATABASE DIscordIA"
CRIA_TABELA = [

   ["SHOW TABLES LIKE 'postagens_site'",
                                   "CREATE TABLE postagens_site("
                                   "postagem varchar(255) NOT NULL,"
                                   "processado bit DEFAULT 0,"
                                   "url varchar(255),"
                                   "canal_postado bigint NOT NULL,"
                                   "mensagem_id bigint NOT NULL,"
                                   "data_hora_postagem datetime,"
                                   "PRIMARY KEY (postagem))",
                                   'postagens_site'],

                                  ["SHOW TABLES LIKE 'postagens_graduacao'",
                                   "CREATE TABLE postagens_graduacao("
                                   "postagem varchar(255) NOT NULL,"
                                   "processado bit DEFAULT 0,"
                                   "url varchar(255),"
                                   "canal_postado bigint NOT NULL,"
                                   "mensagem_id bigint NOT NULL,"
                                   "data_hora_postagem datetime,"
                                   "PRIMARY KEY (postagem))",
                                   'postagens_graduacao']
     
     ]

SCRIPT_INSERE_POSTAGEM_GRADUACAO = '''
INSERT INTO DIscordIA.postagens_graduacao (postagem, processado, url, canal_postado, mensagem_id, data_hora_postagem)
VALUES ('%s', %d, '%s', '%d', '%d', '%s');
'''

SCRIPT_BUSCA_POSTAGEM_GRADUACAO = '''
SELECT * FROM DIscordIA.postagens_graduacao
WHERE postagem = '%s'
'''

SCRIPT_DELETA_POSTAGEM_GRADUACAO = "DELETE FROM DIscordIA.postagens_graduacao WHERE postagem = '%s'"

SCRIPT_ATUALIZA_POSTAGEM_GRADUACAO = '''
UPDATE DIscordIA.postagens_graduacao
SET
postagem = '%s',
processado = %d,
url = '%s',
canal_postado = %d,
mensagem_id = %d,
data_hora_postagem = '%s'
WHERE postagem = '%s';
'''

SCRIPT_BUSCA_POSTAGENS_GRADUACAO = '''
SELECT * FROM DIscordIA.postagens_graduacao
ORDER BY data_hora_postagem DESC
'''


# CREDENCIAIS BOT
TOKEN = 'MTEzMDYxNDQ2NzgyMzE0NDk3Mg.GzPCeU.KGb2GZeszlzsBJUhK5jZR0nxnYWca3KWSjJrDU'

# CANAIS DISCORD
CANAIS_AVISOS_TESTE = {'seminarios_graduacao': 1123260769497272457,
                       'seminarios_pos': 1123260769497272458,
                       'defesas_mestrado_doutorado': 1123260769497272459,
                       'aviso_gerais': 1123260769497272460}

WEBHOOKS_URL = {1123260769497272457: 'https://discord.com/api/webhooks/1154693111864373248'
                                     '/zMNuPuDKb_v38diWQHzb8O0ejAO1XC9hi_nOLsfXRGrUILSRoIIMZHei6Oz9995_p6zH',
                1123260769497272458: 'https://discord.com/api/webhooks/1154787437873209344'
                                     '/9sdy0Lu33cO4m6drbDboYOpriCd9ffCLDCzBF8VsIrhzeNCDd3Ew8fauAHR3TGzFbg4b',
                1123260769497272459: 'https://discord.com/api/webhooks/1154787694187118654/-WL-NwotJ'
                                     '-z_DCx1KH62kSjjIvJWcEEUtA9L6T5yXEQxnH5Wwjm9JpwyOJ8djLp2pqE3',
                1123260769497272460: 'https://discord.com/api/webhooks/1154788109700050954/Qo82UTq5fJkKcrs3vohImW7'
                                     '-MqOERvFIT9MsNt_f1TgSdKaHlctmvX7ioofGcIIZKFRz'}


# INFORMACOES SITE DI
SITE_DI = 'https://www.inf.puc-rio.br/'
SITE_SEMINARIO_GRADUACAO = "https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRojMQ1HPab3wWMpfvFQj8MGEycN-ZW7ti-od-ILi3FsptrJteqUuwVnwhLK_snQqIuvElzWvAYHmQh/pubhtml/sheet?headers=false&gid=417388442"


# MESES
DIC_MESES_STR_NUM = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
    "jan": 1,
    "fev": 2,
    "mar": 3,
    "abr": 4,
    "mai": 5,
    "jun": 6,
    "jul": 7,
    "ago": 8,
    "set": 9,
    "out": 10,
    "nov": 11,
    "dez": 12,
}

TEMPO_ESPERA = 60 * 10
TEMPO_ESPERA_ENTRE_POSTAGENS = 60 * 5
TEMPO_ESPERA_SALVAR_IMG = 5







