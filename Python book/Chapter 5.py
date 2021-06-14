first = raw_input("gimme yer first name")
last = raw_input("now gimme yer last name. Or else.....")
print first, last
print ""
print ""
print "Now,",first, last, "shall meet his doom!"
print ""
print ""
length = int(raw_input("Dat's right. Gimme yer rooms length in feet, because yoo are in desperate need for a new carpet."))
width = int(raw_input("Ye has guessed it. Da width now. NOW!"))
total = length * width
print "ye rooms sq.ft. is", total,"."
print ""
print ""
cost = int(raw_input("Mmmmhmmm. Cost per square foot. N....O.....W...!!!!!!!!!"))
costy = cost * total
print "So kid, your room is",total,"sqft or", total / 3, "sqyd. Soooooo, dat wwill cost a total of $", cost * total
print ""
print ""
print "Let's see. You need to pay", cost * total, "dollars, am I right? Let's see how much you have. Enter da number of dollars yoo have."
d = int(raw_input())
q = int(raw_input("okay, quarters."))
di = int(raw_input("dimes."))
n = int(raw_input("nickels."))
p = int(raw_input("at last, pennies."))
ttotal = q * 25 + di * 10 + n * 5 + p
tttotal = ttotal / 100
ttttotal = d * 100 + tttotal
print "k. Yoo have a total of YIKES!!!! Only", ttttotal,"bucks? YIKKKESSS!!!! Go earn some money, hobo."