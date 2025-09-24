import os

# Subjects and number of chapters
subjects = {
    "science": 18,
    "math": 8,
    "history": 16,
    "geography": 10,
    "civics": 10,
    "english": 10,
    "poetry": 8,
    "hindi": 13
}

# HTML template for dayX.html
def day_html_template(subject_name, chapter_num):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_name.capitalize()} Chapter {chapter_num} Day {chapter_num}</title>
    <style>
        .btn {{
            background: linear-gradient(90deg, #00e5ff, #1de9b6);
            padding: 12px 28px;
            border: none;
            border-radius: 30px;
            font-size: 1.2rem;
            color: black;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            text-decoration: none;
            margin: 10px;
        }}
        .btn:hover {{
            transform: scale(1.1);
            box-shadow: 0 0 20px #00e5ff;
        }}
    </style>
</head>
<body>
    <h1>{subject_name.capitalize()} Chapter {chapter_num} Day {chapter_num}</h1>
    <p>Content goes here...</p>
    <a href="qns.html" class="btn">Go to qns page</a>
</body>
</html>
"""

# HTML template for qns.html
def qns_html_template(subject_name, chapter_num):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_name.capitalize()} Chapter {chapter_num} Questions</title>
</head>
<body>
    <h1>Questions for {subject_name.capitalize()} Chapter {chapter_num}</h1>
    <p>Questions content goes here...</p>
</body>
</html>
"""

# Create folders and files
for subject, chapters in subjects.items():
    os.makedirs(subject, exist_ok=True)
    for i in range(1, chapters + 1):
        chap_folder = os.path.join(subject, f"{i}chap")
        os.makedirs(chap_folder, exist_ok=True)

        # Create dayX.html with full HTML and button
        day_file = os.path.join(chap_folder, f"day{i}.html")
        with open(day_file, "w", encoding="utf-8") as f:
            f.write(day_html_template(subject, i))

        # Create qns.html
        qns_file = os.path.join(chap_folder, "qns.html")
        with open(qns_file, "w", encoding="utf-8") as f:
            f.write(qns_html_template(subject, i))

print("All subjects and chapters created with full dayX.html and qns.html files!")
