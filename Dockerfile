# Dockerfile
FROM python:3.11-slim

# ติดตั้ง dependency ที่จำเป็น
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libgl1 libglib2.0-0 \
    libgomp1 && \
    ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
