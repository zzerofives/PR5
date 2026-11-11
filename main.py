from pathlib import Path
import sys
from storage import load, save
from report import show

def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("anketa.txt")
    try:
        people, mistakes, lines_count = load(source)
    except FileNotFoundError:
        print(f"Нет входного файла: {source}")
        return
    except (OSError, UnicodeError) as error:
        print(f"Не удалось открыть анкеты: {error}")
        return
    show(people, mistakes, lines_count)
    try:
        save(source.parent, people, mistakes)
    except OSError as error:
        print(f"Не удалось записать результаты: {error}")
        return
    print("\nФайлы ok.txt и errors.txt сохранены")

if __name__ == "__main__":
    main()
