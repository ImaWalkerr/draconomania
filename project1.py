import pandas
#df = pandas.read_csv('E:/Games/titanic.csv')

#1. Распечатайте колонки которые есть датафрейме.
#print(df.columns)

#2. Узнайте сколько людей было на борту
#print(df['Name'])

#3. Узнайте сколько на борту было мужчин.
males_only = df[(df['Sex'] == 'male')]
#print(males_only.shape[0])

#4. Посчитайте процент выживших на борту.
all = df[(df['Survived'] == 1)]
#print(all.shape[0]/(df.shape[0])*100)

#5. Кого было больше на борту, мужчин или женщин ?
female_only = df[(df['Sex'] == 'female')].shape[0]
male_only = df[(df['Sex'] == 'male')].shape[0]
def res():
    a = males_only
    b = female_only
    if a > b:
        return "males"
    else:
        return "female"
#print(res())
#print(males_only, female_only)??

#6. Посчитайте сколько процентов из выживших были мужчинами?
#female_only = df[(df['Sex'] == 'female') & (df['Survived'] == 1)].shape[0]
#males_only = df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]
#print(female_only/(female_only+male_only)*100)

#используем 1 df на 1 значение. .shape[0] чтобы получить значение из таблицы

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
print(df.columns)
all1 = df[(df['id'] == 'math', 'reading', 'writing') & (df['id'].merge)]