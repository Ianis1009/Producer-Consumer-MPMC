import threading

from producer import producer
from consumer import consumer
from buffer import put

NUM_PRODUCERS = 3
NUM_CONSUMERS = 2
ITEMS_PER_PRODUCER = 10


def main():
    producers = []
    consumers = []

    for i in range(NUM_CONSUMERS):
        t = threading.Thread(target=consumer, args=(i, ))
        consumers.append(t)

    for i in range(NUM_PRODUCERS):
        t = threading.Thread(target=producer, args=(i, ITEMS_PER_PRODUCER))
        producers.append(t)

    for t in consumers:
        t.start()
    for t in producers:
        t.start()

    for t in producers:
        t.join()

    for _ in range(NUM_CONSUMERS):
        put(None)

    for t in consumers:
        t.join()

    print("[INFO]: Toate thread-urile au terminat")



if __name__ == "__main__":
        main()
        

    