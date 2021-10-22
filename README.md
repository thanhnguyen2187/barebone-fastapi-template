# Barebone FastAPI Template

A template which consists the most basic elements to work with FastAPI.

## Prerequisites

- Python 3.8
- Ubuntu 20.04/Linux

## Getting Started

- Move to the correct folder:

```bash
cd barebone-fastapi-template
```

- Create a new virtual environment:

```bash
python -m venv venv
```

- Activate the environment:

```bash
source venv/bin/activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Start development server:

```bash
uvicorn barebone_fastapi_template:app --reload
```

- Run test:

```bash
pytest
```

## Project Structure

### `barebone_fastapi_templates`

The main source code folder, following a "standard" Python project structure.

- `repositories`: to communicate with databases/external data sources
- `endpoints`: to receive requests and response data
- `mediators`: for data transformation functions
- `cores`: pure processing functions
- `integrations`: third-party packages (`pydantic`, `fastapi`) extending/integration

```
+--------------------------------+
|   endpoints   |   repositories |
| +----------------------------+ |
| |         mediators          | |
| | +------------------------+ | |
| | |        cores           | | |
| | +------------------------+ | |
| +----------------------------+ |
+--------------------------------+
```
