name = input()
howMany = int(input())
teamNames = [input() for _ in range(howMany)]
teamNames.sort()
wins = []
for teamName in teamNames:
    L = name.count('L') + teamName.count('L')
    O = name.count('O') + teamName.count('O')
    V = name.count('V') + teamName.count('V')
    E = name.count('E') + teamName.count('E')

    win = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    wins.append(win)

print(teamNames[wins.index(max(wins))])
