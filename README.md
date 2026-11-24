# LLM & AI Engineering Lab (`ai-lm-engineer-lab`)

A structured, hands-on engineering lab for building a strong foundation in Large Language Model (LLM) application development—from core inference mechanics and structured outputs to RAG, evaluation pipelines, and production-ready services.

---

## Curriculum & Learning Modules

| Module | Directory | Focus Areas |
| :--- | :--- | :--- |
| **01. LLM Inference** | `lessons/01_llm_inference/` | OpenAI-compatible API calls (Groq / OpenAI), sampling parameters (`temperature`, `top_p`, `max_output_tokens`), and token usage tracking |
| **02. Prompt Engineering** | `lessons/02_prompt_engineering/` | System/user prompt design, few-shot prompting, chain-of-thought, and templating |
| **03. Structured Output** | `lessons/03_structured_output/` | Schema validation and type-safe LLM responses using `pydantic` |
| **04. RAG** | `lessons/04_rag/` | Retrieval-Augmented Generation, chunking, embeddings, and context grounding |
| **05. Evaluation** | `lessons/05_evaluation/` | Benchmarking prompts and pipelines, automated metrics, and LLM-as-a-judge |
| **06. Production** | `lessons/06_production/` | Serving LLM workflows with `FastAPI` & `Uvicorn`, async calls (`httpx`), retries, and latency/cost optimization |

---

## Repository Structure

```text
llm-ai-engineering-lab/
├── lessons/                     # Step-by-step core lessons
│   ├── 01_llm_inference/        # First API calls, parameters & token usage
│   ├── 02_prompt_engineering/   # Prompt patterns & strategies
│   ├── 03_structured_output/    # Pydantic schemas & structured parsing
│   ├── 04_rag/                  # Retrieval-Augmented Generation workflows
│   ├── 05_evaluation/           # Evaluation methods & grading scripts
│   └── 06_production/           # Production APIs & deployment patterns
├── src/
│   └── llm_lab/                 # Shared reusable package modules & utilities
├── experiments/                 # Sandbox for rapid prototyping
│   ├── inference/
│   ├── notebooks/
│   └── prompts/
├── evaluation/
│   └── datasets/                # Golden datasets & test cases for evals
├── projects/
│   └── knowledge_assistant/     # End-to-end capstone / applied project
├── tests/                       # Unit & integration test suite (pytest)
├── .env.example                 # Example environment variable template
└── requirements.txt             # Python dependencies
```

---

## Tech Stack

- **LLM Client:** `openai` (compatible with OpenAI, Groq, and local inference servers)
- **Data Validation:** `pydantic`
- **API & Serving:** `fastapi`, `uvicorn`, `httpx`
- **Configuration:** `python-dotenv`
- **Testing:** `pytest`

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shomay12/ai-lm-engineer-lab.git
cd llm-ai-engineering-lab
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file and add your API credentials:

```bash
cp .env.example .env
```

Update `.env` with your API key and target model (for example, using Groq's OpenAI-compatible endpoint):

```dotenv
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```

### 5. Run Lesson 01: First Inference Request

```bash
python lessons/01_llm_inference/first_request.py
```

---

## Running Tests

```bash
pytest
```
