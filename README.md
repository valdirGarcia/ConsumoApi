# Projeto Python: Star Wars API

Este é um projeto idealizado como parte da avaliação da disciplina de Desenvolvimento Web 3 do terceiro semestre de 2023 na Faculdade de Tecnologia de
Araras (FATEC Araras). O projeto consiste em uma aplicação de linha de comando que interage com a API de Star Wars (SWAPI) para consultar informações 
sobre personagens, filmes e planetas do universo de Star Wars.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Se você ainda não o tem, pode baixá-lo em [python.org](https://www.python.org/downloads/).

Além disso, o código utiliza a biblioteca `requests`, que não está incluída na biblioteca padrão do Python. Você pode instalar a biblioteca usando o arquivo `requirements.txt` fornecido. Para fazer isso, execute o seguinte comando em seu terminal:

```bash
pip install -r requirements.txt
```

de o git clone 

```
git clone https://github.com/valdirGarcia/ConsumoApi.git
```

## Instalando as Dependências 

Navegue até a pasta do projeto clonado:

```
cd consumoApi
```

Agora, instale as dependências necessárias executando o seguinte comando em seu terminal:

```
pip install -r requirements.txt
```

## Executando o Cliente Star Wars API

Para iniciar o cliente Star Wars API, execute o seguinte comando:

```
python consumoApi.py
```
Isso abrirá o cliente e exibirá um menu de opções:

1. **Consulta de Dados de Personagem:** 
2. **Consulta de Dados de Filme:**
3. **Consulta de Dados de Planeta:** 
4. **Encerramento do Programa:**

Escolha uma opção digitando o número correspondente e pressione Enter. Siga as instruções na tela para fornecer o ID do personagem, filme ou planeta desejado. O cliente buscará as informações da API Star Wars e as exibirá na tela.

## Encerrando o Programa

Para encerrar o programa, basta escolher a opção "4".

Aproveite o cliente Star Wars API para explorar informações sobre o universo Star Wars! Se tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para abrir uma issue no repositório do GitHub.
