# Koa

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Comandos](#comandos)
- [Docs Externos](#docs)
- [License](#license)
- [Fonte](#fonte)

## Pré-requisitos

- Node v12+
- Postgres v10+
- Docker

## **Instalação**

1.  **Local**

    ```
    git clone <url>

    cd koa-boilerplate

    npm install

    npm run build
    ```

2.  **Environment e configuração do DB**

    Adicione o arquivo .env na raiz do projeto com a seguintes variaveis de ambiente. 

    ```
    NODE_ENV=development
    PORT=3000
    SECRET=foobar
    TYPEORM_CONNECTION=postgres
    TYPEORM_URL=postgres://postgres:Password1@localhost:5432/postgres
    TYPEORM_ENTITIES=build/src/entities/*.js
    TYPEORM_MIGRATIONS=build/migrations/*.js
    TYPEORM_MIGRATIONS_TABLE_NAME=migrations
    TYPEORM_MIGRATIONS_DIR=migrations
    ```

    Rode as migrações usando o TypeORM:

    ```
    npx typeorm migration:run
    ```

3.  **Rodar localmente**

    Para rodar a aplicação locamente:

    ```
    npm run start:dev
    ```

    Runs:

    - Build
    - Linting
    - Unit Tests
    - Docker Build
    - Integration Tests

4.  **Testes**

    Para rodar os testes, utilize o comando:

    ```
    npm run unittest
    ```

## **Comandos**

1.  **npm scripts**

    ```
    npm run <command>
    ```

    - `start:dev` Run typescript files directly using nodemon and tsnode. Detects changes and automatically restarts server
    - `build` Runs tsc to compile the app. Files are emitted to /build.
    - `eject` Removes example code
    - `lint` Checks for linting errors using ESLint configuration
    - `unittest` Run jest unittests with code coverage
    - `unittest:watch` Detects changes and automatically re-runs tests
    - `docker:up` Standup the dockerize app, a postgres docker image and a migration image that migrates the db
    - `docker:down` Teardown the docker containers
    - `inttest` Run integration tests against the docker images
    - `inttest:watch` Run integration tests and watch for changes
    - `commit` Runs the previouse commands to verify changes before commit. This command also runs in the pipeline

2.  **typeorm scripts**

    All TypeORM commands run on the configuration information specified in the .env folder.
    See [TypeORM CLI Docs](https://github.com/typeorm/typeorm/blob/master/docs/using-cli.md)

    ```
    npx typeorm <command>
    ```

    - `migration:run` Apply any reminaing migrations to the db specified in
    - `migration:revert` Revert the most recent migration applied
    - `migration:show` Show all migrations with status
    - `migration:generate -n migrationNameHere` Compare entities to current db schema and generate migration with changes
    - `migration:create -n migrationNameHere` Create a new migration

## **Docs**

- [Koa](https://devdocs.io/koa/)
- [Typescript](https://www.typescriptlang.org/docs/home)
- [TypeORM](https://github.com/typeorm/typeorm/tree/master/docs)
- [Awilix-Koa](https://github.com/jeffijoe/awilix-koa)
- [Docker](https://docs.docker.com)
- [Hapi/Joi](https://github.com/hapijs/joi/blob/master/API.md)
- [EsLint](https://eslint.org/docs/user-guide/configuring)
- [Sinon](https://sinonjs.org/releases/latest/)
- [Supertest](https://www.npmjs.com/package/supertest)

## **License**

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © Evan Gordon Fleming.

## **Fonte**

O repositório original desse serviço pode ser encontrado [aqui](https://github.com/gothinkster/realworld)
