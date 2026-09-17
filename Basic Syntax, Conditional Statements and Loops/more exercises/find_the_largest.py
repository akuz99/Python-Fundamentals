number = input()

digits = sorted(number, reverse = True) #sorted - сортира от малко към голямо, а reverse ги обръща. То работи с булева, затова трябва = True

new_number = ""

for digit in digits:
    new_number += digit

print(new_number)

#drugo reshenie (no purvoto e po-dobro):
# while number != "":
#     biggest_digit = ""
#
#     for current_digit in number:
#         if current_digit > biggest_digit:
#             biggest_digit = current_digit
#
#     new_number += biggest_digit
#     number = number.replace(biggest_digit, "", 1) - v skobite: zameni nai-golqmata cifra s prazen string i go napravi samo edin put(za da izbegne mahaneto povtorno ako ima dve ednakvi chisla)



