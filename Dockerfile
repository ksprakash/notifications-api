FROM python:latest
LABEL project=NotificationsAPI
COPY  .  .
RUN apt update -y &&  \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python","app.py"]
    