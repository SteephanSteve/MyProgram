
t=int(input())
c='$'
for i in range(t):
    print ((c*i).rjust(t)+c+(c*i).ljust(t)).center(t*6)
for i in range((t+1)/2):
    print (c*t).center(t*6)
for i in range((t+1)/2):
    print (c*(i+1)).rjust(t-2)+(c*(t*5-4)).center(t-2)+(c*(i+1)).ljust(t)
for i in range(t):
    print (c*t).ljust(t)
for i in range((t+1)/2):
    print (c*(t/2-i)).rjust(t-3)+(c*(t*5-3)).ljust(t*5-3)+(c*(i+1)).ljust(t+5)
for i in range(t):
    print (c*t).rjust(t*6-3)                                                                        
for i in range((t+1)/2):
    print (c*(t/2-i)).rjust(t-3)+(c*(t*5-4)).center(t-2)+(c*(t/2-i+1)).ljust(t)
for i in range((t+1)/2):
    print (c*t).center(t*6)
for i in range(t):
    print ((c*(t-i-1)).rjust(t)+c+(c*(t-i-1)).ljust(t)).center(t*6)
