class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("<new> creating")
        if not cls._instance:
            print("Instance not existing already.")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("<init> called")


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s1)
print(s1 is s2)
