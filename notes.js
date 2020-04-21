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

 */

/*
--------------------------------------------------------------------
*/