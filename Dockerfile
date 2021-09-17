FROM python:latest

ENV ROOT_PATH="/opt/main_app/"

ADD code/requirements.txt requirements.txt
RUN pip install -r requirements.txt && mkdir -p ${ROOT_PATH}

COPY code/ ${ROOT_PATH}
WORKDIR ${ROOT_PATH}

EXPOSE 5000
ENTRYPOINT ["python3", "main.py"]
