##VARIABLE INIT
cursor = 0
desc = 'section'
##FUNCTION SECTION
def endTest():
    ####### START ########
    global cursor
    print(f'{"END ------> "}{cursor}')
    print('')
    return cursor
    ###### END ##########
def startTest(desc):
    ####### START ########
    global cursor
    cursor += 1
    print(f'START ------> {cursor} {desc} ')
    ###### END ##########
##USAGE XAMPLE
##########################

startTest(desc)
cursor = endTest()

##########################
startTest(desc)
cursor = endTest()

##########################
startTest(desc)
cursor = endTest()
##END USAGE EXAMPLE