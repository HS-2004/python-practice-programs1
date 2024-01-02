lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

print("Output of cube of no.from ll to ul :")
for i in range(lower_limit, upper_limit + 1):
    print(f"{i}: {i ** 3}")
