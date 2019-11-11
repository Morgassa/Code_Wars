num_to_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20:'twenty'}

def wallpaper(l, w, h):
    if l and w and h !=0:
        hc = h * (15/100)
        h +=hc
        wall_extension = 2 * (l+w)
        papers_colums = wall_extension / 0.52
        lenght_of_paper = (papers_colums * h) /10
        lenght_of_paper = int((lenght_of_paper//1)+1)
           
        return (num_to_words[lenght_of_paper])
    else:   
        return ('zero')
    
    
wallpaper(0.0, 3.5, 3.0) # , "zero")
wallpaper(6.3, 4.5, 3.29) # , "sixteen")
wallpaper(7.8, 2.9, 3.29) # , "sixteen")
wallpaper(6.3, 5.8, 3.13) # , "seventeen")
wallpaper(6.1, 6.7, 2.81) #, "sixteen")




# John wants to decorate a room with wallpaper. He's heard that making sure he has the right 
# amount of wallpaper is more complex than it sounds. He wants a fool-proof method for getting it right.

# John knows that the rectangular room has a length of l meters, a width of w meters, a height
#  of h meters. The standard width of the rolls he wants to buy is 52 centimeters. The length 
# of a roll is 10 meters. He bears in mind however, that it’s best to have an extra length of 
# wallpaper handy in case of mistakes or miscalculations so he wants to buy a length 15% greater 
# than the one he needs.

# Last time he did these calculations he got a headache, so could you help John? Your function 
# wallpaper(l, w, h) should return as a plain English word in lower case the number of rolls he must buy.



# Example:

# wallpaper(4.0, 3.5, 3.0) should return "ten"

# wallpaper(0.0, 3.5, 3.0) should return "zero"
# Notes:

#     all rolls (even with incomplete width) are put edge to edge
#     0 <= l, w, h (floating numbers), it can happens that w x h x l is zero
#     the integer r (number of rolls) will always be less or equal to 20

#     FORTH: the number of rolls will be a positive or null integer (not a plain English word; this number can be greater than 20)

