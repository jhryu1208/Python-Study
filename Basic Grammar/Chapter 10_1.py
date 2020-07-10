# Chapter 10-1
# Hangman (행맨) 미니 게임 제작(1)
# 기본 프로그램 제작 및 테스트

import time

# 처음 인사
name = input("what is your name?")

print("Hi, " + name, " Time to play hangaman game!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# 정답 단어
word = "secret"

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 while loop
# 찬스 카운트가 남아 있을 경우
while turns  > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0                                                  ## fail을 0으로 지속적으로 초기화 시켜준다.

    # 정답 단어 반복
    for char in word:                                           ## word의 secret의 단어가 6글자기 때문에 6번 반복된다.
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:                                     ## (첫 순서) guesses는 공백이기 때문에 실행되지 않는다.
            # 추측 단어 출력
            print(char, end = ' ')
        else:
            # 틀린 경우 대시로 처리
            print("_", end = ' ')                               ## (첫 순서) if문 실행되지 않았기 때문에 else문이 6번 반복 실행된다.
            failed += 1                                         ## (첫 순서) 6번 반복 실행되었기 때문에, failed에는 6이 적립되어있다.


    # 단어 추측이 성공한 경우
    if failed == 0:                                             ## (첫 순서) failed는 6이 적립되어있기 때문에, 이 if문은 실행되지 않는다.
        print()                                                 ## (맞출때) guesses에서는 텍스트가 지속적으로 누적된다.
        print()                                                 ##          따라서, 누적된 텍스트가 success를 전부 포함할 경우 failed는 0이다.
        print('Congratulation! The Guesses is correct.')
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    guess = input("guess a character.")

    # 단어 더하기
    guesses += guess                                            ## 계속 텍스트가 누적된다!

    # 정답 단어에 추측한 문자가 포함되어에 있지 않으면
    if guess not in word:
        # 기회 횟수 감소
        turns-=1
        # 오류메시지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turns, "more guesses!")

        if turns == 0 :
            # 실패 메시지
            print("You hangaman game failed. Bye!!")
