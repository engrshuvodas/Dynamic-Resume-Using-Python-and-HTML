from flask import Flask, render_template
from data import resume_data

# Initialize the Flask application
app = Flask(__name__)

# --- ROUTE HANDLERS ---

def index():
    """ 
    Renders the main landing page (Home).
    Passes 'personal' and 'skills' data to the template.
    """
@app.route('/')
def index():
    """
    Render a simple resume-focused page (not a portfolio).
    We assemble a single `resume` dictionary from `resume_data` and pass it
    to `resume.html` so the template can access fields like `resume.name`.
    """
    personal = resume_data.get('personal_info', {})

    # Convert skills into a simple list of names for the simple resume template
    skills = [s.get('name') if isinstance(s, dict) else str(s) for s in resume_data.get('skills', [])]

    # Normalize experience entries for the simple resume template
    experience = []
    for e in resume_data.get('experience', []):
        item = {
            'title': e.get('role') or e.get('title'),
            'company': e.get('company'),
            'duration': e.get('period') or e.get('duration'),
            'description': []
        }
        # primary description (string)
        if e.get('description'):
            item['description'].append(e.get('description'))
        # achievements (list of strings)
        for a in e.get('achievements', []):
            item['description'].append(a)
        experience.append(item)

    # Normalize education
    education = []
    for ed in resume_data.get('education', []):
        education.append({
            'degree': ed.get('degree'),
            'school': ed.get('institution') or ed.get('school'),
            'duration': ed.get('year') or ed.get('duration'),
            'description': ed.get('details') or ed.get('description') or ''
        })

    resume = {
        'name': personal.get('name'),
        'title': personal.get('title'),
        'summary': personal.get('summary'),
        'contact': {
            'email': personal.get('email'),
            'phone': personal.get('phone'),
            'location': personal.get('location')
        },
        'skills': skills,
        'profile_img': personal.get('profile_img') or '/static/images/profile.jpg',
        # optional fields that may exist in data.py
        'languages': resume_data.get('languages', []),
        'hobbies': resume_data.get('hobbies', []),
        'services': resume_data.get('services', []),
        'testimonials': resume_data.get('testimonials', []),
        'skill_levels': resume_data.get('skill_levels', {}),
        'experience': experience,
        'education': education
    }

    return render_template('resume.html', resume=resume)


@app.route('/debug-resume')
def debug_resume():
    """Return the assembled `resume` dictionary as JSON for debugging."""
    from flask import jsonify
    personal = resume_data.get('personal_info', {})
    skills = [s.get('name') if isinstance(s, dict) else str(s) for s in resume_data.get('skills', [])]
    experience = []
    for e in resume_data.get('experience', []):
        item = {
            'title': e.get('role') or e.get('title'),
            'company': e.get('company'),
            'duration': e.get('period') or e.get('duration'),
            'description': []
        }
        if e.get('description'):
            item['description'].append(e.get('description'))
        for a in e.get('achievements', []):
            item['description'].append(a)
        experience.append(item)

    education = []
    for ed in resume_data.get('education', []):
        education.append({
            'degree': ed.get('degree'),
            'school': ed.get('institution') or ed.get('school'),
            'duration': ed.get('year') or ed.get('duration'),
            'description': ed.get('details') or ed.get('description') or ''
        })

    resume = {
        'name': personal.get('name'),
        'title': personal.get('title'),
        'summary': personal.get('summary'),
        'contact': {
            'email': personal.get('email'),
            'phone': personal.get('phone'),
            'location': personal.get('location')
        },
        'skills': skills,
        'profile_img': personal.get('profile_img') or '/static/images/profile.jpg',
        'languages': resume_data.get('languages', []),
        'hobbies': resume_data.get('hobbies', []),
        'services': resume_data.get('services', []),
        'testimonials': resume_data.get('testimonials', []),
        'skill_levels': resume_data.get('skill_levels', {}),
        'experience': experience,
        'education': education
    }

    return jsonify(resume)

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
