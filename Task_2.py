# Петя задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Пример: 4 4 -> 2 2 5 6 -> 2
def eq(x, y):
    return (x + y) 
lowerBound = int(1)
upperBound = int(1000)
sum = int(input("Sum: "))
multi = int(input("Multi: "))
for x in range(lowerBound, upperBound):
    for y in range(lowerBound, upperBound):
        if (eq(x, y) == sum):
            def eq(x, y):
                return (x * y) 
lowerBound = int(1)
upperBound = int(1000)
for x in range(lowerBound, upperBound):
    for y in range(lowerBound, upperBound):
        if (eq(x, y) == multi):
            if (((x * y) == multi) and ((x + y) == sum)):    
                print(x, y) 
                
