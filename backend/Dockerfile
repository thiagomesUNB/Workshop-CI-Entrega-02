FROM node:lts

RUN mkdir /app

WORKDIR /app

COPY package*.json /app/

RUN npm install
RUN npm i nodemon -g

COPY . /app

ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 3000
