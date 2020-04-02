"""Route declaration."""
from flask import current_app as app
from flask import render_template

# routes
@app.route('/aulas/<aula>')
def about(aula):
    return render_template(f'aulas/aula-{aula}.html')
