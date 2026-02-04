from flask import Flask, render_template
from data import resume_data

app = Flask(__name__)

@app.route('/')
def index():
    """ Renders the main resume landing page. """
    return render_template('index.html', 
                          title="Home",
                          personal=resume_data['personal_info'],
                          contact=resume_data.get('contact', {}))

@app.route('/document')
def document():
    """ Renders the detailed professional resume section. """
    return render_template('document.html', 
                          title="Resume",
                          personal=resume_data['personal_info'],
                          contact=resume_data.get('contact', {}),
                          skills=resume_data.get('skills', []),
                          experience=resume_data.get('experience', []),
                          education=resume_data.get('education', []),
                          languages=resume_data.get('languages', []),
                          hobbies=resume_data.get('hobbies', []),
                          services=resume_data.get('services', []),
                          testimonials=resume_data.get('testimonials', []))

if __name__ == '__main__':
    app.run(debug=True)
