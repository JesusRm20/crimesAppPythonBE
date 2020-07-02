FROM python:3.7-alpine 
WORKDIR /cloudProject 
COPY . /cloudProject
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
Run pip install psycopg2-binary
Run pip install -U -r requirements.txt 
EXPOSE 8080 9042 
CMD ["python" , "main.py"]
