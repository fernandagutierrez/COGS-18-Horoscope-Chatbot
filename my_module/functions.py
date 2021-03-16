def your_birth_date(month, day):
    """Get birthdate from user, to later on determine zodiac sign.
    Parameters
    ----------
    month: string
        The users brith month
    day: integer
        The users birth day.
    Returns
    -------
    string
        the birthdate of user.
    """
    return 'Your date of birth is', month, day, '.'
    
# This will check the day and month of the person in order to assign their sign.
def your_zodiac_sign(month, day):
    """Assign zodiac sign to user.
    Parameters
    ----------
    month: string
        The users birth month. 
    day: integer
        The users day of birth.
    Returns
    -------
    string
        the assigned zodiac sign of the user.
    """
    your_zodiac = ''
# zodiac dates can be confusing, for example Sagittarius is from November 21 to December 22. This is why I made the 'if (day <22) else ...'. That way I would minimize the amount of code lines needed.
    if month == 'December': 
        your_zodiac = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 'January': 
        your_zodiac = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 'Feburary': 
        your_zodiac = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 'March': 
        your_zodiac = 'Pisces' if (day < 21) else 'aries'
    elif month == 'April': 
        your_zodiac = 'Aries' if (day < 20) else 'taurus'
    elif month == 'May': 
        your_zodiac = 'Taurus' if (day < 21) else 'gemini'
    elif month == 'June':
        your_zodiac = 'Gemini' if (day < 21) else 'cancer'
    elif month == 'July':
        your_zodiac = 'Cancer' if (day < 23) else 'leo'
    elif month == 'August': 
        your_zodiac = 'Leo' if (day < 23) else 'virgo'
    elif month == 'September':
        your_zodiac = 'Virgo' if (day < 23) else 'libra'
    elif month == 'October':
        your_zodiac = 'Libra' if (day < 23) else 'scorpio'
    elif month == 'November': 
        your_zodiac = 'Scorpio' if (day < 22) else 'sagittarius'
    else: 
        None 
    return your_zodiac

# based off the users zodiac sign, they are told what zodiac sign they are most and least compatible with. 
def zodiac_compatability(your_zodiac):
    """ Will determine who they are most and least compatible with based of their sign.
    Parameters
    ----------
    your_zodiac: string
    Returns
    -------
    strings
      Who they are the most compatible. 
      Who they are the least compatible.
    """
    most_compatible = ''
    least_compatible = ''
    if your_zodiac == 'Sagittarius':
        most_compatible += 'Aquarius'
        least_compatible += 'Taurus'
    elif your_zodiac == 'Capricorn':
        most_compatible += 'Virgo'
        least_compatible += 'Gemini'
    elif your_zodiac == 'Aquarius':
        most_compatible += 'Sagittarius'
        least_compatible += 'Cancer'
    elif your_zodiac == 'Pisces':
        most_compatible = 'Scorpio'
        least_compatible = 'Virgo'
    elif your_zodiac == 'Aries':
        most_compatible += 'Libra'
        least_compatible += 'Taurus'
    elif your_zodiac == 'Taurus':
        most_compatible += 'Scorpio'
        least_compatible += 'Sagittarius'
    elif your_zodiac == 'Gemini':
        most_compatible += 'Sagittarius'
        least_compatible += 'Capricorn'
    elif your_zodiac == 'Cancer':
        most_compatible += 'Taurus'
        least_compatible += 'Aquarius'
    elif your_zodiac == 'Leo':
        most_compatible += 'Sagittarius'
        least_compatible += 'Scorpio'
    elif your_zodiac == 'Virgo':
        most_compatible += 'Scorpio'
        least_compatible += 'Sagittarius'
    elif your_zodiac == 'Libra':
        most_compatible += 'Libra'
        least_compatible += 'Virgo'
    elif your_zodiac == 'Scorpio':
        most_compatible += 'Pisces'
        least_compatible += 'Aries'
    else:
        None
    
    print('You are most compatible with', most_compatible, '.')
    print('You are least compatible with', least_compatible, '.')
      
# Will initiate chatbot.
## Was taken from the code style lecture.
def start_the_chat():
    print('Hello, do you want to know your zodiac?')
    
    response = input()
    
    if response != 'Yes':
        return 
    have_a_chat()

#main function to run chatbot.
## inspired from the code style lecture.
def have_a_chat():
    
    chat = True

    while chat:
        
        #check ask_zodiac
        month = input('What month were you born? \n')
        day = int(input('What day were you born? \n'))
        your_birth_date(month, day)
        sign = your_zodiac_sign(month,day)
        print('Your date of birth is', month, day)
        
        #print zodiac
        print('Your zodiac sign is', sign)
        
        #gives user compatibility
        msg = input('Do you want to know who you are the most and least compatible with? \n')
        if msg == 'Yes':
            zodiac_compatability(sign)
            
        #exit chatbot
        exit_code = input('Do you want to exit? \n')
        
        if exit_code == 'Yes':
            print('Okay, bye!')
            break        