FROM node:20

ENV DB_HOST=localhost
ENV DB_PORT=3308
ENV DB_USER=root
ENV DB_PASSWORD=secret
ENV DB_NAME=dictionary

WORKDIR /app
COPY package.json /app/
COPY yarn.lock /app/
COPY tsconfig.json /app/
COPY src/* /app/

RUN yarn install && \
  yarn tsc

CMD ["node", "dist/index.js"]