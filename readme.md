# Tw33t

## How to run

Build the docker image and start server:

```
docker build -t cubicasa-developer-test .
docker-compose up web
```

Or
```
 docker-compose up --build 
```

Visit [http://localhost:8000/](http://localhost:8000/) for the app

## To view api document
Visit [http://localhost:8000/doc](http://localhost:8000/doc)

## To check the application log

```
tail -f app/logs/app.log    
```

## To start local dev (port :8080)
```
# from root dir of code base
cd ./web
yarn serve
```
Visit [http://localhost:8080](http://localhost:8080)


## To rebuild front end
```angular2html
# from root dir of code base
cd ./web
yarn build
```
