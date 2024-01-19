from typing import Callable, Type, get_type_hints

type FnRetNone = Callable[..., None]

class Signal:
    def __init__(self, *args) -> None:
        self.param_types = list(args)
        self.callables: list[FnRetNone] = []

    def __get__[T](self, inst: T, inst_type: Type[T]):
        if not inst:
            raise AttributeError("The attribute does not exist. Are you sure you intialized the class?")
        return self
    
    def connect(self, func: FnRetNone):
        if self.param_types != list(get_type_hints(func).values()):
            raise TypeError("The function type does not match the expected types by the signal.")
        self.callables.append(func)
    
    def disconnect(self, func: FnRetNone):
        if self.param_types != list(get_type_hints(func).values()):
            raise TypeError("The function type does not match the expected types by the signal.")
        self.callables.remove(func)
    
    def emit(self, *args):
        for callable in self.callables:
            callable(*args)


def signal(*args) -> Signal:
    return Signal(*args)


if __name__ == '__main__':
    class TestObject:
        test_signal = signal(int)

        def cool(self):
            self.test_signal.emit(10)

    def test_fn(test: int):
        print(test)

    test = TestObject()
    test.test_signal.connect(test_fn)
    test.cool()
