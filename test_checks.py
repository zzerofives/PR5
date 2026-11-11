from pathlib import Path
from validators import fio, email, phone, parse_line
from storage import load
from report import hide_number

def test_fio():
    assert fio("  бЕлова   аЛина ") == "Белова Алина"

def test_email():
    assert email(" USER@POST.RU ") == "user@post.ru"

def test_phone():
    assert phone("8 (921) 123-45-67") == "79211234567"

def test_errors():
    person, error = parse_line("Петров Игорь;bad.email;89112223344;09с41")
    assert person is None and error

def test_input():
    path = Path(__file__).with_name("anketa.txt")
    good, bad, count = load(path)
    assert len(good) >= 5
    assert len(bad) >= 4
    assert count >= 10

def test_mask():
    assert hide_number("79112223344") == "+7 (911) ***-**-44"
