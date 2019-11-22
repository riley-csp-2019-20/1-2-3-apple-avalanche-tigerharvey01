#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
wn = trtl.Screen()
apple_letter_x_offset= -25
apple_letter_y_offset

#new code
screen_width = 400 
screen_height= 400
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

def reset_apple(active_apple):
    length_of_list= len(letter_list)
    if (length_of_list != 0):
      index= rand.randiant(0, length_of_list)
      active_apple.goto(rand.randint(-(screen_width)/2, (screen_width/2), rand.randint(-(screen_height)/2, (screen_height/2))
      draw_apple(active_apple, letter_list.pop(index))
  

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter("A", active_apple)
  wn.update()

  draw_apple(apple)

#moves apple to ground and hides it
def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)
def draw_letter(letter, active_apple):
  active_apple.color('white')
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset, active_apple.ycor()+ apple_letter_y_offset)
  active_apple.write(letter, font=('arial',74, 'bold'))
  active_apple.setpos(remember_position)

draw_apple(apple)
wn.onkeypress(drop, 'a')

def check_letter_():
  if(current_letter=='A'):
    drop_apple("A")
def check_letter_():
  if(current_letter=='B'):
    drop_apple("B")
def check_letter_():
  if(current_letter=='C'):
    drop_apple("C")
def check_letter_():
  if(current_letter=='D'):
    drop_apple("D")
def check_letter_():
  if(current_letter=='E'):
    drop_apple("E")
def check_letter_():
  if(current_letter=='F'):
    drop_apple("F")
def check_letter_():
  if(current_letter=='G'):
    drop_apple("G")
def check_letter_():
  if(current_letter=='H'):
    drop_apple("H")
def check_letter_():
  if(current_letter=='J'):
    drop_apple("J")
def check_letter_():
  if(current_letter=='K'):
    drop_apple("K")
def check_letter_():
  if(current_letter=='L'):
    drop_apple("L")
def check_letter_():
  if(current_letter=='M'):
    drop_apple("M")
def check_letter_():
  if(current_letter=='N'):
    drop_apple("N")
def check_letter_():
  if(current_letter=='O'):
    drop_apple("O")
def check_letter_():
  if(current_letter=='P'):
    drop_apple("P")
def check_letter_():
  if(current_letter=='Q'):
    drop_apple("Q")
def check_letter_():
  if(current_letter=='R'):
    drop_apple("R")
def check_letter_():
  if(current_letter=='S'):
    drop_apple("S")
def check_letter_():
  if(current_letter=='T'):
    drop_apple("T")
def check_letter_():
  if(current_letter=='U'):
    drop_apple("U")
def check_letter_():
  if(current_letter=='V'):
    drop_apple("V")
def check_letter_():
  if(current_letter=='W'):
    drop_apple("W")
def check_letter_():
  if(current_letter=='X'):
    drop_apple("X")
def check_letter_():
  if(current_letter=='Y'):
    drop_apple("Y")
def check_letter_():
  if(current_letter=='Z'):
    drop_apple("Z")
def check_letter_():
  if(current_letter=='I'):
    drop_apple("I")

wn.listen()
trtl.mainloop()