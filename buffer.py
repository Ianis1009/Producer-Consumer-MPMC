import threading

CAPACITY = 5

buffer = []
head = 0
tail = 0

mutex = threading.Lock()
empty = threading.Semaphore(CAPACITY)

full = threading.Semaphore(0)
buffer = [None] * CAPACITY

def put(item):
    global tail
    empty.acquire()
    mutex.acquire()
    buffer[tail] = item
    tail = (tail + 1) % CAPACITY
    print(f"[PUT] {item}")
    mutex.release()
    full.release()


def get():
    global head
    full.acquire()
    mutex.acquire()

    item = buffer[head]
    buffer[head] = None
    head = (head + 1) % CAPACITY
    print(f"[GET] {item}")
    mutex.release()
    empty.release()
    return item