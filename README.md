# stage1

## Build image:

docker build -t myimage .

## Run

docker run -d --name mycontainer -p 80:80 myimage

## Run mapping volume

docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app myimage

## Run and debug Python Flask code live

docker run -d --name mycontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 myimage flask run --host=0.0.0.0 --port=80

