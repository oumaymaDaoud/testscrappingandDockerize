FROM python:3.9-alpine
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY main.py /.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# les commandes utilisés dans terminal 
#docker build -t oumaymascraping (pour création image from dockerfile)
#docker-compose up --force-recreate (pour création les containers )

 