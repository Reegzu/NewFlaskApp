import os
import click
from app import create_app

#pobranie ze zmiennej srodowiskowej 'set FLASK_CONFIG=(co tam chcemy) i zastosowanie go do odpalenia reszty apki
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

#wykorzystywane do baz danych, umozliwia autoamtyczny import jej elementow
@app.shell_context_processor
def make_shell_context():
    return
