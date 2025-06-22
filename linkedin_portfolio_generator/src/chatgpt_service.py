import openai
import os
import logging
from dotenv import load_dotenv
from typing import Dict, Any

def configure_openai():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("A chave da API da OpenAI não foi encontrada. Verifique seu arquivo .env.")

def gerar_portfolio_com_chatgpt(dados_extraidos: Dict[str, Any]) -> str:
    """
    Envia os dados extraídos para o ChatGPT e gera um portfólio.

    Args:
        dados_extraidos (dict): Um dicionário com os dados do perfil.

    Returns:
        str: O texto do portfólio gerado.
    """
    logging.info("Enviando dados para a API da OpenAI...")
    
    prompt = f"""
    Você é um especialista em branding pessoal. Abaixo estão dados extraídos de um perfil profissional.
    Seu papel é transformar essas informações em um portfólio impactante, bem redigido, claro e com tom profissional.
    Estruture com seções como: "Sobre", "Experiência Profissional", "Formação", "Habilidades", "Idiomas", "Atividades Voluntárias", e "Resumo Final".

    Dados extraídos:
    {dados_extraidos}

    Por favor, gere o portfólio completo e bem formatado.
    """
    
    try:
        configure_openai()
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        
        portfolio_texto = response.choices[0].text.strip()
        logging.info("Portfólio gerado com sucesso.")
        return portfolio_texto
        
    except Exception as e:
        logging.error(f"Ocorreu um erro ao se comunicar com a API da OpenAI: {e}")
        return "Erro ao gerar o portfólio." 