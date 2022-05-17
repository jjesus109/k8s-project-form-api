FROM python:3.8-slim
WORKDIR src/
ENV PYTHONPATH=PYTHONPATH:/src/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY exec.sh .
COPY app/* ./app/
CMD ["sh", "exec.sh"]