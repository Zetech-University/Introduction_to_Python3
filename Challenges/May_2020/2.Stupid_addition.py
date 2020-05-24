
def stupid(here, there):
    if type(here) == int and type(there) == int:
        print(str(here) + str(there))
        # Concutinate 

    elif type(here) == str and type(there) == str:
        print(int(here) + int(there))
        # Add 

    else:
        print('None')
        # None 

stupid(3, 6)        #   Returns '36'
stupid('3', '6')    #   Returns  9
stupid(3, '6')      #   Returns 'None'