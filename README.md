# DevOps Mini Project

This repository demonstrates a minimal end-to-end DevOps pipeline for a small Flask application.

Pipeline architecture overview:
Jira -> GitHub -> GitHub Actions -> Docker -> Target Environment

- Managed in Jira: track issues, features and releases.
- Hosted on GitHub: source code and collaboration.
- Built with GitHub Actions: CI job runs tests and builds Docker images on each push/PR to `main`.
- Packaged with Docker: containerized application ready for deployment.

How to run locally:
1. Create a virtual environment and install requirements:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
2. Run the app:
   python app.py
3. Visit: http://localhost:5000
