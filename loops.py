'''for(int i=0; i < 10; i++){
    print(i)
}'''


for value in range(10):
    print(value)
print("Loop finished")

print(value)

while value < 1:
    print("Value is", value)
    #print("Incremented value is", value + 1)
    #value = value + 1
    value += 1

for i in range(5):
    print("i is", i)
    for j in range(5):
        print("j is", j)
        break
    print("j loop finished")
print("i loop finished")
    

