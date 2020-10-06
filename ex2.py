seconds = int(input("input seconds: "))
size_of_time = 60
hours = seconds // size_of_time ** 2
minutes = (seconds - hours * size_of_time ** 2) // size_of_time
seconds = seconds - (minutes + hours * size_of_time) * size_of_time
print("чч:", "%02d" % hours, "мм:", "%02d" % minutes, "сс:", "%02d" % seconds)
