class LogMixin:
    def log(self,message):
        print(f'Log:{message}')
class user(LogMixin):
    #def create_user(self,name):
        #self.log(f'user{name}created')
    def name(self,name):
        self.name=name
        print(self.name)    
user=user()
user.name('Sankar')                