from pathlib import Path
from validators import parse_line

def load(filename):
    people = []
    mistakes = []
    lines = Path(filename).read_text(encoding="utf-8").splitlines()
    for line_no, line in enumerate(lines, 1):
        if not line.strip():
            continue
        item, problem = parse_line(line)
        if problem is None:
            people.append(item)
        else:
            mistakes.append((line_no, problem, line))
    return people, mistakes, len(lines)

def save(folder, people, mistakes):
    directory = Path(folder)
    people = sorted(people, key=lambda item: item["fio"])
    good_lines = []
    for item in people:
        good_lines.append(";".join(item[key] for key in ("fio", "email", "phone", "group")))
    bad_lines = []
    for number, reason, original in mistakes:
        bad_lines.append(f"Строка {number}: {reason}\n{original}")
    (directory / "ok.txt").write_text("\n".join(good_lines) + "\n", encoding="utf-8")
    (directory / "errors.txt").write_text("\n".join(bad_lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    print("storage.py отвечает за чтение и сохранение анкет")
