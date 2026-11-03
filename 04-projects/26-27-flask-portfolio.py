from flask import Flask, render_template_string

app = Flask(__name__)

# HTML
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #101820;
            color: white;
            line-height: 1.6;
        }

        nav {
            background: #17232e;
            padding: 20px;
            display: flex;
            justify-content: space-between;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 10px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        .hero {
            text-align: center;
            padding: 100px 20px;
        }

        .hero h1 {
            color: #00d4ff;
            font-size: 40px;
        }

        .btn {
            display: inline-block;
            background: #00d4ff;
            color: black;
            padding: 10px 20px;
            margin-top: 20px;
            text-decoration: none;
            border-radius: 5px;
        }

        section {
            padding: 50px 10%;
            text-align: center;
        }

        section h2 {
            color: #00d4ff;
            margin-bottom: 20px;
        }

        .project {
            background: #17232e;
            padding: 20px;
            margin: 15px auto;
            max-width: 500px;
            border-radius: 10px;
        }

        footer {
            background: #17232e;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>

<body>

    <nav>
        <h2>My Portfolio</h2>

        <div>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <div class="hero">
        <h1>Hello, I'm Uma!</h1>

        <h2>First-Year CSE Student</h2>

        <p>
            I'm learning programming and building
            projects using Python and C.
        </p>

        <a href="#projects" class="btn">
            View My Projects
        </a>
    </div>

    <section id="about">
        <h2>About Me</h2>

        <p>
            I'm a Computer Science student interested
            in software development, technology
            and problem-solving.
        </p>
    </section>

    <section id="skills">
        <h2>My Skills</h2>

        <p>C | Python | HTML | CSS | Flask</p>
    </section>

    <section id="projects">
        <h2>My Projects</h2>

        <div class="project">
            <h3>Expense Tracker</h3>
            <p>A Python application to track expenses.</p>
        </div>

        <div class="project">
            <h3>Number Guessing Game</h3>
            <p>A beginner-friendly game built using C.</p>
        </div>

        <div class="project">
            <h3>Student Management System</h3>
            <p>A C project to manage student records.</p>
        </div>
    </section>

    <section id="contact">
        <h2>Contact Me</h2>

        <p>Email: your-email@example.com</p>

        <p>GitHub: github.com/your-username</p>
    </section>

    <footer>
        <p>© 2026 My Portfolio | Built with Flask</p>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
