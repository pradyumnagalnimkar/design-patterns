class ClassicSingletion:
    _instance = None

    def __init__(self):
        print("initialised <init>")
        raise RuntimeError("Call getInstance() method.")

    @classmethod
    def getInstance(cls):
        print("Inside <getInstance> method")
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance


s1 = ClassicSingletion.getInstance()
s2 = ClassicSingletion.getInstance()

print(s1 is s2)

