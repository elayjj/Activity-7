#Built-in and Customization

animalsfood_cost = [200, 300, 400, 501, 600,]

def get_max_cost(animalsfood_cost):
    max_cost = 0
    for cost in animalsfood_cost:
        if cost > max_cost:
            max_cost = cost
            return max_cost
#Built in function
print(max(animalsfood_cost))
print(min(animalsfood_cost))

#custom function
print(max(animalsfood_cost))