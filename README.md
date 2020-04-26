# Classification Prediction Web App

## Description

## Demo

https://covid-19-fatality-predictor.herokuapp.com/

## Features

## Tech Stack

- HTML / CSS
- Python
- Flask
- Jupyter Notebook

## Setup

Install miniconda3 package from official website to use conda.
https://docs.conda.io/en/latest/miniconda.html

Move to project directory

```
cd ml-ds-js
```

Create a virtual environment

```
# venv
python -m venv env

# conda
conda create --prefix ./env
```

Activate virtual environment

```
# venv
source env/bin/activate

# conda
conda env list
conda activate /filepath/env
```

Install dependencies

```
# venv
pip install -r requirements.txt

# conda
conda install pip
which pip # Make sure it is environment pip, not global pip
pip install -r requirements.txt
```

### Setup web app

Start server

```
python app.py
```

Stop server

```
ctrl + c
```

### Setup Jupyter Notebook

Start server

```
jupyter notebook
```

Stop server

```
ctrl + c
```

## Lessons Learned
