class BankDetails:
    def __init__(self,cusid,cname,bal):
        self._cid=cusid
        self._cname=cname
        self._bal=bal


    def Welcome_message(self):
        print("welcome to SBI")

    def display_details(self):
        print(f'{self.custid} - {self.c_name} - {self.bal}')

