# Running Locally

	python3 -m venv env &&
	source env/bin/activate &&
	pip install pandas &&
	pip install seaborn &&
    pip install matplotlib &&
	pip install jupyter &&
	jupyter-notebook

Avoid pip3 in virtual environments.

Open Jupyter Notebook and click fake_job_prediction.ipynb and run each step:

	jupyter-notebook

To run new cmds in the same virtual environment, in a new prompt run:

	source env/bin/activate


Or you can run fake_job_prediction.ipynb from the command line:  

	jupyter nbconvert --to notebook --inplace --execute fake_job_prediction.ipynb

If you get a vague error when opening Jupyter notebook, 
run the jupyter nbconvert cmd above to reveal the error.