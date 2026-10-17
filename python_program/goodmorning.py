import time as samay

timestamp = samay.strftime('%H:%M:%S')  
hours =6  #int(samay.strftime('%H'))
minutes = int(samay.strftime('%M'))
second = int(samay.strftime('%S'))

if hours <= 24 :
    #logic works But with help of AI
    if hours >= 7 and hours < 12:
        print("Good Morning.")
    elif hours >= 12 and hours < 18:
        print("Good Afternoon.")
    elif hours >= 18 and hours < 21:
        print("Good Evening.")
    else :
        print("Good Night. Go Home.")
else :
    print("You are in wrong time.")


#Old Logic, Failed
# print("Time is ",hours,":", minutes,":", second)

# if (7 <= hours >= 12):
#     print("Good Morning")
# elif(12 <= hours >= 17):
#     print('Good Afternoon')
# elif(17 <= hours >= 21):
#     print('Good Evening')
# elif(21 <= hours >= 24):
#     print('Good Night')
# else:
#     print("Not welcome. Go Home.")

# if(timestamp >= '7:00:00'):
#     print('Good morning')