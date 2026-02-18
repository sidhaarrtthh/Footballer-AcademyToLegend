import random
import time
academy_club  = ['Northwells Academy' , 'Manchester Young Boys' , 'Northern Athletic Academy' , 'Southwells Academy']
local_club = ['Seaside FC' , 'Modern Athletics FC' , 'Newtown FC']
pro_club = ['Northwells FC' , 'Southwells FC', 'Northern Athletic FC' , 'Bluco FC']
prem_club = ['Superstars FC' , 'Premier XI' , 'Westside FC' , 'Toppers FC']

match_time = random.randint(1,95)



print('Footballer: Academy to Legend | Alpha 1.0')

print('Welcome to Footballer: Academy to Legend')
time.sleep(2)
print('Start as a player in the academy and work you way up to the most elite teams!')
time.sleep(2)
print('Make choices and watch your player grow and move clubs')
time.sleep(2)
input('Are you ready?\n')




pname = input('Enter player name:  ')
player = {'name' : pname , 
          "age" : 18 , 
          'shooting' : 50 ,
          'passing' : 50 ,
          'pace' : 50 ,
          'handling' : 50 ,
          'club' : random.choice(academy_club),
          'goals' : 0,
          'assist' : 0}
                        
print('player details : ' , player) 
month = 1
season = 1

while True:
    print(f"\n--- SEASON {season} ---")
    print('Current Club : ' , player['club'])
    input('Enter any key to start the season.')
    while month <= 12:
        print('Month ' , month)
        
        print('what do you want to do : ')
        print('1.Train Shooting ')
        print('2.Train Passing')
        print('3.Train Handling ')
        print('4.Train Pace')
        print('5.Do nothing')
        
        ch = int(input('What should we do? ' ))
        if ch == 1:
            player['shooting'] += 5
            print('Shooting Increased by 5 points!')

            month += 1

        elif ch ==2:
            player['passing'] += 5
            print('Passing Increased by 5 points!')
            month += 1
        
        elif ch == 3:
            player['handling'] += 5
            print('Handling stats increased by 5')
            month += 1
        elif ch == 4:
            player['pace'] += 5
            print('player pace increased by 5')
            month += 1
        else:
            print('Month Passed without any productive activity')
            month += 1
        if month== 3 or month== 6 or month==9 or month==12:
            print('\nMatch Day!')
            time.sleep(1)
            print('Playing match....')
            time.sleep(3)
            match_goals = 0
            match_assists = 0
            goal_chance = random.randint(1,100)
            assist_chance = random.randint(1,100)
            if goal_chance <= player['shooting']:
                player['goals'] += 1
                match_goals += 1
                print("You scored a GOAL!")

            if assist_chance <= player['passing']:
                player['assist'] += 1
                match_assists += 1
                print("You made an ASSIST!")
            # MATCH RATING SYSTEM
            rating = 6 + (match_goals * 1.5) + (match_assists * 1)

            if rating > 10:
                rating = 10

            print("Match Rating:", round(rating, 1), "/ 10")
            if rating >= 9:
                print('Man of the match!')

            elif rating >=7:
                print('Good game!')
            elif rating ==6:
                print('You barely had an impact.')
            time.sleep(2)



    print("\n--- SEASON OVER ---")
    print("Goals scored:", player['goals'])
    print("Assists:", player['assist'])
    print("Final stats:", player)

    player['age'] += 1
    print("You are now age:", player['age'])

    # PROMOTION SYSTEM
    goals = player['goals']
    current_club = player['club']

    if current_club in academy_club:
        if goals >= 1:
            player['club'] = random.choice(local_club)
            print("Scouts were impressed! You have been signed by", player['club'])
        else:
            print("No scouts were interested in you. You decided to train at", player['club'], "for another season.")

    elif current_club in local_club:
        if goals >= 2:
            player['club'] = random.choice(pro_club)
            print(player['club'] , 'signs' , pname , 'after an impressive season.' , " You joined", player['club'])
        else:
            print("Contract extended at", player['club'], "for another season.")

    elif current_club in pro_club:
        if goals >= 5:
            player['club'] = random.choice(prem_club)
            print("SHOCKING MOVE! " , player['club'], ' signs ' , pname , 'for a HISTORIC transfer fee' ,  "You signed for", player['club'])
        else:
            print("Contracted Extended at", player['club'], "for another season.")

    # NOW reset season stats
    player['goals'] = 0
    player['assist'] = 0
    month = 1
    season +=1
    cont = input("\nDo you want to play another season? (y/n): ")

    if cont.lower() != 'y':
        print("\n--- RETIREMENT ---")
        print(player['name'], "has announced retirement from football.")
        print("Final club:", player['club'])
        print("Final age:", player['age'])
        break
    if player['age'] >= 35:
        chance = random.randint(1, 100)

        if chance <= 40:
            print("\n--- FORCED RETIREMENT ---")
            print("You failed your medical evaluation due to concerns regarding your age.")
            print("The International Football Federation has processed your retirement.")
            print("Final club:", player['club'])
            print("Final age:", player['age'])
            break


print('Thank You for playing Footabller : Academy to Legend.')
