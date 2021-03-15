/* =================================================================  
  NOTES
================================================================= */

/*
CONDA
https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533

install miniconda3 package from official website

cd sample_project

conda create --prefix ./env pandas numpy matplotlib scikit-learn

conda env list

conda activate /Users/eunice/Desktop/sample_project/env

conda list

conda install jupyter

jupyter notebook

conda deactivate

--------------------------------------------------------------------

conda env export > environment.yml

cd heart-disease-project

# Create conda environment from yml file 
conda env create --prefix ./env -f ../environment.yml 

^ Alternative for: 
conda env create --prefix ./env pandas scikit-learn numpy matplotlib jupyter

--------------------------------------------------------------------
BLACK

activate / enter virtual environment
pip install black

Add .vscode settings.json settings from previous python projects
This will set formatter to black
And format on save to true

install linter, such as pylint, with conda

Can also run by doing below in terminal
black app.py

--------------------------------------------------------------------
FLASK

https://flask.palletsprojects.com/en/1.1.x/installation/
^ venv instructions

install flask

--------------------------------------------------------------------
HEROKU

Getting Started on Heroku with Python
https://devcenter.heroku.com/articles/getting-started-with-python#prepare-the-app
https://github.com/heroku/python-getting-started

--------------------------------------------------------------------
CHOOSE HEROKU URL

Creating a named app
https://devcenter.heroku.com/articles/creating-apps#creating-a-named-app

`heroku create example` // example.herokuapp.com

Renaming Apps from the CLI
https://devcenter.heroku.com/articles/renaming-apps

--------------------------------------------------------------------
Deploy the app
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

`git push heroku main`

Deploying a Python Flask app on Heroku
https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0
https://github.com/jokamjohn/bucket_api_heroku
John Kagga 2017

Step-by-Step Guide on Deploying a Simple Flask App to Heroku
https://pybit.es/deploy-flask-heroku.html
2017

Deploy Python Flask App on Heroku
https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

heroku create eflask-app

--------------------------------------------------------------------
Python
https://devcenter.heroku.com/categories/python-support

Deploying Python Applications with Gunicorn
https://devcenter.heroku.com/articles/python-gunicorn

Python Dependencies via Pip
https://devcenter.heroku.com/articles/python-pip

Specifying a Python Runtime
https://devcenter.heroku.com/articles/python-runtimes

Deploying with Git
https://devcenter.heroku.com/articles/git

The Procfile
https://devcenter.heroku.com/articles/procfile

 */

/*
--------------------------------------------------------------------
*/