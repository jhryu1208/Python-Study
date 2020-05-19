# Chapter 09_1
# 파일 읽기 및 쓰기

# *읽기 모드 : r, *쓰기모드 : w, *추가모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로(' ../ , ./'), 절대 경로 ('C:\Django\exapmle..')

#  [파일 읽기 (Read)]
#  [예제1]
## (절대경로)
## f = open('F:\\Programming\\Python\\Python-Basic\\Basic Grammar\\resource\\it_news.txt', 'r', encoding='UTF-8')
## (상대경로)
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
