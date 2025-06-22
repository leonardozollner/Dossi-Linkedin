import logging
import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict, Any

def scrape_linkedin_profile(url: str) -> Optional[Dict[str, Any]]:
    """
    Raspa os dados de um perfil do LinkedIn.

    Args:
        url (str): A URL do perfil do LinkedIn.

    Returns:
        dict: Um dicionário com os dados extraídos.
    """
    logging.info(f"Iniciando scraping da URL: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        nome_tag = soup.find('h1', class_='text-heading-xlarge')
        cargo_atual_tag = soup.find('div', class_='text-body-medium')
        resumo_tag = soup.find('div', class_='display-flex ph5 pv3')

        dados_extraidos = {
            "nome": nome_tag.get_text(strip=True) if nome_tag else "Não encontrado",
            "cargo_atual": cargo_atual_tag.get_text(strip=True) if cargo_atual_tag else "Não encontrado",
            "resumo": resumo_tag.get_text(strip=True) if resumo_tag else "Não encontrado",
            # Adicionar a extração de outras seções aqui (experiência, formação, etc.)
            # Esta é uma implementação básica e pode precisar de ajustes dependendo da estrutura do HTML do LinkedIn
        }
        
        logging.info("Scraping concluído com sucesso.")
        return dados_extraidos
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Erro de HTTP: {http_err}")
        if response.status_code == 429:
            logging.warning("Recebemos um status 429 (Too Many Requests). O LinkedIn pode ter bloqueado o scraping.")
            # Implementar fallback com busca no Google aqui
        return None
    except Exception as e:
        logging.error(f"Ocorreu um erro durante o scraping: {e}")
        return None

def search_google_for_linkedin_url(person_name: str) -> Optional[str]:
    """
    Busca no Google por um perfil do LinkedIn e retorna a primeira URL encontrada.

    Args:
        person_name (str): O nome da pessoa a ser buscada.

    Returns:
        str: A URL do perfil do LinkedIn encontrada.
    """
    logging.info(f"Buscando perfil de '{person_name}' no Google...")
    
    search_query = f"site:linkedin.com/in/ {person_name}"
    google_url = f"https://www.google.com/search?q={search_query}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(google_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra o primeiro link que parece ser de um perfil do LinkedIn
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and "linkedin.com/in/" in href and href.startswith("/url?q="):
                linkedin_url = href.split("/url?q=")[1].split("&sa=")[0]
                logging.info(f"Perfil do LinkedIn encontrado: {linkedin_url}")
                return linkedin_url
                
        logging.warning(f"Nenhum perfil do LinkedIn encontrado para '{person_name}' no Google.")
        return None
        
    except Exception as e:
        logging.error(f"Ocorreu um erro ao buscar no Google: {e}")
        return None 