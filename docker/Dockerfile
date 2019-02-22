FROM python:3.6
RUN pip3 install kubernetes
ADD main.py main.py
ENTRYPOINT ["python", "-u"]
CMD ["main.py"]