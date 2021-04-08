import redis
from time import sleep


def sub_handler(message):
    print(message['data'], flush=True)


def read_msgs():
    r = redis.Redis(host='redis', port=6379, db=0)
    p = r.pubsub()
    
    p.subscribe(**{'redis_pub': sub_handler})
    while True:
        _ = p.get_message()
        sleep(0.05)


def main():
    read_msgs()


if __name__ == '__main__':
    main()

