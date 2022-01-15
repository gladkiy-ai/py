FROM python:3.8
COPY main.py /main.py
RUN chmod +x /main.py
CMD python3 /main.py

