repeat_string = lambda current_string, repeat: current_string * repeat

string = input()
counter = int(input())

result = repeat_string(string, counter)
print(result)