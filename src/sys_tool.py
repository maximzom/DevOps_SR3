import sys

USAGE = """Використання: python src/sys_tool.py [--help]

Друкує рядок «командна строка», якщо сценарій запущено напряму.
При імпорті як модуля нічого не друкується.

Опції:
  -h, --help   показати цю довідку
"""


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if "-h" in argv or "--help" in argv:
        print(USAGE)
        return
    print("командна строка")


if __name__ == "__main__":
    main()
