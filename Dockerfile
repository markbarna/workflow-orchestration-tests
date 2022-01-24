FROM python:3.9-slim

WORKDIR /opt
COPY docker_requirements.txt requirements.txt

RUN python -m venv .venv && \
    /opt/.venv/bin/pip install --upgrade pip && \
    /opt/.venv/bin/pip install -r requirements.txt

WORKDIR /home
COPY handlers/ handlers/

ENTRYPOINT [ "/opt/.venv/bin/python", "-m", "handlers.entrypoint" ]
CMD [ "--help" ]