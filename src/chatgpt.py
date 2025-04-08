""" # move sequence
S = input().strip()

#Number of combos
M = int(input())

#  Read combos, APPENED TO LIST W/ KEY VALUE
combos = []
for i in range(M):
    combo_str, point_str = input().split()
    combos.append((combo_str, int(point_str)))

# Base score: 1 point per move
base_score = len(S)

#Try each combo: if it appears at least once, add the bonus
max_score = base_score

for pattern, bonus in combos:
    if pattern in S:
        max_score = max(max_score, base_score + bonus)

# 🏁 Print final score
print("Final Score:", max_score) """

# 📥 Get Wesley's move sequence (a string like "UDLRUDLLLR")
""" S = input().strip()
M = int(input())

# 📋 Create a list to store all combos and their bonus points
combos = []
for i in range(M): #range of m = all combos
    combo_str, point_str = input().split()  #combo, point for input
    combos.append((combo_str, int(point_str))) #append them to a list so we can accesss key value pairs

# ➕ Base score = 1 point per move in the sequence (each character = 1 point)
base_score = len(S)

# 🔝 Start by assuming no bonus combo is used: best score = base score, if 1 eltter best_score = 1 currently
best_score = base_score

# 🔍 Go through each combo to see if it appears in the move sequence
for pattern, bonus in combos:
    # ✅ If the current combo pattern appears anywhere in the sequence
    if pattern in S:
        # 🧾 Calculate total score if we used this combo's bonus
        combo_score = base_score + bonus
        
        # 💡 If that total score is higher than what we have so far, update best_score
        if combo_score > best_score:
            best_score = combo_score

# 🏁 After trying all combos, print the highest possible final score
print("Final Score:", best_score) """

"""  """




S = input().strip()
M = int(input())

# 📋 Store all combos and their bonus points
combos = []
for i in range(M):
    combo_str, point_str = input().split()
    combos.append((combo_str, int(point_str)))

base_score = len(S)
max_bonus = 0

for key, value in combos:
    if key in S:
        max_bonus = value
        if value > max_bonus:
            max_bonus = value
print(base_score + max_bonus)