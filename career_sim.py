import random
import time

match_time = random.randint(1,95)



print('Footballer: Academy to Legend | Pre-Alpha 0.5')




pname = input('enter player name ')
player = {'name' : pname , 
          "age" : 18 , 
          'shooting' : 50 ,
          'passing' : 50 ,
          'pace' : 50 ,
          'handling' : 50 ,
          'club' : 'academy',
          'goals' : 0,
          'assist' : 0}
                        
print('player details : ' , player) 
month = 1
season = 1

while True:
    print(f"\n--- SEASON {season} ---")
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
            goal_chance = random.randint(1,100)
            assist_chance = random.randint(1,100)
            if goal_chance <= player['shooting']:
                player['goals'] += 1
                print("You scored a GOAL!")

            if assist_chance <= player['passing']:
                player['assist'] += 1
                print("You made an ASSIST!")

    print("\n--- SEASON OVER ---")
    print("Goals scored:", player['goals'])
    print("Assists:", player['assist'])
    print("Final stats:", player)
    player['age'] += 1
    print("You are now age:", player['age'])
    player['goals'] = 0
    player['assist'] = 0
    month = 1
    season += 1
    cont = input("Play another season? (y/n): ")

    if cont.lower() != 'y':
        break
 
    