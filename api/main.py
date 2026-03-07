from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

requests_total = Counter(
    "api_requests_total",
    "Total API Requests"
)

@app.get("/")
def home():
    requests_total.inc()
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
