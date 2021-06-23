# build stage
FROM node:14.16.1-alpine as build-stage
WORKDIR /app/
COPY vue-ibay-front/package.json /app/
RUN npm cache verify
RUN npm install
COPY vue-ibay-front /app/
RUN npm run build

# production stage
FROM nginx:latest as production-stage
COPY vue-ibay-back/nginx/prod.conf /etc/nginx/nginx.conf
COPY vue-ibay-back/static /usr/src/app/static/
COPY vue-ibay-back/media /usr/src/app/media/
COPY --from=build-stage /app/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
