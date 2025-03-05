from abc import ABC,abstractmethod
class Employe(ABC):
    @abstractmethod
    def role(self):
        pass
class Empcompany(Employe):
    def role(self):
        return "Full Stack Dev"
e1=Empcompany()
print(e1.role())    