# FastAPI Setup on Ubuntu

## Prerequisites

- Ubuntu 20.04 or later
- Python 3.8 or later

## Step 1: Update and Upgrade the System

First, update and upgrade your system packages:

```sh
sudo apt update
sudo apt upgrade -y
```

## Step 2: Install Python
Install Python and pip
```sh 
sudo apt install python3 python3-pip -y 
```

Verify the installation
```sh
python3 --version
pip3 --version
```

## Step 3: Set Up a Virtual Environment
Create a virtual environment for your project:
```sh
sudo apt install python3-venv -y
python3 -m venv venv
```

Activate the virtual environment
```sh
source venv/bin/activate
```

## Step 4: Install FastAPI and Uvicorn
```sh
pip install -r requirements.txt
```

## Step: Run FastAPI Server
```sh
fastapi run main.py
```
