from datetime import datetime

import unicodedata

from config import DIC_MESES_STR_NUM


def converte_data_post(data_post_str: str) -> datetime:
    """
        Converte a string da data capturada do site em um objeto datetime.

        :param
            data_post_str (str): A string da data.

        :return
            datetime: A data convertida.
    """
    dia, mes, ano, horario = data_post_str.split(" ")[1::2]
    hora, minuto = horario.split(":")
    mes = DIC_MESES_STR_NUM[mes.lower()]
    return datetime(day=int(dia), month=mes, year=int(ano), hour=int(hora), minute=int(minuto))

def remove_acentos_string(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

