FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates tini && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
ENV UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .
ENV PORT=8080
EXPOSE 8080
ENTRYPOINT ["/usr/bin/tini","--"]
CMD ["uv","run","python","purchasing_concierge_ui.py"]
