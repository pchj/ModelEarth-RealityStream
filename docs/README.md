[RealityStream](../)

# Local Setup Extras

Also see our notes on [Node, Python, Docker and Conda](/io/coders/python/).

Occasionally you may want to update your local streamlit

	pip install --upgrade streamlit

If you encounter issues, try installing the required dependencies

	pip install -r requirements.txt

If that doesn't work, try

	pip install wordcloud
	pip install spaCy
	python -m spacy download en_core_web_sm
	pip install scikit-learn
	pip install imblearn
	pip install markdown
	pip install seaborn sns

spaCy is an open-source natural language processing (NLP) library


If you get a CLI error due to an older version, you can uninstall all instances of Streamlit. Then reinstall and restart terminal.  This should remove an older version from the anaconda folder.

	pip uninstall streamlit
	pip install streamlit

Run `pip -V` before and after you start your virtual environment.  
In May 2024, the latest pip version is: pip 24
Also running once in your virtual environment seems to correct going forward.

	python -m pip install --upgrade pip

If conflicts occur after you deploy to Streamlit.io, 
the following will allow you to see the same error locally.
Then update versions in requirements.txt to resolve conflicts.

	pip install --upgrade --force-reinstall -r requirements.txt

**For Admins** In requiements.txt, once new versions of numpy and spacy fix their bugs,  
it may be possible to remove max versions. Sync to "earthscape" repo for [reality.streamlit.app](https://reality.streamlit.app)

	numpy>=1.26.4,<2.0.0
	spacy>=3.7.2,<3.8.0

<!--
	Was spacy>=3.7.2, but en_core_web_sm-3.7.2 not available

	Tried spacy==3.7.2 with en_core_web_sm-3.7.2 based on:
	https://discuss.streamlit.io/t/how-to-include-en-core-web-sm-2-2-0-in-deployment/37673/3
-->

Also see our notes on [Node, Python, Docker and Conda](/io/coders/python/).
