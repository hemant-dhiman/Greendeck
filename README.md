# Greendeck assignment

- `Download this repository`

- `drag and drop it in Docker`
 
- `or`
 
- `you can use online docker`(https://labs.play-with-docker.com/)

## Unzip project in Docker

```
unzip Greendeck.zip
cd Greendeck
ls
```

## Dockerfile content

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
- `you are able to see all the files in the directory by 'ls' command`
- `now run following commands`

- `sudo docker build --tag greendeck_1 .`
```

## Running the Dockerimage file

```
sudo docker run --name greendeck_1 -p 5000:5000 greendeck_1
```

# Format for CRUD operations

***CREATE Operation***
- method used
1. db.collection.insert_many({}) # for multiple records
2. db.collection.insert_one({}) # for single record

*format*
```json
{
    "_d" : "single digit integer value",
    "name": "name of e-commerce products (string value)",
    "brand_name": "name of the brand (string value)",
    "regular_price_value": "price of e-commerce products (integer value)",
    "offer_price_value": "offer price e-commerce products (integer value)",
    "currency": "currency type (string value)",
    "classification_l1": "class type e.g. baby & child (String value)",
    "classification_l2": "class type e.g. soft toys (String value)",
    "classification_l3": "class type can be blank also",
    "classification_l4": "class type can be blank also",
    "image_url": "Image URL (String type)"
}
```



***READ operation***
- method used

*format*
```text
1. db.collection.find(          # collection
    { _id: {$gt: 18} },         # query criteria
    { name: 1, address:1 }      # projection
).limit(int)                    # cursor modifier
```




***UPDATE operation***
- method used
1. db.collection.updateOne({}) # update only one instance
2. db.collection.updateMany({}) # update multiple instance
3. db.collection.replaceOne({}) # replace perticullar instance

*format*
```text
db.collection.updateMany(           # collection
    { _id: {$lt: 18} },             # update filter
    { $set {status: "reject"} }     # update action
)
```


***DELETE opration***
- method used
1. db.collection.deleteOne()
2. db.collection.deleteMany()

*format*
```txt
db.collection.deleteMany(       # collection
    { status: "rejected" }      # delete filter
)
```
