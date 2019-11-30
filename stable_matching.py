'''
 ____  _        _     _      __  __       _       _     _                _    _                  _ _   _               
/ ___|| |_ __ _| |__ | | ___|  \/  | __ _| |_ ___| |__ (_)_ __   __ _   / \  | | __ _  ___  _ __(_) |_| |__  _ __ ___  
\___ \| __/ _` | '_ \| |/ _ \ |\/| |/ _` | __/ __| '_ \| | '_ \ / _` | / _ \ | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \ 
 ___) | || (_| | |_) | |  __/ |  | | (_| | || (__| | | | | | | | (_| |/ ___ \| | (_| | (_) | |  | | |_| | | | | | | | |
|____/ \__\__,_|_.__/|_|\___|_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, /_/   \_\_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|
                                                                |___/           |___/                                  

@Author: Ryan Schachte
@Publication-Date: 1/12/17 5:23 PM
@Update-Date: 30/11/19 5:37 PM - @Flavio Clesio
@Description: 

The stable matching algorithm seeks to solve the problem of finding a stable match between two sets of equal size
given a list of preferences for each element. 

We can define "matching" and "stable" by the following definitions.

Matching: Mapping from the elements of one set to the elements of another set
Stable: No element A of the first set that prefers an element B of the second set over its current partner
		such that element B prefers element A over its current partner. 
'''
# The women that the men prefer
preferred_rankings_men = {
    'ryan': ( 'lizzy' , 'sarah' , 'zoey' , 'daniella' ] ,
    'josh': ( 'sarah' , 'lizzy' , 'daniella' , 'zoey' ] ,
    'blake': ( 'sarah' , 'daniella' , 'zoey' , 'lizzy' ] ,
    'connor': ( 'lizzy' , 'sarah' , 'zoey' , 'daniella' ]
}

# The men that the women prefer
preferred_rankings_women = {
    'lizzy': [ 'ryan' , 'blake' , 'josh' , 'connor' ] ,
    'sarah': [ 'ryan' , 'blake' , 'connor' , 'josh' ] ,
    'zoey': [ 'connor' , 'josh' , 'ryan' , 'blake' ] ,
    'daniella': [ 'ryan' , 'josh' , 'connor' , 'blake' ]
}

# Keep track of the people that "may" end up together
tentative_engagements = [ ]

# Men who still need to propose and get accepted successfully
free_men = [ ]


def init_free_men():
    '''Initialize the arrays of women and men to represent
        that they're all initially free and not engaged'''
    for man in preferred_rankings_men.iterkeys():
        free_men.append(man)


def begin_matching(man):
    '''Find the first free woman available to a man at
        any given time'''

    print("DEALING WITH %s" % (man))
    for woman in preferred_rankings_men[ man ]:

        # Boolean for whether woman is taken or not
        taken_match = [ couple for couple in tentative_engagements if woman in couple ]

        if (len(taken_match) == 0):
            # tentatively engage the man and woman
            tentative_engagements.append([ man , woman ])
            free_men.remove(man)
            print('%s is no longer a free man and is now tentatively engaged to %s' % (man , woman))
            break

        elif (len(taken_match) > 0):
            print('%s is taken already..' % (woman))

            # Check ranking of the current dude and the ranking of the 'to-be' dude
            current_guy = preferred_rankings_women[ woman ].index(taken_match[ 0 ][ 0 ])
            potential_guy = preferred_rankings_women[ woman ].index(man)

            if (current_guy < potential_guy):
                print('She\'s satisfied with %s..' % (taken_match[ 0 ][ 0 ]))
            else:
                print('%s is better than %s' % (man , taken_match[ 0 ][ 0 ]))
                print('Making %s free again.. and tentatively engaging %s and %s' % (
                taken_match[ 0 ][ 0 ] , man , woman))

                # The new guy is engaged
                free_men.remove(man)

                # The old guy is now single
                free_men.append(taken_match[ 0 ][ 0 ])

                # Update the fiance of the woman (tentatively)
                taken_match[ 0 ][ 0 ] = man
                break


def stable_matching():
    '''Matching algorithm until stable match terminates'''
    while (len(free_men) > 0):
        for man in free_men:
            begin_matching(man)


def main():
    init_free_men()
    print(free_men)
    stable_matching()
    print(tentative_engagements)


main()
