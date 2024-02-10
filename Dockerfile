FROM python:3.10.12


WORKDIR /bot


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .


CMD ["python", "bot/main.py"]