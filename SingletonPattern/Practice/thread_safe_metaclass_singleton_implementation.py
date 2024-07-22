import threading


class ThreadSafeSingleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        print("<new call> creating.")
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__()
            return cls._instances[cls]


class Singleton(metaclass=ThreadSafeSingleton):
    def some_business_logic(self):
        pass


def get_instance():
    s1 = Singleton()
    print(s1)


threads = []
for i in range(10):
    t = threading.Thread(target=get_instance())
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()