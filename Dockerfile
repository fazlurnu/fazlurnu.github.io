FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir jupyterlite-core jupyterlite-pyodide-kernel jupyter-server

COPY notebooks/ notebooks/

RUN jupyter lite build --contents notebooks/ --output-dir /site

WORKDIR /site

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000"]
