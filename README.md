# LinkedIn Portfolio Generator

## 🚀 Objetivo do Projeto

Este projeto consiste em uma aplicação de linha de comando (CLI) que gera um portfólio profissional em formato PDF ou DOCX a partir do perfil do LinkedIn de um usuário. A aplicação extrai informações relevantes do perfil, utiliza a API da OpenAI para gerar um texto coeso e profissional, e formata o resultado em um documento final.

## 🔧 Funcionalidades

- **Extração de Dados do LinkedIn**: A aplicação pode receber o nome de uma pessoa ou a URL de seu perfil do LinkedIn para iniciar o processo de extração de dados.
- **Scraping Inteligente**: Utiliza técnicas de scraping para coletar informações como cargo atual, empresa, experiências passadas, formação acadêmica, habilidades, e mais.
- **Fallback de Busca**: Caso o scraping direto do LinkedIn seja bloqueado, a aplicação recorre a uma busca no Google para encontrar o perfil público.
- **Geração de Texto com IA**: Os dados extraídos são enviados para a API da OpenAI (ChatGPT), que gera um portfólio bem redigido e estruturado.
- **Exportação para PDF/DOCX**: O portfólio final é salvo em um arquivo `.pdf` ou `.docx` para fácil compartilhamento.
- **Interface de Linha de Comando**: Interação com o usuário através de uma CLI simples e intuitiva.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Web Scraping**: `requests`, `beautifulsoup4`, `selenium`
- **Interação com API**: `openai`
- **Geração de Documentos**: `python-docx`, `pdfkit`
- **Gerenciamento de Dependências**: `pip` e `requirements.txt`
- **Variáveis de Ambiente**: `python-dotenv`

## ⚙️ Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/leonardozollner/Dossi-Linkedin
    cd linkedin-portfolio-generator
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    - Renomeie o arquivo `.env.example` para `.env`.
    - Adicione sua chave da API da OpenAI ao arquivo `.env`:
      ```
      OPENAI_API_KEY=sua_chave_de_api_aqui
      ```

## ▶️ Como Usar

Para gerar um portfólio, execute o seguinte comando no terminal:

```bash
python src/main.py --url "url_do_perfil_do_linkedin"
```

Ou, para buscar por nome:

```bash
python src/main.py --nome "nome da pessoa"
```

O arquivo do portfólio gerado será salvo na raiz do projeto.

## 📄 Exemplo de Prompt para o ChatGPT

O prompt enviado para a API da OpenAI é estruturado da seguinte forma para garantir um resultado de alta qualidade:

```python
prompt = f"""
Você é um especialista em branding pessoal. Abaixo estão dados extraídos de um perfil profissional. Seu papel é transformar essas informações em um portfólio impactante, bem redigido, claro e com tom profissional. Estruture com seções como: "Sobre", "Experiência Profissional", "Formação", "Habilidades", "Idiomas", "Atividades Voluntárias", e "Resumo Final".

Dados extraídos:
{dados_extraidos}
"""
```

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões para melhorar este projeto, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. 
