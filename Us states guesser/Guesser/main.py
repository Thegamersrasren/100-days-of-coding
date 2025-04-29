import turtle
import pandas
screen = turtle.Screen()
screen.title("The US States Guessing Game")
bg = "blank_states_img.gif"
screen.addshape(bg)
turtle.shape(bg)

data = pandas.read_csv("50_states.csv")



correct = []
lives = 5
states = data.state.to_list()
while len(correct) < 50 :
   guess_state = screen.textinput(title=f"{len(correct)}/50 States Correct Lives left {lives}", 
                          prompt="Type any state in the US").title() 
   if guess_state == "Exit":
      
            
      

      break
   if guess_state in states:
      correct.append(guess_state)
      tim = turtle.Turtle()
      tim.hideturtle()
      tim.penup()

      state_data = data[ data.state == guess_state]
      tim.goto(state_data.x.item(), state_data.y.item())
      tim.write(guess_state)
     
   else:
      lives -= 1
      
   if lives == 0:
      missing_states = []
      for places in states:
         if places not in correct:
            missing_states.append(places)
            new_stuff = pandas.DataFrame(missing_states)
            new_stuff.to_csv("States that you didnt get")
      break
turtle.mainloop