# A1 — From Prototypes to Agents with ADK (Kitchen Renovation Proposal)

This project implements the A1 codelab end-to-end with the Google Agent Development Kit (ADK).  
The agent writes a contract-style **kitchen renovation proposal** and a tool `store_pdf` saves it as a **PDF** either to **Google Cloud Storage (GCS)** or locally (dry-run).

---

## What you get

- **One agent** (`renovation_proposal_agent`) using a Gemini model
- **One tool** (`store_pdf(title, body)`) that creates a well-formatted PDF
- **Two run modes**
  - **Dry-run**: saves the PDF locally and returns a `file://` path (no GCS needed)
  - **GCS**: uploads the PDF to your bucket and returns a URL or `gs://` URI
- Works with **ADK Dev UI** (`adk web`) or **CLI** (`adk run`)

## Repository layout

A1_From_Prototypes_to_Agents_with_ADK/
├── README.md
└── renovation_agent/
├── init.py
├── agent.py
├── requirements.txt
└── .env.example


> ADK discovers your agent because `renovation_agent/__init__.py` imports `agent.py` and defines `root_agent`.

---

## Prerequisites

- Python **3.10+**
- One of the following for Gemini access:
  - **Google AI Studio API key** (simple local demos), or
  - **Vertex AI** credentials (project + location)
- For GCS uploads (only if not using dry-run):
  - A **Google Cloud project** with billing enabled
  - A **GCS bucket** you can write to
  - **Application Default Credentials** on your machine:
    ```bash
    gcloud auth application-default login
    ```

---

## Setup

1) Create and activate a virtual environment, then install dependencies:
```bash
cd A1_From_Prototypes_to_Agents_with_ADK
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r renovation_agent/requirements.txt

2) Copy .env.example to .env and fill in values.

Path A — AI Studio (recommended for local demos):

GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_AI_STUDIO_KEY
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1
STORAGE_BUCKET=your-bucket-name
DRY_RUN=false

Path B — Vertex AI (alternative):

GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1
STORAGE_BUCKET=your-bucket-name
DRY_RUN=false

No GCS yet? Use dry-run:

DRY_RUN=true
# STORAGE_BUCKET may be left blank if DRY_RUN=true

Run

Run from the parent directory that contains the renovation_agent/ package so ADK can import it.

Dev UI (recommended for your video)
adk web


Open the local URL it prints.

Select renovation_proposal_agent in the dropdown.

Paste the sample prompt (below) and run.

CLI (alternative)
adk run renovation_agent

Sample prompt

Generate a proposal document for a kitchen remodel. Make it contract-appropriate with headings and bullet points. When it is ready, store it as a PDF.

Expected result

In dry-run: the final message includes a file://…/kitchen_proposal_*.pdf path.

With GCS: the final message includes a public URL (if made public) or a gs://bucket/object.pdf URI.

Verifying the output

Dry-run: open the file://… path in your PDF viewer.

GCS:

In the Cloud Console, navigate to Storage > Buckets > your bucket and confirm the object.

If you want a public link for your assignment video, make the object publicly readable.
(Use public access only for demo coursework; restrict in production.)

Troubleshooting

“Missing key inputs argument!”
You set neither (or both) Gemini auth paths. Set exactly one of:

AI Studio: GOOGLE_GENAI_USE_VERTEXAI=FALSE and GOOGLE_API_KEY

Vertex AI: GOOGLE_GENAI_USE_VERTEXAI=TRUE and project/location

Agent not visible in Dev UI
Run adk web from the parent folder of renovation_agent/.
Ensure renovation_agent/__init__.py contains from . import agent.

GCS permission denied / bucket not found
Run gcloud auth application-default login.
Check .env STORAGE_BUCKET spelling and your project.

PDF created but text looks odd
The sample uses core fonts; non-ASCII characters are replaced. For full Unicode, switch to a TTF font in agent.py.
