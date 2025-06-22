import argparse
import logging
import sys
import os

# Adiciona o diretório raiz ao path para que os módulos possam ser importados
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import setup_logging
from src.scraper import scrape_linkedin_profile, search_google_for_linkedin_url
from src.chatgpt_service import gerar_portfolio_com_chatgpt
from src.doc_generator import gerar_documento_final

def main():
    """
    Função principal que orquestra a execução do programa.
    """
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Gerador de Portfólio a partir do LinkedIn.")
    parser.add_argument("--url", type=str, help="A URL do perfil do LinkedIn.")
    parser.add_argument("--nome", type=str, help="O nome da pessoa para buscar no Google.")
    
    args = parser.parse_args()
    
    if not args.url and not args.nome:
        logging.error("Você deve fornecer uma URL (--url) ou um nome (--nome).")
        return
        
    dados_extraidos = None
    if args.url:
        dados_extraidos = scrape_linkedin_profile(args.url)
    elif args.nome:
        url_encontrada = search_google_for_linkedin_url(args.nome)
        if url_encontrada:
            dados_extraidos = scrape_linkedin_profile(url_encontrada)
        else:
            logging.error(f"Não foi possível encontrar um perfil para '{args.nome}'.")
            return

    if not dados_extraidos:
        logging.error("Não foi possível extrair os dados. Encerrando o programa.")
        return
        
    portfolio_texto = gerar_portfolio_com_chatgpt(dados_extraidos)
    
    if portfolio_texto and "Erro" not in portfolio_texto:
        nome_base = dados_extraidos.get("nome", "portfolio").replace(" ", "_").lower()
        gerar_documento_final(portfolio_texto, nome_base)
        logging.info("Processo concluído com sucesso!")
    else:
        logging.error("Não foi possível gerar o portfólio. Verifique os logs para mais detalhes.")

if __name__ == "__main__":
    main() 