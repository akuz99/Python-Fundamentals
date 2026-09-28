start = int(input())
end = int(input())

result = ""

for index in range(start,end + 1):
    result += chr(index) + " "

print(result)
