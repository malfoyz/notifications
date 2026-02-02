FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv pip install --system ".[test]"

COPY . ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
