# Pastebin Clone #

Django Rest Framework Tutorial [from official site](https://www.django-rest-framework.org/tutorial/1-serialization/).

Try hitting an endpoint with `httpie`

`$ http http://127.0.0.1:8000/snippets.json --debug`

or create a record with either command line or browseable API:

`$ http -a jon:snarrf POST http://127.0.0.1:8000/snippets/ code="print(123)"`

Vist the following URL for logging in to DRF Browseable API:

http://127.0.0.1:8000/api-auth/login/?next=/snippets/


And remove a record with:

`$ http --json DELETE http://127.0.0.1:8000/snippets/9/`


---
## Includes a Jupyter Notebook that can be run with Shell Plus.

To run the Jupyter Notebook:

1. `$ source venv/bin/activate`
2. `$ cd tutorial; ./manage.py shell_plus --notebook`
3. In Jupyter file listing, open `tutorial_commands.ipynb`
4. Run first cell to import the Django model to verify the notebook is working with Django
