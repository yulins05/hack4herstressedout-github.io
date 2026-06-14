FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install security patches and build dependencies if necessary
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy internal application modules
COPY config/ ./config/
COPY services/ ./services/
COPY ui/ ./ui/
COPY app.py callbacks.py ./

# Avoid running container processes as root for container isolation security
RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

# Production container WSGI daemon execution command
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "--workers", "2", "--threads", "4", "--timeout", "60", "app:server"]