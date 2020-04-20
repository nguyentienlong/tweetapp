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

To remove old `tw33t` app if you see an error message `Cannot create container for service web: Conflict. The container name "/tw33t" is already in use`
```
docker rm tw33t
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
```
# from root dir of code base
cd ./web
yarn build
```
