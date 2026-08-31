# Pin the interpreter release; renovate this deliberately when upgrading.
FROM python:3.11.11-slim-bookworm@sha256:081075da77b2b55c23c088251026fb69a7b2bf92471e491ff5fd75c192fd38e5

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace

RUN groupadd --gid 10001 research \
    && useradd --uid 10001 --gid 10001 --create-home --shell /bin/bash research

COPY requirements.lock pyproject.toml README.md ./
COPY src ./src
COPY scripts ./scripts
COPY tests ./tests
COPY experiments ./experiments

RUN python -m pip install --upgrade pip==24.3.1 \
    && python -m pip install --requirement requirements.lock \
    && python -m pip install --editable . \
    && chown --recursive research:research /workspace

USER research

CMD ["bash"]
