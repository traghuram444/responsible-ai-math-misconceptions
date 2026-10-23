FROM python:3.11.11-slim-bookworm@sha256:081075da77b2b55c23c088251026fb69a7b2bf92471e491ff5fd75c192fd38e5
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 \
    OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
    PYTHONHASHSEED=20261020 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    HF_HOME=/tmp/huggingface PYTHONPATH=/workspace/src
COPY wheels /wheels
COPY requirements.lock /requirements.lock
RUN python -m pip install --no-index --find-links=/wheels --require-hashes -r /requirements.lock \
    && python -m pip check \
    && groupadd --gid 10001 research \
    && useradd --uid 10001 --gid 10001 --no-create-home research
USER 10001:10001
WORKDIR /workspace
CMD ["python", "--version"]
