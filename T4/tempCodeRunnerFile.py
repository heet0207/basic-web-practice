from abc import ABC,abstractmethod,abstractproperty
class shape(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def draw(self):
        pass
    @abstractproperty
    def n(self):
        pass

class Circle(shape):
    def __init__(self):
        super().__init__('Circle')
    def draw(self):
        print('Draw a Circle')
    @property
    def n(self):
        return self.name

c=Circle()
c.draw()
c.n
isinstance(c,Circle)
issubclass(Circle,shape)