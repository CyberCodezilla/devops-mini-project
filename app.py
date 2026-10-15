from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>End-to-End DevOps Pipeline Mini Project</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f6f8fa; color: #0f172a; display:flex; align-items:center; justify-content:center; height:100vh; margin:0; }
    .card { background: white; padding: 2.5rem; border-radius: 12px; box-shadow: 0 6px 18px rgba(15,23,42,0.08); max-width:720px; text-align:center; }
    h1 { margin:0 0 0.5rem 0; font-size:1.6rem; color:#0b1320; }
    p { margin:0.25rem 0 1.25rem 0; color:#334155; }
    .badge { display:inline-block; padding:0.45rem 0.8rem; border-radius:999px; background:#10b981; color:white; font-weight:600; }
  </style>
</head>
<body>
  <div class="card">
    <h1>End-to-End DevOps Pipeline Mini Project</h1>
    <p>Managed in Jira | Hosted on GitHub | Built with GitHub Actions | Packaged with Docker</p>
    <div class="badge" role="status">Application Status: Running &amp; Verified</div>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML), 200

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "devops-mini-project"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
