from bs4 import BeautifulSoup

html = """
<h1> My Firat Web scraper </h1>

<p>learning python is fun</p>
"""
soup = BeautifulSoup(html, "html.parser")

heading = soup.find("h1")

print(heading.text)


html = """
<h1>Python Zero to Hero</h1>
<h2>Learn Python</h2>
<p>Python is easy to learn.</p>
<p>Practice makes you better.</p>
"""

soup = BeautifulSoup(html, "html.parser")

headings = soup.find_all(["h1", "h2"])

for heading in headings:
    print(heading.text)

paragraphs = soup.find_all("p")

for paragraph in paragraphs:
    print(paragraph.text)
