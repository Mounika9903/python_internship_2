class Dad:
    def __init__(self, amount):
        self.amount = amount
 
    def dadWallet(self):
        print(f"Wallet amount of Dad: {self.amount}")
 
    def emptyPocket(self):
        self.amount = 0
        print("Dad's pocket is now empty.")
    
class Son(Dad):
    def __init__(self, sonWallet, amount):
        super().__init__(amount)  
        self.sonWallet = sonWallet
 
    def theft(self):
        self.sonWallet += self.amount
        print(f"Son wallet after theft: {self.sonWallet}")
 
    def theftAmount(self):
        print(f"The Amount Stolen: {self.sonWallet}")
        
class Grand_Son(Dad):
    def __init__(self,Grand_SonWallet,amount):
        super().__init__(amount)
        self.Grand_SonWallet=Grand_SonWallet 
    def theft(self):
        self.Grand_SonWallet+=self.amount
        print(f"Grand_Son wallet after theft: {self.Grand_SonWallet}")
    def theftAmount(self):
        print(f"The Amount Stolen: {self.Grand_SonWallet}")    
    def emptyPocket(self):
        self.amount = 0
        print("Son pocket is now empty.")   
    
                         
dada = Dad(10000)
dada.dadWallet()
s1 = Son(0,10000)
s1.theft()
dada.emptyPocket()
dada.dadWallet()
s1=Grand_Son(0,10000)
s1.theft()
dada.emptyPocket()
dada.dadWallet()