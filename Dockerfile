FROM python:2.7
EXPOSE 8080
COPY ahdh-api/app.py
CMD python ahdh-api/app.py
