#!/bin/bash
docker-compose up -d
docker exec -d jupyterlab_jupyter_1 jupyter lab
