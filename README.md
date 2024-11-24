# DataHarbor

DataHarbor is a lightweight, containerized data engineering platform inspired by Databricks. It provides functionalities for managing notebooks, workflows, metadata, and Spark clusters.

## Features
- Notebook management (.ipynb, .py, .sql support)
- PostgreSQL metadata storage
- Spark cluster management
- Workflow creation and execution

## Tech Stack
- **Backend**: Flask
- **Frontend**: React.js
- **Database**: PostgreSQL
- **Big Data**: Apache Spark
- **Containerization**: Docker & Docker Compose

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/DataHarbor.git
   cd DataHarbor

## Project Structure 

DataHarbor/
├── backend/
│   ├── app.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── notebooks.py
│   │   ├── metadata.py
│   │   ├── workflow.py
│   │   └── clusters.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── notebook.py
│   │   ├── job.py
│   │   └── cluster.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── config.py
│   ├── requirements.txt
│   └── Dockerfile
├── db/
│   ├── init.sql
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   ├── services/
│   │   └── styles/
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── Dockerfile
├── notebooks/
│   └── sample.ipynb
├── docker-compose.yml
└── README.md
