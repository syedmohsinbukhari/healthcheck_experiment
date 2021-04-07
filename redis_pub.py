from time import sleep


def main():
    i = 0
    while True:
        print(i, flush=True)
        sleep(1)
        i += 1
        if i > 60:
            break


if __name__ == '__main__':
    main()

