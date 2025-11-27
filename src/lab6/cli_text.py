import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n


def main():

    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")

    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Количество топовых слов " "(по умолчанию: 5)",
    )
    cat_parser = subparsers.add_parser("cat", help="Вывод содержимого файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    args = parser.parse_args()

    file = Path(args.input)

    if not file.exists():
        parser.error("Файл не найден")

    if args.command == "cat":
        with open(file, "r", encoding="utf-8") as f:
            number = 1
            for row in f:
                row = row.rstrip("\n")
                if (args.n):
                    print(f"{number}: {row}")
                    number += 1
                else:
                    print(row)

    elif args.command == "stats":
        with open(file, "r", encoding="utf-8") as f:
            data = [row for row in f]
        data = "".join(data)
        tokens = tokenize(text=data)
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)


        number = 1
        for x, y in top:
            print(f"{number}. {x} - {y}")
            number += 1


if __name__ == "__main__":
    main()