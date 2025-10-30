from oop.BankDetails import BankDetails

class Credit_Card(BankDetails):
    def __init__(self,custid,cname,bal,credit_score,status):
        super().__init__(custid,cname,bal)
        self.credit_score = credit_score
        self.status = status

    def Welcome_message(self):
        print(f' welcome to SBI,{self.cname}')

    def cc_details(self):
        print(f'{self.credit_score} - {self.status}')