import config

def say_hello(name):
   print(f"Hello, {name} form {config.APP_NAME}!")
   print(f"Goodbye, {name} from {config.APP_NAME}!")
   print(f"Today is {now.strftime('%Y-%m-%d')}.")
      
def greet_user():
   name = input("Please enter your name: ")
   say_hello(name)
   
if __name__ == "__main__":
   greet_user()