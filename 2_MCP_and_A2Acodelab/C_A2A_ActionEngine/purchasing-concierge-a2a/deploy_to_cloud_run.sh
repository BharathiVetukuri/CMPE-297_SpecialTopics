set -euo pipefail
PROJECT_ID="${PROJECT_ID:-$(gcloud config get-value project)}"
REGION="${REGION:-us-central1}"
REPO="${REPO:-pc-images}"
SERVICE="${SERVICE:-purchasing-concierge-a2a}"
IMAGE="${IMAGE:-pc-a2a}"
FULL_IMAGE="$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE:latest"
gcloud artifacts repositories describe "$REPO" --location="$REGION" >/dev/null 2>&1 || \
gcloud artifacts repositories create "$REPO" --repository-format=docker --location="$REGION"
gcloud builds submit --tag "$FULL_IMAGE"
gcloud run deploy "$SERVICE" \
  --image "$FULL_IMAGE" \
  --region "$REGION" \
  --allow-unauthenticated \
  --port 8080 \
  --memory 1Gi \
  --cpu 1 \
  --concurrency 80

gcloud run services describe "$SERVICE" --region "$REGION" \
  --format='value(status.url)'
