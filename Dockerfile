FROM python:3.8
COPY main.py .
RUN ls
CMD python3 main.py