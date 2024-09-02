from singleton_meta import SingletonMeta

class ClickCounter(metaclass=SingletonMeta):
    counter = 0
    
    def click(cls):
        cls.counter += 1
