from flask import Flask, render_template
from data import resume_data

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main resume landing page.
    Passes the 'personal_info' and 'skills' parts of the dictionary.
    """
    return render_template('index.html', 
                           title="Home",
                           personal=resume_data['personal_info'], 
                           skills=resume_data['skills'],
                           projects=resume_data['projects'][:2]) # Show first 2 projects only on index

@app.route('/document')
def document():
    """
    Renders the detailed document/resume page.
    Passes all resume data parts relevant to a full CV.
    """
    return render_template('document.html', 
                           title="Full Resume",
                           personal=resume_data['personal_info'],
                           education=resume_data['education'],
                           experience=resume_data['experience'],
                           projects=resume_data['projects'],
                           skills=resume_data['skills'])

if __name__ == '__main__':
    # Running in debug mode for development
    app.run(debug=True)
