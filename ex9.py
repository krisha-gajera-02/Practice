import random

participants = ["Krisha", "Aditi", "Rahul", "Neha", "Aman"]

winner = random.choice(participants)
print("Winner:", winner)

num_unique_winners = 3
unique_winners = random.sample(participants, num_unique_winners)
print("Top 3 Unique Winners:", unique_winners)

num_top3 = 3
top3_with_repetition = random.choices(participants, k=num_top3)
print("Top 3 (with repetition):", top3_with_repetition)

random.shuffle(participants)
print("Shuffled Participants:", participants)

lucky_number = random.randint(1, 100)
print("Lucky Number:", lucky_number)

discount = random.uniform(5, 20)
print("Discount Percentage:", round(discount, 2))

rand_float = random.random()
print("Random Float (0-1):", rand_float)
