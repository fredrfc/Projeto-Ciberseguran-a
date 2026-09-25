from enum import Enum

#Enumeração para padronizar os tipos de ativos que são permitidos no sistema
class TipoAtivo(Enum):
    NOTEBOOK = 'Notebook'
    ROTEADOR = 'Roteador'
    SERVIDOR = 'Servidor'
    BANCO_DE_DADOS = 'Banco de dados'

#Enumeração para padronizar a escala de severidade para as vulnerabilidades
class Severidade(Enum):
    BAIXA = 'Baixa'
    MEDIA = 'Média'
    ALTA = 'Alta'
    CRITICA = 'Crítica'

#Enumeração para padronizar os status das vulnerabilidades
class Status(Enum):
    ABERTA = 'Aberta'
    EM_MANUTENCAO = 'Em manutenção'
    CORRIGIDA = 'Corrigida'
    ACEITA_COMO_RISCO = 'Aceita como risco'