# Dynamic Resume - Python & HTML Implementation

This project demonstrates how to build a dynamic resume application where the data is stored in **Python Dictionaries** and rendered into **HTML templates** using Flask.

## How it Works

### 1. Data Source (`data.py`)
All resume information is stored in a structured Python dictionary called `resume_data`. This makes it easy to update your resume in one place without touching the HTML structure.

```python
resume_data = {
    "personal_info": { "name": "...", "title": "..." },
    "skills": [...],
    "experience": [...]
}
```

### 2. Backend Logic (`app.py`)
The Flask application acts as the bridge. It imports the dictionary from `data.py` and passes specific parts of it to the HTML templates using the `render_template` function.

```python
@app.route('/')
def index():
    return render_template('index.html', personal=resume_data['personal_info'])
```

### 3. Frontend Rendering (`templates/`)
We use **Jinja2** (Flask's templating engine) to access the dictionary keys inside the HTML. 

- **Variables**: `{{ personal.name }}` grabs the value associated with the `name` key.
- **Loops**: `{% for skill in skills %}` iterates through a list of skills.
- **Logic**: `{% if title == 'Home' %}` allows for conditional styling.

## How to Run

1. Make sure you have Python installed.
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and go to: `http://127.0.0.1:5000`

## Project Structure
- `app.py`: Main backend entry point.
- `data.py`: Centralized resume data.
- `templates/`: HTML files (View layers).
- `static/`: CSS and assets for premium design.