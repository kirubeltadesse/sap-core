# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.1

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements*.txt .
RUN python -m pip install -r requirements-dev.txt

# copying the requirements.txt file to the work directory
COPY requirements*.txt ./

# Installing the python requirement on the container
RUN pip install -r requirements-dev.txt

WORKDIR /workspace
COPY . /workspace

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /workspace
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
