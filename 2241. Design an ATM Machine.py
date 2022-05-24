class ATM:

    def __init__(self):
        self.map2={20: 0, 50: 0, 100: 0, 200: 0, 500: 0}


    def deposit(self, banknotesCount):
        currency = [20, 50, 100, 200, 500]
        dummy=dict(zip(currency,banknotesCount))
        dum_keys=dummy.keys()
        for keys in dum_keys:
            if keys in self.map2:
                self.map2[keys]=self.map2[keys]+dummy[keys]
            else:
                self.map2[keys]=dummy[keys]




    def withdraw(self, amount):
        count=0
        self.map=self.map2.copy()
        self.result = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
        res=[True if x==0 else False  for x in self.map.values()  ]
        empty=all(res)
        if empty:
            return -1
        while amount>0:
            key_less = [x for x, y in self.map.items() if x <= amount and y != 0]
            if len(key_less)==0:
                return -1
            max_amount=max(key_less)
            amount=amount-max_amount
            count+=1
            self.map[max_amount]=self.map[max_amount]-1

            self.result[max_amount]=self.result[max_amount]+1

            if self.map[max_amount] == 0:
                del self.map[max_amount]
                key_less.remove(max_amount)
            if amount==0:
                break
        self.map2=self.map.copy()
        return self.result







atm=ATM()
atm.deposit([0,0,1,2,1])
print(atm.withdraw(600))
atm.deposit([0,1,0,1,1])
print(atm.withdraw(600))
print(atm.withdraw(550))


