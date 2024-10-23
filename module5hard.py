#
# Задание "Свой YouTube":
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать
# методы добавления видео, авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
#     Атрибуты: nickname(имя пользователя, строка),
#               password(в хэшированном виде, число),
#               age(возраст, число)
#
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
#     Атрибуты: title(заголовок, строка),
#               duration(продолжительность, секунды),
#               time_now(секунда остановки (изначально 0)),
#               adult_mode(ограничение по возрасту, bool (False по умолчанию))
#
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#      Атрибуты: users(список объектов User),
#                videos(список объектов Video),
#                current_user(текущий пользователь, User)

#     Метод log_in, который принимает на вход аргументы:
#           nickname, password и пытается найти пользователя в users с такими же
#           логином и паролем. Если такой пользователь существует, то current_user
#           меняется на найденного.
#           Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#
#     Метод register, который принимает три аргумента:
#           nickname, password, age, и добавляет пользователя в список, если пользователя
#           не существует (с таким же nickname).
#           Если существует, выводит на экран: "Пользователь {nickname} уже существует".
#           После регистрации, вход выполняется автоматически.
#
#     Метод log_out для сброса текущего пользователя на None.
#
#     Метод add, который принимает неограниченное кол-во объектов класса Video и
#           все добавляет в videos, если с таким же названием видео ещё не существует.
#           В противном случае ничего не происходит.
#
#     Метод get_videos, который принимает поисковое слово и возвращает список названий
#           всех видео, содержащих поисковое слово.
#           Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
#           (не учитывать регистр).

#     Метод watch_video, который принимает название фильма, если не находит точного
#           совпадения(вплоть до пробела), то ничего не воспроизводится,
#           если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
#           После текущее время просмотра данного видео сбрасывается.
#     Для метода watch_video так же учитывайте следующие особенности:
#           Для паузы между выводами секунд воспроизведения можно использовать функцию
#           sleep из модуля time.
#           Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
#           В противном случае выводить в консоль надпись:
#           "Войдите в аккаунт, чтобы смотреть видео"
#           Если видео найдено, следует учесть, что пользователю может быть отказано в
#           просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение:
#           "Вам нет 18 лет, пожалуйста покиньте страницу"
#           После воспроизведения нужно выводить: "Конец видео"
#
#####
import time
#
class User :
    def __init__(self, nickname, password, age) :
        self.nickname = nickname # (имя пользователя, строка)
        self.password = hash(password) # (в хэшированном виде, число)
        self.age = age # (возраст, число)
#
    def __hash__(self) : # получение ХЭШ-а пароля
        return hash(self.password)
##
class Video :
    def __init__(self, title, duration, time_now = 0, adult_mode = False) :
        self.title = title # (заголовок, строка)
        self.duration = duration # (продолжительность, секунды)
        self.time_now = time_now # (секунда остановки (изначально 0))
        self.adult_mode = adult_mode # (ограничение по возрасту, bool
                                     # (False по умолчанию))
##
#
class UrTube : #
    users = [] # (список объектов User)
    videos = []  # (список объектов Video)
    current_user =  [None] #current_user(текущий пользователь, User)
#
#
    def log_in(self, nickname, password) : # пытается найти пользователя в users
        # с такими же логином и паролем. Если такой пользователь существует,
        # то current_user меняется на найденного.
        for i in UrTube.users : #
            if nickname in i[0] : #
                self.password = i[1] #
                self.age = i[2] #
                UrTube.current_user = [self.nickname, self.password, self.age]
            return True
        else : #
            return False
#
    def register(self, nickname, password, age) : # добавляет пользователя в список,
        # (если пользователя с таким же nickname не существует ).
        # Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        # После регистрации, вход выполняется автоматически.
        #
        self.nickname = nickname # (имя пользователя, строка)
        #print(self.nickname)
        self.password = hash(password) # (в хэшированном виде, число)
        #print(self.password)
        self.age = age # (возраст, число)
        #print(self.age)
        for i in UrTube.users : #
            print(i)
            if nickname in i[0] : #
                self.password = i[1] #
                self.age = i[2] #
                UrTube.current_user = [self.nickname, self.password, self.age]
                print(f'Пользователь {nickname} уже существует')
                break
            #
            user = User(self.nickname, self.password, self.age) #
            current_user = [self.nickname, self.password, self.age]
            UrTube.users.append(current_user)  #
            UrTube.current_user =  current_user  #
        #input('  --')
#
    def log_out(self) : #  для сброса текущего пользователя на None.
        UrTube.current_user = [None]
        return True
#
    def add(self, *args) : # принимает неограниченное кол-во объектов класса Video и
#       # все добавляет в videos, если с таким же названием видео ещё не существует.
#       # В противном случае ничего не происходит.
        videos = UrTube.videos
        add = 1
        for i in args : #
            it = i.title
            if videos != [] :
                for j in videos : #
                    print(it)
                    print(j)
                    if j[0] == it :
                        add = 0
                #break
            #print(videos)
            if add == 1 : #
                video = [i.title, i.duration, i.adult_mode]
                print('video',video)
                UrTube.videos = videos.append(video)
        return videos
#user = User(self.nickname, self.password, self.age) #
            # current_user = [self.nickname, self.password, self.age]
            # UrTube.users.append(current_user)  #
            # UrTube.current_user =  current_user  #
#
    def get_videos(self, pstr) : # принимает поисковое слово и возвращает список названий
#           # всех видео, содержащих поисковое слово.
#           # Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
#           # (не учитывать регистр).
        videos = UrTube.videos
        lower_pstr = pstr.lower()
        rstr = ''
        if videos != [] :
            for i in videos :
                low_i = i.lower()
                if lower_pstr in low_i :
                    #print(f'{i}  ', end = '  ')
                    rstr += '  '+i
            return rstr
        return []
        #pass
#
    def watch_video(self, title) : # Для паузы между выводами секунд воспроизведения можно
            # использовать функцию sleep из модуля time.
#           Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
#           В противном случае выводить в консоль надпись:
#           "Войдите в аккаунт, чтобы смотреть видео"
#           Если видео найдено, следует учесть, что пользователю может быть отказано в
#           просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение:
#           "Вам нет 18 лет, пожалуйста покиньте страницу"
#           После воспроизведения нужно выводить: "Конец видео"
#
            #nickname = getattr(User, nickname, None)
            #if User(nickname) = nickname
            self.title = title
            videos = UrTube.videos
            #print(f'videos + {videos}')
            for i in videos :
                #print(f'FOR I  {i}')
                #print(f'FOR TITL  {i}')
                #ti = "'"+i+"'"
                #print(i)
                #print(title)
                if i == title :
                    #tivideo = title
                    #duvideo =
                    #advideo =

                    print(f'watch_video  {i}')
                    break

                    #print(f'watch_video  NONE')

        # return
        # if True :
        #     print(UrTube.current_user)
        # #if UrTube().current_user in UrTube().users and Video(self,title) in UrTube().videos : #
        #
        # return True
        # #video = Video(title)
        # time_dur = Video().duration
        # for i in time_dur : #
        #     print(i, end = ' ')
        #     time.sleep(1)
        #print("Войдите в аккаунт, чтобы смотреть видео")
        #print("Вам нет 18 лет, пожалуйста покиньте страницу")
        #return 'конец видео'
        #pass
#
##

#
#
ur = UrTube()
#print(ur.users)
#print(ur.videos)
#print(ur.current_user)
#user1 = User('Пользователь_1', 'xaxaxa', 25)
#print(user1.age)
#print(user1.nickname)
#print(user1.password)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#print(v2.title)
#print(v2.duration)
#print(v2.time_now)
#print(v2.adult_mode)
v1 = Video('Лучший язык программирования 2024 года', 200)
#print(f'{v1.title}, {v1.duration}, {v1.adult_mode}')
ur.add(v1, v2)
#print(ur.videos)
#print('лучший')
print(ur.get_videos('лучший'))
#print('ПРОГ')
print(ur.get_videos('ПРОГ'))
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#input(' ')
ur.watch_video('Для чего девушкам парень программист?')
print(ur.users)
print(ur.current_user)
#
#####
#
# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
#
# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
#
#
#   Конец задания
#
