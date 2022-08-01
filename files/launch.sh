#!/bin/bash
clear
printf " \033[0;32m Launching Container... \033[0m"
docker run -dit --rm -p 8282:8282 --name flask-app flask/alpine