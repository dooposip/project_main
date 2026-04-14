$files = @(
    ".flaskenv", "config.py", "project_structure.md", "README.md", "requirements.txt",
    "travel\forms.py", "travel\models.py", "travel\__init__.py",
    "travel\static\admin.js", "travel\static\main.js", "travel\static\notice.js", "travel\static\sub2.js",
    "travel\static\css\headfoot.css", "travel\static\css\style.css", "travel\static\css\sub2.css", "travel\static\css\travel_detail.css",
    "travel\templates\base.html", "travel\templates\form_errors.html", "travel\templates\main.html",
    "travel\templates\admin\register_form.html", "travel\templates\auth\login.html", "travel\templates\auth\signup.html",
    "travel\templates\comment\answer_form.html", "travel\templates\notice\question_detail.html", "travel\templates\notice\question_form.html",
    "travel\templates\review\review_form.html", "travel\templates\sub\sub2.html", "travel\templates\sub\travel_detail.html",
    "travel\views\answer_views.py", "travel\views\auth_views.py", "travel\views\main_views.py",
    "travel\views\question_views.py", "travel\views\register_views.py", "travel\views\review_views.py", "travel\views\sub_views.py"
)

$outputFile = "full_project_code_study.md"
if (Test-Path $outputFile) { Remove-Item $outputFile }

foreach ($file in $files) {
    if (Test-Path $file) {
        $ext = [System.IO.Path]::GetExtension($file).ToLower()
        $lang = "text"
        if ($ext -eq ".py") { $lang = "python" }
        elseif ($ext -eq ".html") { $lang = "html" }
        elseif ($ext -eq ".css") { $lang = "css" }
        elseif ($ext -eq ".js") { $lang = "javascript" }
        elseif ($ext -eq ".md") { $lang = "markdown" }
        
        Write-Output "Processing $file"
        Add-Content -Path $outputFile -Value "### [$file]"
        Add-Content -Path $outputFile -Value "```$lang"
        $content = Get-Content -Path $file -Raw
        if ($null -ne $content) {
            Add-Content -Path $outputFile -Value $content
        }
        Add-Content -Path $outputFile -Value "```"
        Add-Content -Path $outputFile -Value ""
    } else {
        Write-Warning "File not found: $file"
    }
}
