# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age



def is_good(total, ldl, trig):
    return total < 200 and ldl < 100 and trig < 150

def is_high(total, ldl, trig):
    return total > 240 or ldl > 160 or trig >= 200

def is_borderline(total, ldl, trig):
    return (200 < total < 240
            or 130 < ldl < 160
            or 150 <= trig < 200)

def announce_good():
    print('*** Good level of cholestrol ***')
    
def announce_high():
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')

def announce_borderline():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \n"
          "should come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. '
          'For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')


# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

if is_good(total_cholesterol, ldl, triglyceride):
    announce_good()
elif is_high(total_cholesterol, ldl, triglyceride):
    announce_high()
elif is_borderline(total_cholesterol, ldl, triglyceride):
    announce_borderline()
else:
    print('Error: unhandled case.')
