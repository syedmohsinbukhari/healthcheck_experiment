import redis
from time import sleep


def publish_it():
    r = redis.Redis(host='redis', port=6379, db=0)

    i = 0
    while True:
        print(i, flush=True)
        r.publish('redis_pub', i)
        sleep(1)
        i += 1
        if i > 60:
            break


def main():
    while True:
        publish_it()
        sleep(60)


if __name__ == '__main__':
    main()

