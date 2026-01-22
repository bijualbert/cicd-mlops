# Copilot Instructions for cicd-mlops

## Project Overview
This repository demonstrates a CI/CD pipeline for machine learning using Python, DVC, MLEM, and GitHub Actions. The workflow automates data processing, model training, evaluation, and deployment.

## Architecture & Data Flow
- **Data**: Raw data is stored in `data/`. Processed data is saved to `data/intermediate` via `src/process_data.py`.
- **Pipeline**: The DVC pipeline (`dvc.yaml`) defines three main stages: `process` (data split), `train` (model training with GridSearchCV), and `evaluate` (model evaluation and metrics logging).
- **Model**: Trained models are saved in `model/` (notably `svm.mlem` for deployment).
- **Parameters**: All configurable parameters are in `params.yaml`.
- **Metrics**: Experiment metrics are logged to `dvclive/`.

## Key Workflows
- **Setup**: Install dependencies with `pip install -r requirements.txt`.
- **Data Sync**: Use `dvc pull -r read` to fetch data from remote storage. Credentials are required for private remotes.
- **Experimentation**: Run `dvc exp run` to execute the pipeline. Edit files in `src/`, `params.yaml`, or `tests/` to trigger new experiments.
- **Testing**: Run `pytest` to execute all tests in `tests/`. Fixtures in `conftest.py` provide model and data objects for test cases.
- **Model Deployment**: On `main` branch push, `.github/workflows/publish.yaml` deploys the model using MLEM and Fly.io.

## Conventions & Patterns
- **All data/model paths and parameters are managed via `params.yaml` and referenced using `dvc.api.params_show()` in code.**
- **Helper functions** for data I/O are in `src/helper.py`.
- **Test data and models** are loaded using fixtures in `tests/conftest.py`.
- **DVC Live** is used for experiment tracking and metric logging.
- **Makefile** provides shortcuts for cleaning, requirements management, and experiment/deployment tasks.

## Integration Points
- **DVC**: Used for data versioning, pipeline orchestration, and experiment tracking.
- **MLEM**: Used for model serialization and deployment.
- **GitHub Actions**: `.github/workflows/run_test.yaml` runs tests and evaluation on PRs; `publish.yaml` deploys models on main branch updates.
- **CML**: Used for experiment reporting in PRs.

## Examples
- To run the full pipeline locally:
  ```sh
  dvc exp run
  ```
- To test code:
  ```sh
  pytest
  ```
- To deploy the model (after merge to main):
  - Model is deployed automatically via GitHub Actions and MLEM.

## References
- See [README.md](../README.md) for more details and external articles.
- See `dvc.yaml`, `params.yaml`, and `.github/workflows/` for pipeline and automation logic.
