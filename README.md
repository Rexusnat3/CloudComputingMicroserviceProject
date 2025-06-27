# Email Service Microservice

## Project Structure
```

email-service/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── email_sender.py
│   └── config.py
├── ecs-task-def.json
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── .env                # (ignored in .gitignore)
├── .gitignore
├── README.md
```


This is a lightweight, containerized email sending microservice built with FASTAPI and Python. 
this service provides a simple REST API for sending emails via SMTP with some error handling and 
validation. 

Features:
1. RESTful API: Simple POST endpoint for sending emails
2. Email Validation: Built-in email address validation using Pydantic
3. SMTP Support: Compatible with any SMTP provider (Gmail, SendGrid, etc.)
4. Containerized: Docker-ready for easy deployment
5. AWS Ready: ECS task definition included for AWS deployment
6. Environment-based Config: Secure configuration via environment variables
7. Auto Documentation: Interactive API docs with FastAPI/Swagger

Prerequisites:
Python 3.11+
Docker
SMTP email provider credentials

Instalation and Set Up:
1. Clone the repository
   (git clone https://github.com/Rexusnat3/CloudComputingMicroserviceProject.git
   cd email-service)
2. Create a virtual environment
   (python - venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate)
3. Install Dependencies
   (pip install -r requirements.txt)
4. Configure Environment Variables
   (edit the .env file with your SMTP credentials)
5. Run the application
  (uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload)

Gmail Setup
For Gmail, you'll need to:

Enable 2-factor authentication
Generate an App Password
Use the App Password as SMTP_PASSWORD in your env file

