from collections import Counter

def hide_number(number):
    return f"+7 ({number[1:4]}) ***-**-{number[-2:]}"

def show(people, mistakes, all_lines):
    people = sorted(people, key=lambda person: person["fio"])
    print(f"{'№':>2} {'ФИО':<30} {'Почта':<25} {'Группа':<8} Телефон")
    print("-" * 88)
    for index, person in enumerate(people, 1):
        print(f"{index:>2} {person['fio'][:30]:<30} "
              f"{person['email'][:25]:<25} {person['group']:<8} "
              f"{hide_number(person['phone'])}")
    print("-" * 88)
    print(f"Всего строк: {all_lines}")
    print(f"Принято: {len(people)}. Отклонено: {len(mistakes)}.")
    if mistakes:
        print("\nНекорректные записи:")
        for number, cause, raw in mistakes:
            print(f"  {number}: {cause}\n     {raw}")
    print("\nПо учебным группам:")
    for group, count in sorted(Counter(item["group"] for item in people).items()):
        print(f"  {group}: {count}")

if __name__ == "__main__":
    print("report.py показывает обработанные анкеты")
    # Подсчёт анкет по доменам почты
    domains = {}

    for person in people:
        domain = person["email"].split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

    print("\nПо доменам электронной почты:")
    for domain, count in sorted(domains.items()):
        print(f"  {domain}: {count}")