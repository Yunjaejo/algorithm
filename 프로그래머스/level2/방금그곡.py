def time_to_minute(x):  # HH:MM 을 분으로 변환해주는 함수
    return int(x.split(':')[0]) * 60 + int(x.split(':')[1])


def get_play_time(x):  # 음악이 총 재생된 분 수를 구하는 함수
    return time_to_minute(x.split(',')[1]) - time_to_minute(x.split(',')[0])


def sharp_to_lower(x):  # '#'이 len(str) 에서 1칸을 차지하지 않게하기위해 올림음을 소문자로 치환해주는 함수
    return x.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answer = []
    for music in musicinfos:
        m = sharp_to_lower(m)
        that_sound = sharp_to_lower(music.split(',')[3])
        play_time = get_play_time(music)
        if play_time == len(that_sound):  # 재생시간이 같으면 음계 그대로
            that_sound = that_sound
        elif play_time > len(that_sound):  # 재생시간이 더 길다면 음계 반복 재생 + 남은시간 음계 붙이기
            that_sound = that_sound * (play_time // len(that_sound)) + that_sound[:play_time % len(that_sound)]
        elif play_time < len(that_sound):  # 재생시간이 더 짧다면 재생시간까지만 음계 재생
            that_sound = that_sound[:play_time % len(that_sound)]

        if m in that_sound:  # 내가 들은 음이 that_sound 에 있다면
            answer.append([play_time, music.split(',')[2]])  # 재생시간과 제목을 정답배열에 추가

    if answer:  # 정답이 있다면
        return sorted(answer, key=lambda x: (-x[0]))[0][1]  # 정답을 0번인덱스(재생시간) 내림차순으로 정렬 후 제목만 뽑기.
    else:
        return '(None)'

    # 조건 5: "조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다."
    # 재생시간 긴 순으로 30 줄에서 정렬함. 먼저 입력된 음악 제목은 순서대로 append 되니까 그냥 리턴하면 됨.
    # 만약 순서대로 입력된게 아니라면 enumerate 를 사용해서 반복문의 인덱스를 살펴보자
