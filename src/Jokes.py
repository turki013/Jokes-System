from requests import get


response = get("https://official-joke-api.appspot.com/random_joke")
try:
 response.raise_for_status()
 joke = response.json()
except Exception as e:
    print(f"Error: {e}")
print("Welcome to the Jokes App")
Jokes = input("Enter a tap to get joke: ") 
print(f"Joke: {joke['setup']}")
print(f"Answer: {joke['punchline']}")
 



        
   
        
        