#FIND BIRTH INFO WITHOUT USING 
#MODULES FOR FISCAL CODE
import datetime
fiscal_code = 'RSSMRA80E04A010U'
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
yearFromDate = int(date.strftime("%y"))
#MAX YEAR 2099
def mapFiscalCode(val,case):
    if(case == 'sex'):
        ####### START ########
        ###CHECK USER SEX
        if(int(sex) > 40):
            return 'F'
        elif(int(sex) <= 40 and int(sex) >= 1 ):
            return 'M'
        else:
            return 'Sex Error'
        ####### END ########
    elif(case == 'day'):
        ####### START ########
        ###CHECK USER BIRTH DAY
        if(int(day) > 40):
            return int(day) - 40
        elif(int(day) <= 31 and int(day) >= 1):
            return day
        else: 
            return 'Day error'
        ####### END ########
    elif(case == 'month'):    
        ####### START ########
        ###CHECK BIRTH MONTH
        if(month == 'A'):
            return 'Gennaio'
        elif(month == 'B'):
            return 'Febbraio'
        elif(month == 'C'):
            return 'Marzo'
        elif(month == 'D'):
            return 'Aprile'
        elif(month == 'E'):
            return 'Maggio'
        elif(month == 'H'):
            return 'Giugno'
        elif(month == 'L'):
            return 'Luglio'
        elif(month == 'M'):
            return 'Agosto'
        elif(month == 'P'):
            return 'Settembre'
        elif(month == 'R'):
            return 'Ottobre'
        elif(month == 'S'):
            return 'Novembre'
        elif(month == 'T'):
            return 'Dicembre'
        else:
            return 'Month error'
        ####### END ########
    elif(case == 'year'):
        ###CHECK USER BIRTH YEAR
        ####### START ########
        if(int(year) > yearFromDate):
            return f'{19}{year}'
        elif(int(year) > 0 and int(year) <= yearFromDate):
            return f'{20}{year}'
        else:
            return 'Year Error'
        ####### END ########
    else:
        return 'System Error'

month = fiscal_code[8]
day = fiscal_code[9:11]
year = fiscal_code[6:8]
sex = day
#month
print(f'Birth Month: {mapFiscalCode(month,"month")}')
#sex
print(f'Sex: {mapFiscalCode(sex,"sex")}')
#birthdate
print(f'Birth Day: {mapFiscalCode(day,"day")}')
#year
print(f'Birth Year: {mapFiscalCode(year,"year")}')
#recap
print(f'Birth date: {mapFiscalCode(day,"day")}-{mapFiscalCode(month,"month")}-{mapFiscalCode(year,"year")}')