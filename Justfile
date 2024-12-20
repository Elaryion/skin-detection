devserv:
    uv run src/serv.py

test:
    uv run src/pred.py

imagepull:
    #TODO

build:
    sudo docker build . -t elaryon-server

run:
    sudo docker run -p 5000:5000 elaryon-server

