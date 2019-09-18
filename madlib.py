import random
y = 1
z = []
while(y > 0):
     time = ["A second", "A minute", "An hour", "A day", "A week", "A month", "A year", "A decade", "A century", "A millennium"]
     adjective = ["a demented", "a possessed", "a paranoid", "a pessimistic", "a naive", "an obnoxious"]
     animals = ["cat", "dog", "spider", "pig", "human", "snake", "bear", "cow", "bird"]
     verb = ["jump", "sleep", "eat", "run", "walk", "swim", "fly"]
     verb2 = ["blackmail", "humiliate", "surpress", "incarcerate", "cryogenically freeze"]
     print(random.choice(time) + " ago, there was " + random.choice(adjective) + " " + random.choice(animals) + " who decided to " + random.choice(verb) + " and " + random.choice(verb2) + " people.")
     y = y + 1
