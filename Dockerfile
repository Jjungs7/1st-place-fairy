FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /usr/src/1st-place-fairy

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY fairy fairy

ENTRYPOINT ["python", "-m", "fairy.main"]
