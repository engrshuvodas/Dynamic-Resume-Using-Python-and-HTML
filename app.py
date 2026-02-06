from flask import Flask, render_template
from data import resume_data

# Initialize the Flask application
app = Flask(__name__)

# --- ROUTE HANDLERS ---

@app.route('/')
def index():
    """ 
    Renders the main landing page (Home).
    Passes 'personal' and 'skills' data to the template.
    """
    return render_template('index.html', 
                           title="Professional Profile",
                           personal=resume_data['personal_info'],
                           skills=resume_data['skills'])

@app.route('/document')
def document():
    """ 
    Renders the detailed resume document.
    Passes all resume data sections to the template.
    """
    return render_template('document.html', 
                           title="Detailed Resume",
                           personal=resume_data['personal_info'],
                           experience=resume_data['experience'],
                           education=resume_data['education'],
                           projects=resume_data['projects'],
                           contact=resume_data['contact_info'])

# --- DATA FLOW EXPLANATION ---
# 1. The 'resume_data' dictionary is imported from data.py.
# 2. Inside each route, we use 'render_template' to load an HTML file.
# 3. We pass specific keys from the dictionary as arguments (e.g., personal=resume_data['personal_info']).
# 4. In HTML (using Jinja2), we access these variables using double curly braces (e.g., {{ personal.name }}).

if __name__ == '__main__':
    # Run the server in debug mode for development
    app.run(debug=True)
