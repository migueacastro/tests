FROM node:21.7.3-alpine

ENV NODE_ENV development

WORKDIR /app
COPY ["package.json", "package-lock.json", "yarn.lock", "./"]

RUN yarn
COPY . .
EXPOSE 3000
EXPOSE 24678
