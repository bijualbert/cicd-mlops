# ML Pipeline CI/CD Demo

## Overview
This is a sample project demonstrating CI/CD (Continuous Integration/Continuous Deployment) for Machine Learning models. It uses DVC for data and model versioning, CML for automated reporting in pull requests, and MLEM for model deployment.

## Project Structure
- `src/`: Python scripts for data processing, training, and evaluation
- `data/`: Data files (tracked by DVC)
- `model/`: ML models (tracked by DVC)
- `tests/`: Test files
- `dvclive/`: Metrics from DVC experiments
- `params.yaml`: Parameters for Python scripts
- `dvc.yaml`: DVC pipeline definition
- `.github/workflows/`: GitHub Actions workflows for CI/CD
- `app.py`: FastAPI server for the demo interface

## Tools Used
- **DVC**: Data and model version control
- **CML**: Continuous Machine Learning - posts experiment metrics to PRs
- **MLEM**: ML model deployment
- **FastAPI**: API server
- **scikit-learn**: Machine learning library

## Running the Project
The project runs a FastAPI server on port 5000 that displays the project status and API documentation.

### Prerequisites
To fully run the ML pipeline, you need:
1. AWS credentials for S3 access (to pull data/models)
2. Run `dvc pull -r read` to fetch data and models from remote storage

### Running Experiments
```bash
dvc exp run
```

### Running Tests
```bash
pytest tests/
```

## API Endpoints
- `GET /` - Main dashboard page
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## Python Version
This project uses Python 3.11
