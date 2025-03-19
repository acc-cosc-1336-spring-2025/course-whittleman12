import decisions

options = int(input("Enter a score: "))
total = int(input("Enter the maximum score: "))

result = decisions.get_options_ratio(options, total)

print(decisions.get_faculty_rating(result))
