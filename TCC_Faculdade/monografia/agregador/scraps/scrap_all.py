from scraps import scrap_imo1, scrap_imo2, scrap_imo3, scrap_imo4, scrap_imo5


def main():
    try:
        scrap_imo1.main()
    except Exception as erro:
        print(erro)

    try:
        scrap_imo2.main()
    except Exception as erro:
        print(erro)

    try:
        scrap_imo3.main()
    except Exception as erro:
        print(erro)

    try:
        scrap_imo4.main()
    except Exception as erro:
        print(erro)

    try:
        scrap_imo5.main()
    except Exception as erro:
        print(erro)


if __name__ == '__main__':
    main()
