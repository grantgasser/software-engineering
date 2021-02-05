# 
# Your previous Java content is preserved below:
# 
# import java.io.*;
# import java.util.*;
# 
# 
# /* Prompt: Given a circular train of at least one car
#  * where each car has a light that may be either on or off,
#  * move forwards and/or backwards through the train to determine
#  * the length.  You start in a random car and the lights
#  * are initially on or off at random.  You may change the lights
#  * to assist in counting the cars.  You may only see the light of the car
#  * that you are "in".
#  */
# public class Train { 
#   
#     class Car { 
#         boolean on; 
#         Car prev; 
#         Car next; 
# 
#         Car(boolean o) { on = o; } 
#     } 
# 
# 
#     //Please complete this function.  
#     public int numberCars(Car start) { 
# 
#     } 
# }

# mistake: I guess O(N) but its O(N^2) - wish I had more time to analyze and
# get it right

# also, he mentioned something about reverse binary search to reduce runtime - I'm assuming to O(N log N)
def num_cars(start):
    counter = 0
    done = False
    
    # set initial light
    initial_light = start.on
    curr = start
    
    while not done:
        curr = curr.next
        counter += 1
        
        if curr.on == initial_light:
            # change curr light so we can check if initial light changes
            curr.on = not curr.on
            
            
            # check for stopping condition
            for i in range(counter):
                curr = curr.prev
                
            # if diff, then same car, end of cycle
            if curr.on != initial_light:
                done = True
            else:
                for i in range(counter):
                    curr = curr.next
                
    return counter


# - 1 (ON) - 2 (OFF) - 3 (OFF) - 4 -

# if next == initial_light:
    # go back counter steps
    # change next to opposite of curr
    # if next == curr:
        # same car, stop (done = True)
