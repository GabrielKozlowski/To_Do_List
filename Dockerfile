FROM python:3.11
RUN apt-get update -y
RUN apt-get install tk -y

CMD ["/src/app/app.py"]
ENTRYPOINT [ "python3" ]