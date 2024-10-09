FROM ubuntu:22.04

# avoid unnecessary writes to disk
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

ARG dev=false

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    python3 \
    python3-venv \
    ssh \
    wget \
    gnupg2 \
    && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends google-cloud-cli && \
    rm -rf /var/lib/{apt,dpkg,cache,log}

ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and pre-commit config
COPY requirements.txt ./
COPY .pre-commit-config.yaml ./

# Create virtual environment, upgrade pip, and install requirements
RUN python3 -m venv /opt/venv && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

# Copy application code
COPY . .
