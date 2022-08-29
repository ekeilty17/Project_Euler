

print("True, break")
for i in range(10):
    if True:
        break
else:
    print("Hi")

print()
print("False, break")
for i in range(10):
    if False:
        break
else:
    print("Hi")


print()
print("True, continue")
for i in range(10):
    if True:
        continue
else:
    print("Hi")

print()
print("False, continue")
for i in range(10):
    if False:
        continue
else:
    print("Hi")
