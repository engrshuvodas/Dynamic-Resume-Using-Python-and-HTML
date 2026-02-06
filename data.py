# Resume Data Dictionary
# This file serves as the main data source for the resume.
# Data is stored in a clean, organized dictionary format.

resume_data = {
    "personal_info": {
        "name": "Engr. Shuvo Das",
        "title": "Full-Stack Software Engineer & Automation Expert",
        "email": "engrshuvoda@gmail.com",
        "phone": "+880 1765-245872",
        "location": "Gujarat, India",
        "summary": "Innovative Software Engineer with over 8 years of experience in building high-performance web applications and automation tools. Specialist in WhatsApp marketing software and custom desktop solutions. Proven track record of delivering 150+ successful projects for global clients.",
        "profile_img": "Shuvo.jpg",
        # set to the static image path used by the template
        "profile_img": "/static/images/profile.jpg",
        "github": "github.com/engrshuvodas",
        "linkedin": "linkedin.com/in/engrshuvodas",
        "website": "www.shuvodas.com"
    },
    "skills": [
        {"name": "Python & Flask", "category": "Backend"},
        {"name": "JavaScript & React", "category": "Frontend"},
        {"name": "HTML5 & CSS3", "category": "Frontend"},
        {"name": "Database Management", "category": "Infrastructure"},
        {"name": "WhatsApp API & Automation", "category": "Specialized"},
        {"name": "Desktop App Dev (PyQt/Electron)", "category": "Specialized"}
    ],
    "experience": [
        {
            "role": "Senior Software Engineer",
            "company": "Freelance Global Solutions",
            "period": "2018 - Present",
            "description": "Leading the development of custom automation tools and high-traffic web platforms for international clients.",
            "achievements": [
                "Architected a WhatsApp Marketing suite used by 500+ businesses.",
                "Reduced client manual workload by 70% through intelligent automation.",
                "Maintained a 100% project completion rate on Upwork and Freelancer."
            ]
        },
        {
            "role": "Full-Stack Developer",
            "company": "TechInnovate Ltd",
            "period": "2015 - 2018",
            "description": "Developed and maintained corporate websites and internal CRM systems.",
            "achievements": [
                "Modernized legacy PHP systems to modern Python-based architectures.",
                "Optimized database queries, improving load times by 40%."
            ]
        }
    ],
    "education": [
        {
            "degree": "B.Tech in Computer Science & Engineering",
            "institution": "Parul University",
            "year": "2014",
            "details": "Focused on Software Engineering, Data Structures, and Algorithmic Design."
        },
        {
            "degree": "Diploma in Computer Technology",
            "institution": "Technical Institute",
            "year": "2010",
            "details": "Foundational studies in computer hardware and networking."
        }
    ],
    "projects": [
        {
            "name": "WASenderPro",
            "description": "A comprehensive WhatsApp marketing automation tool with lead extraction and personalized messaging capabilities.",
            "link": "https://github.com/engrshuvodas/WASenderPro"
        },
        {
            "name": "Dynamic Resume Builder",
            "description": "A Flask-based application that generates professional resumes from raw JSON/Dictionary data.",
            "link": "#"
        }
    ],
    "contact_info": {
        "whatsapp": "+8801765245872",
        "address": "123 Tech Avenue, Gujarat, India",
        "availability": "Open for Global Contracts"
    }
}
