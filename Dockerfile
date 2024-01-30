FROM python:3.10.12


WORKDIR /bot


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN sudo apt install awscli -y
RUN aws configure
COPY . .


CMD ["python", "bot/main.py"]