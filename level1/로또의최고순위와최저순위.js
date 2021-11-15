function solution(lottos, win_nums) {
  let cntZero = 0; // --- 지워진 숫자 카운트 변수
  let cntAnswer = 0; // --- 맞춘 숫자 카운트 변수

  lottos.forEach((zero) => { // --- 내가 찍은 번호 중 0의 개수만큼 cntZero에 추가
    if (zero === 0) {
      cntZero++;
    }
  });

  if (cntZero === 6) {
    return [1, 6]; // 0의 개수가 6개라면 1등도 될 수 있고 6등도 될 수 있다.
  } else {
    for (let i = 0; i < lottos.length; i++) { // 내가 입력한 로또 숫자
      for (let j = 0; j < win_nums.length; j++) { // 회차 로또 정답 숫자
        if (lottos[i] === win_nums[j]) { // 두개가 일치한다면 cntAnswer에 추가
          cntAnswer++;
        }
      }
    }
    if (cntAnswer < 2) {
      cntAnswer = 1; // 2개 미만(0개, 1개)이 정답이면 6등이기에 1로 처리
    }
  } // else 끝
  var answer = [7 - ( cntZero + cntAnswer ), 7 - cntAnswer]
  return answer;
}