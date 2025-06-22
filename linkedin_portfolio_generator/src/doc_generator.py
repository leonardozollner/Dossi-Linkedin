import logging
from docx import Document
import pdfkit
import os

def gerar_docx(texto: str, nome_arquivo: str):
    """
    Gera um arquivo .docx a partir de um texto.

    Args:
        texto (str): O conteúdo do documento.
        nome_arquivo (str): O nome do arquivo a ser salvo (sem extensão).
    """
    try:
        documento = Document()
        documento.add_paragraph(texto)
        caminho_arquivo = f"{nome_arquivo}.docx"
        documento.save(caminho_arquivo)
        logging.info(f"Documento DOCX salvo em: {caminho_arquivo}")
    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo DOCX: {e}")

def gerar_pdf(texto: str, nome_arquivo: str):
    """
    Gera um arquivo .pdf a partir de um texto.
    Nota: Requer a instalação do wkhtmltopdf no sistema.
    https://wkhtmltopdf.org/downloads.html

    Args:
        texto (str): O conteúdo do documento.
        nome_arquivo (str): O nome do arquivo a ser salvo (sem extensão).
    """
    try:
        # pdfkit pode precisar de um caminho para o executável do wkhtmltopdf
        # path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        # pdfkit.from_string(texto, f"{nome_arquivo}.pdf", configuration=config)
        
        caminho_arquivo = f"{nome_arquivo}.pdf"
        pdfkit.from_string(texto, caminho_arquivo)
        logging.info(f"Documento PDF salvo em: {caminho_arquivo}")
    except FileNotFoundError:
        logging.error("Erro ao gerar PDF: 'wkhtmltopdf' não encontrado.")
        logging.warning("Certifique-se de que o wkhtmltopdf está instalado e no PATH do sistema.")
        logging.warning("Download: https://wkhtmltopdf.org/downloads.html")
    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo PDF: {e}")

def gerar_documento_final(portfolio_texto: str, nome_base: str):
    """
    Gera os documentos finais (DOCX e PDF).

    Args:
        portfolio_texto (str): O texto do portfólio.
        nome_base (str): O nome base para os arquivos.
    """
    logging.info("Gerando documentos finais...")
    gerar_docx(portfolio_texto, nome_base)
    gerar_pdf(portfolio_texto, nome_base) 