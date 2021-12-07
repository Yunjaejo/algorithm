A, B, V = map(int, input().split())

day = (V - B) / (A - B)

if day % 1 > 0:  # 만약 day 가 정확히 나누어 떨어지지 않는다면 (4.2일이 걸린다면) 5일만에 올라간 것이므로 +1
    print(int(day) + 1)
else:
    print(int(day))

# V = (A-B) * day + B 임. (마지막날의 -B까지 계산했기에 하루치의 B를 더해줌)
# ->  day(V-B)/(A-B)



