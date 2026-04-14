import os

files = [
    ".flaskenv", "config.py", "project_structure.md", "README.md", "requirements.txt",
    "travel/forms.py", "travel/models.py", "travel/__init__.py",
    "travel/static/admin.js", "travel/static/main.js", "travel/static/notice.js", "travel/static/sub2.js",
    "travel/static/css/headfoot.css", "travel/static/css/style.css", "travel/static/css/sub2.css", "travel/static/css/travel_detail.css",
    "travel/templates/base.html", "travel/templates/form_errors.html", "travel/templates/main.html",
    "travel/templates/admin/register_form.html", "travel/templates/auth/login.html", "travel/templates/auth/signup.html",
    "travel/templates/comment/answer_form.html", "travel/templates/notice/question_detail.html", "travel/templates/notice/question_form.html",
    "travel/templates/review/review_form.html", "travel/templates/sub/sub2.html", "travel/templates/sub/travel_detail.html",
    "travel/views/answer_views.py", "travel/views/auth_views.py", "travel/views/main_views.py",
    "travel/views/question_views.py", "travel/views/register_views.py", "travel/views/review_views.py", "travel/views/sub_views.py"
]

output_file = "full_project_code_study.md"

lang_map = {
    ".py": "python",
    ".html": "html",
    ".css": "css",
    ".js": "javascript",
    ".md": "markdown",
}

with open(output_file, "w", encoding="utf-8") as f:
    for file_path in files:
        # Standardize path for current OS
        normalized_path = os.path.normpath(file_path)
        if os.path.exists(normalized_path):
            print(f"Processing {normalized_path}")
            ext = os.path.splitext(normalized_path)[1].lower()
            lang = lang_map.get(ext, "text")
            
            f.write(f"### [{file_path}]\n")
            f.write(f"```{lang}\n")
            try:
                with open(normalized_path, "r", encoding="utf-8") as file_content:
                    f.write(file_content.read())
            except UnicodeDecodeError:
                # Handle cases where utf-8 might fail, though these should be text files
                with open(normalized_path, "r", encoding="cp949") as file_content:
                    f.write(file_content.read())
            except Exception as e:
                f.write(f"Error reading file: {e}")
                
            f.write("\n```\n\n")
        else:
            print(f"Warning: File not found: {normalized_path}")
