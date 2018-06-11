FROM python:3

WORKDIR /usr

COPY ./src ./src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP microblog.py

WORKDIR /usr/src/server

CMD ["/bin/bash"]

