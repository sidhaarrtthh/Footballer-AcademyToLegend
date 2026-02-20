import random
import time
academy_club  = ['Northwells Academy' , 'Manchester Young Boys' , 'Northern Athletic Academy' , 'Southwells Academy' , 'Westside Youngs' , 'Flames Academy' ]
local_club = ['Seaside FC' , 'Modern Athletics FC' , 'Newtown FC', 'Greenhills FC']
pro_club = ['Northwells FC' , 'Southwells FC', 'Northern Athletic FC' , 'Bluco FC' , ]
prem_club = ['Superstars FC' , 'Premier XI' , 'Westside FC' , 'Toppers FC']
agency = ['Nextstep Talent Management' , 'Allround Talent Management' , 'Superstarts Contracts' , 'Lightning Talent Management']

match_time = random.randint(1,95)



def play_match(player):
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

    rating = 6 + (match_goals * 1.5) + (match_assists * 1)

    if rating > 10:
        rating = 10

    print("Match Rating:", round(rating,1))





print('Footballer: Academy to Legend | Alpha 1.1')

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
          'assist' : 0,
          'Agency' : 'No Agent'}
                        
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

            

        elif ch ==2:
            player['passing'] += 5
            print('Passing Increased by 5 points!')
            
        
        elif ch == 3:
            player['handling'] += 5
            print('Handling stats increased by 5')
            
        elif ch == 4:
            player['pace'] += 5
            print('player pace increased by 5')
            
        else:
            print('Month Passed without any productive activity')
            
        if month== 3 or month== 6 or month==9 or month==12:
            play_match(player)
        month+=1




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
            print('Local Scouts have ten notice of you...')
            time.sleep(2)
            new_club = random.choice(local_club)
            print("\nTRANSFER OFFER!")
            print(new_club, "wants to sign you.")

            choice = input("Do you accept? (y/n): ")

            if choice.lower() == 'y':
                player['club'] = new_club
                print("You signed for", new_club)
                agent = random.choice(agency)
                print('you have also signed for a player agency! ' , agent)
                player['Agency'] = agent
            else:
                print("You decided to stay at", player['club'])

    elif current_club in local_club:
        if goals >= 2:
            print('Message from agent : Many clubs are asking about you...An offer is expected soon.')
            time.sleep(2)
            new_club = random.choice(pro_club)
            print("\nTRANSFER OFFER!")
            print(new_club, "wants to sign you.")

            choice = input("Do you accept? (y/n): ")

            if choice.lower() == 'y':
                player['club'] = new_club
                print("You signed for", new_club)
            else:
                print("You decided to stay at", player['club'])

    elif current_club in pro_club:
        if goals >= 4:
            print("Message from agent : A Prem League club is interested! Don't let this oppurtinity slide.")
            new_club = random.choice(prem_club)
            print("\nTRANSFER OFFER!")
            print(new_club, "wants to sign you.")

            choice = input("Do you accept? (y/n): ")

            if choice.lower() == 'y':
                player['club'] = new_club
                print("You signed for", new_club)
            else:
                print("You decided to stay at", player['club'])

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
                
    
