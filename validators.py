def fio(raw):
    parts = raw.split()
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать хотя бы два слова")
    return " ".join(piece.capitalize() for piece in parts)

def email(raw):
    value = raw.strip().lower()
    if value.count("@") != 1 or any(c.isspace() for c in value):
        raise ValueError("некорректный адрес почты")
    name, host = value.split("@")
    if not name or not host or "." not in host:
        raise ValueError("в адресе не хватает логина или домена")
    if host[0] == "." or host[-1] == ".":
        raise ValueError("недопустимая точка в домене")
    return value

def phone(raw):
    number = "".join(symbol for symbol in raw if symbol.isdigit())
    if len(number) != 11:
        raise ValueError(f"получено {len(number)} цифр, требуется 11")
    if number[0] not in ("7", "8"):
        raise ValueError("телефон должен начинаться с 7 или 8")
    return "7" + number[1:]

def group(raw):
    value = "".join(raw.split()).lower()
    if not value:
        raise ValueError("группа отсутствует")
    return value

def parse_line(line):
    columns = line.split(";")
    if len(columns) != 4:
        return None, f"найдено {len(columns)} полей вместо четырёх"
    try:
        person = dict(zip(("fio", "email", "phone", "group"),
                          (fio(columns[0]), email(columns[1]),
                           phone(columns[2]), group(columns[3]))))
    except ValueError as error:
        return None, str(error)
    return person, None

if __name__ == "__main__":
    print(parse_line("Орлов Максим;orlov@post.ru;89112223344;09с41"))
