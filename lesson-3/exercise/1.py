"""
- ask for a number to bet on 
- ask for the value of the wallet
- ask for an amount to bet 
- spin the roulette wheel 1000 times
- determine the value of the wallet
- if number drawn wins 36 times the stake otherwise loses bet 

"""

import random,logging,datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logDate = datetime.datetime.now()
logDate = logDate.strftime('%Y-%B-%d')
print(logDate)
handler = logging.FileHandler("./"+logDate + ".log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def roulette(min,max,wallet):
        ####### START ########
        for your_bet in range (min,max):
            extracted_number = int(random.randint(0,100))
            if(extracted_number == bet_number):
                wallet += bet * 36
            else:
                wallet -= bet
         
        return wallet
       
        ####### END ########
#init variables
bet = int(input('Enter bet amount:'))
wallet = int(input('Enter your wallet value:'))
bet_number = int(input('Enter your number:'))

if(bet > wallet):
    logger.debug('Error')
else:
    before_bet = wallet - bet
    logger.debug(f'your bet is: {bet}$, actually your wallet is: {before_bet}$')
    logger.debug(f'your bet is: {bet}$, after bet your wallet value is: {roulette(1,1000,wallet)}$')
   
