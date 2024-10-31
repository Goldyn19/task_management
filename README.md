# task_managemet

# Django Project Setup Guide

This document provides a step-by-step guide to setting up a Django project.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/) (version 3.8 or later)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)

## Step 1: Create a Virtual Environment

Creating a virtual environment helps isolate project dependencies. You can skip this step if you prefer to install packages globally.

```bash
# Navigate to your desired project directory
cd /path/to/your/project-directory

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

## Step 2
Installing all required packeges and libraries

```bash
# run the following command
pip install requirements.txt
```

## step 3
Setting up .env file
```bash
# Create a .env file in the root directory of the project
## In the file, add the following value to connect to your postgres server

DB_NAME='DB_name'
DB_USER='db_username'
DB_PASSWORD='DB_password'
DB_HOST='DB_host_url'
DB_PORT='DB_port'

```

## step 4
Runimg test scripts for the API end points.

Note: the test scripts is located in the task/test.py file

Run the following command
```
python manage.py test
```

