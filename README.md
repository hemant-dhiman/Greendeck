# Greendeck assignment

- `Download this repository`

- `drag and drop it in Docker`
 
- `or`
 
- `you can use online docker`(https://labs.play-with-docker.com/)

## Unzip project in Docker

```text
unzip Greendeck.zip
cd Greendeck
ls
```

## Dockerfile content

```text
**just for reference don't use this commands in docker**
**move forward to next section (Building a DockerImage file)**
FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]

```

## Building a DockerImage file

```
you are able to see all the files in the directory by 'ls' command

you should see following files
"DataBaseFile     Dockerfile       README.md        app.py           requirement.txt"

now run following commands

sudo docker build --tag greendeck_1 .
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
2. db.collection.replaceOne({}) # replace perticullar instance

*format*
```text
db.collection.updateMany(           # collection
    { _id: {$lt: 18} },             # update filter
    { $set {status: "reject"} }     # update action
)
```


***DELETE opration***
- method used
1. db.collection.remove({})

*format*
```txt
db.collection.remove(       # collection
    { "_id": 37 }           # delete filter
)
```
# Operations

**List all data**

`GET /database`
- `200 OK` on success
```json
[
  {
    "_id": 1,
    "name" : "Jellycat Blossom Tulip Bunny Grabber, Pink",
    "brand_name": "jellycat",
    "regular_price_value": 12,
    "offer_price_value": 12,
    "currency": "GBP",
    "classification_l1": "baby & child",
    "classification_l2": "soft toys",
    "classification_l3": "",
    "classification_l4": "",
    "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?"
  }
]
``` 

**Entry**

`POST /newdata`
- `201 Inserted` on success

##### return
```json
{
    "_id": 1,
    "name" : "Jellycat Blossom Tulip Bunny Grabber, Pink",
    "brand_name": "jellycat",
    "regular_price_value": 12,
    "offer_price_value": 12,
    "currency": "GBP",
    "classification_l1": "baby & child",
    "classification_l2": "soft toys",
    "classification_l3": "",
    "classification_l4": "",
    "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?"
 }
```

**Fetching data**

`GET /database/id/<int: i_d>`
- `i_d` integer type

##### return 
- `404 Not Found` if the id data not exist
- `200 OK` on success
```json
{
    "_id": 1,
    "name" : "Jellycat Blossom Tulip Bunny Grabber, Pink",
    "brand_name": "jellycat",
    "regular_price_value": 12,
    "offer_price_value": 12,
    "currency": "GBP",
    "classification_l1": "baby & child",
    "classification_l2": "soft toys",
    "classification_l3": "",
    "classification_l4": "",
    "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?"
 }
```

***Update***

`UPDATE /update/id/<int:i_d>/<string:name>`

- `i_d` integer value
- `name` String value

##### return
- `200 OK` Updated
- `Id` Already Exists


***Deleting data***

`/remove/id/<int:i_d>`

##### return
- `404 Not Found` if the id data not exist
- `204 No content` Success but return nothing