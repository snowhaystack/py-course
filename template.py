##VARIABLE INIT
cursor = 0
desc = 'section'
##FUNCTION SECTION
def endTest(cursor):
    ####### START ########
    cursor += 1
    print(f'{"END ------> "}{cursor}')
    print('')
    return cursor
    ###### END ##########
def startTest(cursor,desc):
    ####### START ########
    cursor += 1
    print(f'START ------> {cursor} {desc} ')
    ###### END ##########
##USAGE XAMPLE
##########################
startTest(cursor ,desc)
cursor = endTest(cursor)

##########################
startTest(cursor ,desc)
cursor = endTest(cursor)

##########################
startTest(cursor ,desc)
cursor = endTest(cursor)
##END USAGE EXAMPLE