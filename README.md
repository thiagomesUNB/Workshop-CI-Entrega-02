# Trabalho Individual 02 2021.1

A Gestão de Configuração de Software é parte fundamental no curso de GCES, e dominar os conhecimentos de configuração de ambiente, containerização, virtualização, integração e deploy contínuo tem se tornado cada vez mais necessário para ingressar no mercado de trabalho.

Para exercitar estes conhecimentos, você deverá aplicar os conceitos estudados ao longo da disciplina no produto de software contido neste repositório.

O sistema se trata de uma aplicação Web em Typescript, que é composta de:

- Front-end escrito em React (`chat-app`);
- Back-end dividido em três microsserviços:
  - `users-service`: express + ORM
  - `chat-service`: não implementado
  - `api-gateway`: graphql
- 2 Bancos de Dados MySQL 5.7.20 para users-service e chat-service (mesmo este não tendo sido implementado ainda)
  - `phpmyadmin`, como interface para gerenciamento dos bancos de dados

Para executar a aplicação em sua máquina, basta seguir o passo-a-passo descrito no arquivos README das pastas.

- [users-service](./trabalho_individual/users-service/README.md)
- [chat-service](./trabalho_individual/chat-service/README.md).
- [api-gateway](./trabalho_individual/api-gateway/README.md).
- [chat-app](./trabalho_individual/chat-app/README.md).
- [phpmyadmin](./trabalho_individual/phpmyadmin/README.md).

## Critérios de avaliação

### 1. Integração Contínua (CI)

A aplicação ja deverá ter seu ambiente completamente containerizado. Desta forma, cada subsistema (Front-end, Back-end e Banco de Dados) deverá ser isolado em um container individual.

Deverá ser utilizado uma ferramenta de Integração Contínua para garantir o build, os testes e os deploy para o [Docker Hub](https://hub.docker.com) dos serviços principais (chat-app, api-gateway, chat-service e users-service).

Para realizar esta parte do trabalho, deverá ser utilizado a ferramenta [GitLab-CI](https://docs.gitlab.com/ee/ci/).

## Nota

A nota de cada aluno será a soma dos itens abaixo que serão avaliados tanto de forma quantitativa (se foi realizado a implementação + documentação), quanto qualitativamente (como foi implementado, entendimento dos conceitos na prática, complexidade da solução). Faça os commits atômicos, bem documentados, completos a fim de facilitar o entendimento e avaliação do seu trabalho. Lembrando que esse trabalho é individual.

Os Itens de avaliação são (cada item tem peso 2 na nota final de 0 - 10):

1. Integração Contínua

- Integração com o GitLab para a utilização do CI
- Pelo menos 2 stages (build e test)
- Fazer o build dos 4 serviços principais
- Fazer o teste dos 4 serviços principais
- Fazer o deploy dos 4 serviços principais para o hub do docker