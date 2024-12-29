import random

colegas = ["Bob", "Carol", "Eve", "Alice"]

# 1ª opção de seleção aleatória
print(random.choice(colegas))

# 2ª opção de seleção aleatória
random_index = random.randint(0, 3)
print(colegas[random_index])
