# forms-api

A simple REST API to store new forms and get them.
To run it it is necessary to set the following env vars:

    DB_USER
    DB_PASSWORD
    DB_HOST
    DB_PORT
    DB_NAME

## CI/CD

docker build -t kubernetes-course:form-api-[version] -f Dockerfile .
docker tag  kubernetes-course:form-api-[version] jesu11s/kubernetes-course:form-api-[version]
