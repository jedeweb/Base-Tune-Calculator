#
#Math for the tune is from Diquee's of r/ForzaOpenTunes spreadsheet. Had an ongoing copy I made myself, and decided
#to evolve it into this to teach myself Python.
import variables
import functions
import sys


#get input for car variables and set tune

while True:
    print("""Please choose an option:
    1. Set base tune
    2. Change weight unit
    3. Change variables - debug
    4. Exit
    """)  
    MenuChoices = ['1','2','3', '4']
    MenuSelection = input('Enter Selection:')
    while True:
        if MenuSelection in MenuChoices:
            break
        else:
            MenuSelection = input ('Please input a valid selection, 1-4: ')

    if MenuSelection == '1': # Set base tune
        functions.GetTuneInputs()
        print('\n')
        print ('Front Spring: '+ str(round(variables.Tune['SpringFrontLb'],1)) + ' lb/in')
        print ('Rear Spring: '+ str(round(variables.Tune['SpringRearLb'],1)) + ' lb/in')
        print ('Front ARB: '+ str(round(variables.Tune['ArbFront'],1)))
        print ('Rear ARB: '+ str(round(variables.Tune['ArbRear'],1)))
        print ('Front Rebound: ' + str(round(variables.Tune['ReboundFront'],1)))
        print ('Rear Rebound: ' + str(round(variables.Tune['ReboundRear'],1)))
        print ('Front Bump: '+ str(round(variables.Tune['BumpFront'],1)))
        print ('Rear Bump: '+ str(round(variables.Tune['BumpRear'],1)))
        input ('Press any key to continue')
    elif MenuSelection == '2': # Change weight unit
        print ('Thank you Mario! But our princess is in another castle......')
    elif MenuSelection == '3': #Change variables
        print ('Thank you Mario! But our princess is in another castle......')
    elif MenuSelection == '4': # Exit
        sys.exit('Thank you, come again.')
         


