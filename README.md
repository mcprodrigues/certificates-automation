# Automação de Certificados com Python 💻

Este é um programa em Python para automatizar a transferência de dados de uma planilha Excel para preencher campos mutáveis em um certificado padrão.


## Requisitos

- **Python 3.x**
- **Bibliotecas Python**:
  - `openpyxl` para ler dados do Excel.
  - `Pillow` para manipulação de imagens.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/mcprodrigues/certificates-automation.git
    cd certificates-automation
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install openpyxl pillow
    ```

## Uso

1. Prepare a planilha com as seguintes colunas:
   - Nome
   - Curso
   - Participação
   - Carga Horária
   - Data de Emissão

2. Certifique-se de que o arquivo de imagem do certificado e as fontes necessárias estão no diretório correto.

3. Execute o script:

    ```bash
    python app.py
    ```

4. Os certificados gerados serão salvos no diretório atual com o nome formatado.

## Contribuições

Se você deseja contribuir para este projeto, siga estas etapas:

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/mcprodrigues/certificates-automation.git
    ```

2. **Crie uma Nova Branch**

    Crie uma nova branch para sua funcionalidade ou correção:

    ```bash
    git checkout -b feature/NOME
    ```

3. **Siga os Padrões de Commit**

    Certifique-se de seguir os padrões de commit estabelecidos para manter um histórico de mudanças claro e organizado.

4. **Abra um Pull Request**

    Abra um Pull Request (PR) no GitHub explicando o problema resolvido ou a funcionalidade adicionada. Se houver modificações visuais, anexe capturas de tela para ajudar na revisão.

5. **Aguarde a Revisão**

    Após abrir o Pull Request, aguarde a revisão e feedback. Estarei feliz em revisar suas contribuições!

## Licença

Este software está disponível sob as seguintes licenças:

- **[MIT](https://rem.mit-license.org/)**
