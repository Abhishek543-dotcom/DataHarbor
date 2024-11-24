## What is DataHarbor?
DataHarbor is a lightweight, containerized data engineering platform inspired by Databricks. It enables users to manage notebooks, metadata, workflows, and clusters in a seamless environment. Built entirely using Docker, it provides an affordable, scalable, and modular alternative for small teams, data enthusiasts, and developers to collaborate and process big data effectively.

## Features
### Workspace:
- A central place to create, edit, and manage Python notebooks with support for `.py`, `.ipynb`, and `.sql` file formats. Includes import/export functionality.

### Metadata Management:
- Store notebook metadata, workflow details, and execution history using PostgreSQL.

### Workflow Orchestration:
- Create and schedule jobs from notebooks. Define cluster configurations (CPU, RAM) for efficient processing.

### Dynamic Clusters:
- Spin up Spark clusters dynamically in isolated Docker containers for running notebooks.

---

## Why Use DataHarbor?
- **Lightweight and Portable**: Perfect for small teams and personal projects.
- **Fully Containerized**: No need for manual installations; all dependencies are bundled.
- **Customizable**: Modify, extend, and integrate with your own workflows.
- **Learning Platform**: Ideal for understanding containerized data processing and orchestration.

---

## Tech Stack
- **Frontend**: React.js - For an interactive and user-friendly web interface.
- **Backend**: Flask (Python) - Manages API routes, notebook operations, and job scheduling.
- **Database**: PostgreSQL - Stores metadata, job details, and execution history.
- **Big Data Processing**: Apache Spark with PySpark - For scalable data transformations and analysis.
- **Containerization**: Docker - Ensures portability and consistency across environments.
- **Orchestration**: Docker Compose - Manages interdependent services (frontend, backend, database, and clusters).

---

## Project Structure
```plaintext
DataHarbor/
├── backend/             # Backend API with Flask
│   ├── app.py           # Main application entry point
│   ├── routes/          # Modular Flask routes
│   ├── models/          # Database models
│   ├── utils/           # Helper functions
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile       # Backend container setup
├── db/                  # Database setup
│   ├── init.sql         # PostgreSQL initialization script
│   └── Dockerfile       # Database container setup
├── frontend/            # Frontend app with React.js
│   ├── src/             # React app source code
│   ├── public/          # Public assets
│   ├── package.json     # Frontend dependencies
│   └── Dockerfile       # Frontend container setup
├── notebooks/           # Jupyter notebooks
│   └── sample.ipynb     # Placeholder for user uploads
├── docker-compose.yml   # Compose services
└── README.md            # Project documentation
```