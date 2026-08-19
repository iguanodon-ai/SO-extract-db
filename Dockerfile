FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DB_HOST=localhost
ENV DB_PORT=3306
ENV DB_USER=root
ENV DB_PASSWORD=secret
ENV DB_NAME=dictionary
ENV OUTPUT=/app/out/entries.json

WORKDIR /app
RUN mkdir -p /app/out
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY src/ /app/src/

CMD ["uv", "run", "python", "src/extract.py"]
