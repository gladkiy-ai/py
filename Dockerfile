FROM python:3.8
COPY main.py /tmp/jenkins
RUN python3 main.py