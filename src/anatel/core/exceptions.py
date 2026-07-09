"""
Hierarquia de exceções da Anatel Data Platform.

Todas as exceções personalizadas da plataforma devem herdar de
AnatelError.
"""


class AnatelError(Exception):
    """Classe base para todas as exceções da plataforma."""


# ==========================================================
# DOWNLOAD
# ==========================================================

class DownloadError(AnatelError):
    """Erro ocorrido durante o download de arquivos."""


class InvalidUrlError(DownloadError):
    """URL inválida ou mal formada."""


class FileNotFoundDownloadError(DownloadError):
    """Arquivo não encontrado na URL informada."""


# ==========================================================
# EXTRAÇÃO
# ==========================================================

class ZipExtractionError(AnatelError):
    """Erro ao extrair arquivos ZIP."""


# ==========================================================
# LEITURA
# ==========================================================

class CsvReadError(AnatelError):
    """Erro durante a leitura de arquivos CSV."""


# ==========================================================
# EXPORTAÇÃO
# ==========================================================

class ExportError(AnatelError):
    """Erro ao exportar dados."""


# ==========================================================
# BANCO DE DADOS
# ==========================================================

class DatabaseError(AnatelError):
    """Erro relacionado ao banco de dados."""
