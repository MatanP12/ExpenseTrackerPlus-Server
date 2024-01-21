# Expense Tracker Plus API

A simple expense tracker API, built using Python FastAPI, SQLModel

## Build with
-   Python
-   FastAPI - web framework for building APIs with Python 3.8+.
- SQLModel - a library for interacting with SQL databases from Python code, with Python objects(ORM). 
-   Pydantic - data validation library for Python.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

*  [Python 3.11+](https://www.python.org/)
* [Poetry](https://python-poetry.org/)
* Optional: [Docker](https://www.docker.com/)

### Get the project
1. Clone the [ExpenseTrackerPlus](https://github.com/MatanP12/ExpenseTrackerPlus-Server) repository  Using the command`git clone https://github.com/MatanP12/ExpenseTrackerPlus-Server.git`
2. Open any terminal and navigate to the project directory.

### Run on local Machine
1. Install dependencies using `poetry install`
2. invoke web sever using `poetry run uvicorn expense_tracker_plus.main:app --host 0.0.0.0 --port 8000 --reload`
3. Enjoy :)
### Run using docker
1. Invoke the composed containers using `docker-compose up`
2. Delete the containers using `docker-compose down --rmi all` 