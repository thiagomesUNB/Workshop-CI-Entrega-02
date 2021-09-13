# Trabalho Individual 02 2021.1

A Gerência de Configuração de Software é parte fundamental da disciplina de GCES (Gerência de Configuração e Evolução de Software) e, dominar os conhecimentos de configuração de ambiente, containerização, virtualização, integração e deploy contínuo tem se tornado cada vez mais necessário para ingressar no mercado de trabalho.

Para exercitar estes conhecimentos, você deverá aplicar os conceitos estudados ao longo da disciplina no produto de software contido neste repositório.

O sistema se trata de uma aplicação Web em NextJs e um backend em Koa, que é composta de:

- Front-end escrito em NextJs;
- Back-end escrito em Koa;
- 1 Banco de Dados Postgres.

## Execução

Para executar a aplicação em sua máquina, basta seguir o passo-a-passo a seguir:

Para subir todos os serviços deste projeto:

```docker
docker-compose up
```

Para rodar os testes do frontend:

```docker
docker-compose run --entrypoint "npm run test" frontend
```

Para rodar os testes do backend:

```docker
docker-compose run --entrypoint "npm run unittest" backend
```

Já para executar cada componente separado, basta seguir o passo-a-passo descrito no arquivos README das pastas:

- [frontend](./frontend/README.md).
- [backend](./backend/README.md).

## Critérios de avaliação

### 1. Integração Contínua (CI)

A aplicação já deverá ter seu ambiente completamente containerizado. Desta forma, cada subsistema (Front-end, Back-end e Banco de Dados) deverá ser isolado em um container individual.

Deverá ser utilizada uma ferramenta de Integração Contínua para garantir o build, os testes e os deploy para o [Docker Hub](https://hub.docker.com) dos serviços principais (chat-app, api-gateway, chat-service e users-service).

Para realizar esta parte do trabalho, deverá ser utilizado a ferramenta [GitLab-CI](https://docs.gitlab.com/ee/ci/).

## Nota

A nota de cada aluno será a soma dos itens abaixo que serão avaliados tanto de forma quantitativa (se foi realizado a implementação + documentação), quanto qualitativamente (como foi implementado, entendimento dos conceitos na prática, complexidade da solução). Faça os commits atômicos, bem documentados, completos a fim de facilitar o entendimento e avaliação do seu trabalho. Lembrando que esse trabalho é individual.

Os Itens de avaliação são (cada item tem peso 2 na nota final de 0 - 10):

1. Integração Contínua

- Integração com o GitLab para a utilização do CI;
- Pelo menos 2 stages (build e test);
- Fazer o build dos 2 serviços principais;
- Fazer o teste dos 2 serviços principais;
- Fazer o deploy dos 2 serviços principais para o hub do docker.
