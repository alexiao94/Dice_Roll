from IPython.display import clear_output

import time,random


class dice:
    def roll(max_num):
        my_roll = random.randint(1,max_num) #Assign random dice roll landed value
        time.sleep(0.25) #Ensures that my_roll and my_randroll would not collide
        my_randroll = random.randint(3,15) #Assign random number of rolls
        
        for i in range(my_randroll):
            print(random.randint(1,max_num))
            time.sleep(0.5)
            clear_output()
        print("You landed:" + str(my_roll))
                
