import redis
import sys


def read_msgs():
    r = redis.Redis(host='redis', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    
    p.subscribe('redis_pub')
    for msg in p.listen():
        print(f"Received: {msg['data']}")
        break


def main():
    read_msgs()


if __name__ == '__main__':
    main()

