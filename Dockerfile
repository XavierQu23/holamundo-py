FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requeriments.txt
EXPOSE 8000
CMD ["python", "add.py"]
