FROM python:3.8-slim-buster

RUN mkdir /api

WORKDIR /api

COPY requirements.txt /api

RUN  apt-get update \
  && apt-get install -y wget \
  && apt-get install unzip
  

RUN yes | apt-get install python3-pip

RUN yes | apt install python3-dev libpq-dev

RUN pip3 install -r requirements.txt

COPY . /api

RUN wget https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/english_g2.zip

RUN wget https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/devanagari.zip

RUN wget https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip

RUN mkdir ~/.EasyOCR

RUN mkdir ~/.EasyOCR/model

RUN unzip devanagari.zip -d ~/.EasyOCR/model

RUN unzip english_g2.zip -d ~/.EasyOCR/model

RUN unzip craft_mlt_25k.zip -d ~/.EasyOCR/model

EXPOSE 6000

CMD [ "python3", "app.py" ]