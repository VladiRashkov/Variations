def variations(number, collection, number_of_combinations):
    if number == 0:
        return [""]
    
    result = []
    for char in sorted(collection):
        for combination in variations(number - 1, collection, number_of_combinations // len(collection)):
            result.append(char + combination)

    return result


a = int(input())
b = input().split(" ")
c = len(b) ** a

all_variations = variations(a, b, c)


for variation in all_variations:
    print(variation)
