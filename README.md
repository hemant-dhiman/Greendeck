# Greendeck assignment

-`Download this repository`

-`drag and drop it in Docker` -`or` -`you can use online docker` -`https://labs.play-with-docker.com/`

## Unzip project in Docker

```
unzip Greendeck.zip
cd Greendeck
ls
```

## Docker command

```
FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python]
CMD ["app.py"]

```

## Building a DockerImage file

```
- `you are able to see all the files in the directory by ls command`
- `now run following commands`

- `sudo docker build --tag greendeck_1 .`
```

## Running the Dockerimage file

```
sudo docker run --name greendeck_1 -p 5000:5000 greendeck_1
```
