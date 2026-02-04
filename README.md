# Professional Dynamic Resume - Python & HTML

This project is a **Dynamic Resume System** that separates data (Python) from design (HTML). It allows you to maintain your resume content in a simple Python dictionary and render it into a high-quality, professional document.

## How Dictionary Data Flows

### 1. The Data Source (`data.py`)
All your professional information is stored in a structured Python dictionary. This includes nested lists for skills, experience points, and testimonials.

```python
resume_data = {
    "personal_info": { "name": "Engr. Shuvo Das", ... },
    "skills": [ {"name": "Python", "level": 95}, ... ],
    "experience": [ { "role": "Engineer", "points": ["..."] }, ... ]
}
```

### 2. The Backend Bridge (`app.py`)
Using **Flask**, we import the dictionary and pass it to the HTML templates. This makes the data available as variables within the HTML.

```python
@app.route('/document')
def document():
    return render_template('document.html', personal=resume_data['personal_info'], skills=resume_data['skills'])
```

### 3. The Frontend Display (`templates/`)
We use **Jinja2** syntax to dynamically create the resume.

- **Direct Variables**: `{{ personal.name }}` displays the name.
- **Loops**: `{% for skill in skills %}` creates a new skill bar for every item in your dictionary.
- **Lists**: `{% for point in job.points %}` renders your experience bullet points.

## Project Structure
- `app.py`: The brain of the app that handles routing.
- `data.py`: The single source of truth for your resume data.
- `static/style.css`: Professional 2-column resume styling.
- `templates/`:
    - `layout.html`: The structural skeleton.
    - `index.html`: A clean landing summary.
    - `document.html`: The full, detailed professional resume.

## How to Run
1. Install Flask: `pip install flask`
2. Run the app: `python app.py`
3. Visit: `http://127.0.0.1:5000`
4. Click **Download PDF** on the Resume page to save a professional copy!