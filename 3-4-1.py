with open('dataset_3363_3.txt', 'r') as file:
    text = file.read().lower().split(" ")
    winner = 0

for i in range(len(text)):
    a = text.count(text[i])
    if winner < a:
        winner = a
        winner_index = i
        winner_word = text[a]

print(winner_word, winner_index)
