import time
import random
from buffer import put

def producer (producer_id, items_count):
    for i in range(items_count):
        item =  (producer_id, i)
        put(item)
        time.sleep(random.uniform(0.01, 0.99))
    print(f"Producatorul {producer_id}  a terminat de produs resursa.")