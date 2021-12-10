def solution(board, moves):
    board_size = len(board)
    baguni = []
    cnt = 0

    for move in moves:
        for i in range(board_size):
            if board[i][move - 1] == 0:  # 뽑을 곳이 0이라면 그냥 패스
                pass
            else:  # 뽑을 곳에 값이 있다면
                baguni.append(board[i][move - 1])  # 바구니에 더해주기
                board[i][move - 1] = 0  # 더했으니까 보드에 자리 비우기
                if len(baguni) >= 2:  # 만약 바구니에 2개이상 담겼다면 아래 로직 실행
                    if baguni[-1] == baguni[-2]:  # 맨 뒤와 그 앞이 같다면 둘 다 빼내기
                        baguni.pop()
                        baguni.pop()
                        cnt += 2  # 정답에 2 추가하기 (회수가 아니라 개수였다..)
                break  # 하나를 바구니에 더했으면 더 뒤지지 말고 다음 반복문으로 넘어가기

    return cnt
