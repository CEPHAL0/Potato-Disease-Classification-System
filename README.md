# Potato Disease Classificaation System
This system is intended to classify potato plant leaves in three classes
1. Early Blight
2. Late Blight
3. Healthy

The model has been trained using CNN and has been deployed in the python fastapi backend server, to run the model run the following commands in shell:

```shell
cd api
uvicorn index:app --host localhost --port 8000 --reload
```

## JSON Endpoints
The following Endpoints have been configured for the CRUD operation of the users and two seperate models have been deployed:

/model/v1

/model/v2

/user/create

/user/delete

To refer to all of the APIs, you can use the **Swagger** dashboard on the URL:

/docs

_- Sharad Sharma, 2023_
