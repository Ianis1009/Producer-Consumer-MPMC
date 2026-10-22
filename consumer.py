import time
import random
from buffer import get

def consumer (consumer_id):
    while True:
        item = get()
        if item is None:
            print(f"Consumatorul {consumer_id} se opreste.")
            break

        print(f"Consumatorul {consumer_id} proceseaza {item}")
        time.sleep(random.uniform(0.01, 0.99))

        