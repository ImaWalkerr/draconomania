import pandas
info = pandas.read_csv("E:/Games/info.csv")
marks = pandas.read_csv("E:Games/marks.csv")

#Описание info:
#id - номер студента
#gender - пол студента
#race - расса студента
#parents_education - образование родителей студента

#Описание marks:
#id2 - номер студента
#lunch - есть ли скидка в столовке у студента
#prep_course - ходил ли студент на подготовительные курсы
#math - оценка по математике
#reading - оценка по чтению
#writing - оценка граматнасьци студента

#1. Узнайте для скольких людей из датафрейма info неизвестны оценки.
#Подсказка: нужно использовать 1 merge некоторого типа и .shape
print(info.columns)
print(marks.columns)

new = info.merge(marks, left_on='id', right_on='id2')
print(info.shape[0] - new.shape[0])



