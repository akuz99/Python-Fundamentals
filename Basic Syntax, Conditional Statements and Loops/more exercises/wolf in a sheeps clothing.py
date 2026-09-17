animals = input()

queue = animals.split(", ")

queue.reverse()


for index, item in enumerate(queue):
    if item == "wolf":
        if index == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")






