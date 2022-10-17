

class Singleton(type):

    def __ini__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance 


class DBManager(metaclass=Singleton):
    
    def __init__(self) -> None:
        """
        run session and connect to the data base
        """
        pass