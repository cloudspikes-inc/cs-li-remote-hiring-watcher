FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./

# If you prefer requirements.txt, swap the install step; or use Poetry.
RUN pip install --no-cache-dir uv && uv pip install -r <(uv pip compile pyproject.toml --generate-hashes)

COPY . .
CMD ["python", "src/scheduler/aps_scheduler.py"]
EXPOSE 3000