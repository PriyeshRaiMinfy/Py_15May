# Convert two lists into a dictionary
names = ["Alice", "Bob", "Charlie", "Diana","Priyesh"]
scores = [92, 87, 78, 95, 100, 101]
name_to_score = {name: score for name, score in zip(scores, names)}
print("Name to score dictionary:", name_to_score)
