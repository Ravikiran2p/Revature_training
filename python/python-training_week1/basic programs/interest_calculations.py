"""module for intrest Calculations"""
def simple_interest(p,t, r):
    si=p*t*r/100
    amount=p+si
    return si, amount

def compound_interest(p,t, r):
    """
    :param p: princioal amount
    :param ny: number of years
    :param r: rate of interest
    :return: si,amount
    """
    si=p*t*r/100
    amount=p*((1+(r/100))**(1*t))