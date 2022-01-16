FROM python:3.8
COPY . .
RUN ls
CMD python3 main.py