FROM alpine:latest

COPY app /app/
WORKDIR /app
RUN apk update\
&& apk add --no-cache python3 py3-pip\
&& pip install Flask\
&& apk add docker\
&& service docker start

EXPOSE 8282

CMD ["python3", "run.py"]