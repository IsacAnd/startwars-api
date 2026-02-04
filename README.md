# README - Arquitetura Técnica do Projeto Star Wars API

## Arquitetura Técnica - API Star Wars

### Visão Geral

Este projeto consiste em uma API desenvolvida em Python usando FastAPI, que consome dados da API pública do Star Wars (https://swapi.dev/). O objetivo é fornecer endpoints REST que permitam aos usuários consultar e filtrar dados relacionados a personagens, filmes, planetas, e outras informações do universo Star Wars.

A solução está planejada para ser implantada em ambiente Google Cloud Platform (GCP), utilizando os serviços **Cloud Functions** e **API Gateway** para exposição e gerenciamento da API.

### Componentes da Arquitetura

| Componente        | Descrição                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------|
| **Cliente**       | Aplicações ou usuários que consomem a API via HTTP, enviando requisições REST com filtros. |
| **API Gateway**   | Serviço gerenciado no GCP que expõe a API ao público, realiza autenticação e roteamento.   |
| **Cloud Functions** | Funções serverless onde roda a aplicação FastAPI, responsável pelo processamento da lógica, consumo da SWAPI e retorno dos dados filtrados e ordenados. |
| **API SWAPI**     | API pública externa que fornece dados do universo Star Wars.                                |

### Fluxo de Requisição

1. O **Cliente** realiza uma requisição HTTP para o endpoint da API, por exemplo, para consultar personagens ou filmes com filtros e ordenação.
2. O pedido passa pelo **API Gateway**, que valida autenticação via API Key e realiza roteamento.
3. O **API Gateway** encaminha a requisição para a **Cloud Function** que roda a aplicação FastAPI.
4. A função processa a requisição:
   - Valida parâmetros
   - Aplica filtros, ordenação, relacionamentos
   - Consulta a API externa SWAPI para obter dados, aplicando cache local para otimizar performance
5. A resposta formatada é devolvida para o **API Gateway**, que encaminha para o **Cliente**.

### Diagrama da Arquitetura

+------------+ +----------------+ +---------------------+ +------------+
| | HTTP | | HTTP | | HTTP | | | Cliente +--------->+ API Gateway +--------->+ Cloud Function +--------->+ SWAPI | | | | (Autenticação, | | (FastAPI - lógica, | | (Dados | | | | Roteamento) | | filtros, cache) | | Star Wars)|
+------------+ +----------------+ +---------------------+ +------------+

### Decisões Técnicas

- **Cloud Functions:** Escolhido para facilitar o deploy serverless, escalabilidade automática e cobrança por uso.
- **API Gateway:** Garante controle de acesso, autenticação simples via API Key e monitoramento.
- **FastAPI:** Framework moderno, rápido e eficiente para desenvolvimento de APIs em Python.
- **Consumo da SWAPI:** Os dados são consumidos sob demanda, com cache para reduzir chamadas e melhorar performance.
- **Filtros e Ordenação:** Permitidos via query params para flexibilidade nas consultas.
- **Autenticação:** Simples via token Bearer para segurança básica do endpoint.
- **Testes:** Unitários para garantir qualidade do código.
- **Documentação:** Swagger UI automático e README detalhado para uso e manutenção.

### Como Rodar Localmente

1. Clone o repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode a aplicação FastAPI localmente:

```bash
uvicorn app.main:app --reload
```

4. Acesse a documentação interativa em:

http://localhost:8000/docs
