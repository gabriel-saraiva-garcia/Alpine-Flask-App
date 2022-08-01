#!/bin/bash
clear
printf " \033[0;32m Building Docker image based on Dockerfile \033[0m \n" 
cd ..
docker build -t flask/alpine .
