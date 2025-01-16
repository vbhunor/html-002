import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def read_html():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

def test_html_title(read_html):
    soup = BeautifulSoup(read_html, "html.parser")
    assert soup.title.string == "Két fűzfa"

def test_header_and_paragraphs(read_html):
    soup = BeautifulSoup(read_html, "html.parser")
    
    # Ellenőrizzük, hogy a <h1> helyes címeket tartalmaz
    h1 = soup.find("h1")
    assert h1 and h1.text.strip() == "Két fűzfa"
    
    # Ellenőrizzük a három bekezdést
    h2_tags = soup.find_all("h2")
    assert len(h2_tags) == 3
    assert h2_tags[0].text.strip() == "A jövedelem"
    assert h2_tags[1].text.strip() == "A kollégium"
    assert h2_tags[2].text.strip() == "Az orákulum"
    
    p_tags = soup.find_all("p")
    assert len(p_tags) == 3
    
    # Ellenőrizzük, hogy a harmadik bekezdésben kiemelt-e a "bevette magát"
    assert "<strong>bevette magát</strong>" in str(p_tags[2])
    
    # Ellenőrizzük, hogy a második bekezdésben dőlt szöveg van-e
    assert "<em>időszerint</em>" in str(p_tags[1])

def test_html_language(read_html):
    soup = BeautifulSoup(read_html, "html.parser")
    html_tag = soup.find("html")
    assert html_tag and html_tag.get("lang") == "hu"
