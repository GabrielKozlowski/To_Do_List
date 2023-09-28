FROM python:3.11
WORKDIR /app
COPY . .
RUN requirements install
ADD app.py src/app/
CMD [ "python", "/src/app/app.py" ]