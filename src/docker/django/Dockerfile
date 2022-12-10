FROM python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

# Copy project
COPY . .

RUN chmod +x -R /code/pages/management/commands/