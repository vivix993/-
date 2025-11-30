import random
import time
print("добро пожаловать это игра")
s = "продовец"
b = "охранник"
balance = 0
cassa = 1000
фразы = ["здравствуйте", "кгм здаров" ,"добрый день", "эу слыш дарова"]
товары = ["молоко", "хлеб" ,"яблоки", "валерьянки", "воды"]
бабка = ["а вот в наше время....*очень долгий расказ о ссср*", "вот у вас молодых всё одно на уме..... игры!!!", "а нам по новостям рассказали что нас всех заменит дипсик"]
a = input(f"где вы можете выбрать за кого играть. {s}/{b}:     ")
if a == "продовец":
    while cassa <= 1750  or balance >= 450:
        nps = random.randint(1, 100)
        случайная_фраза = random.choice(фразы)
        случайный_продукт = random.choice(товары)
        случайный_продукт1 = random.choice(товары)
        случайная_бабка = random.choice(бабка)
        time.sleep(0.5)
        print("день идёт и к вам подошёл покупатель ")
        time.sleep(0.5)
        if nps <= 25:
            print("нечего не обычного")
            time.sleep(0.5)
            print(f"НПС - {случайная_фраза} дайте {случайный_продукт}")
            time.sleep(0.5)
            деньги = random.randint(50, 250)
            print(f"он оплачивает {деньги} рублей и уходит")
            time.sleep(0.5)
            print("нажмите на 1 если хотите украсть", деньги)
            time.sleep(0.3)
            кража = int(input(   ))
            if кража == 1:
                print("главное чтоб начальник не заметил")
                time.sleep(2)
                balance = balance + деньги
                print(f"новый баланс {balance}")
                time.sleep(1)
            else:
                print("кража это плохо молодец")
                time.sleep(1)
                cassa = cassa + деньги
                print(f"новый баланс кассы {cassa}")
                time.sleep(1)
                i = int(input("хотите выйти? 1/2   "))
                time.sleep(1)
                if i == 1:
                    print("хорошо")
                    time.sleep(1)
                    break
                else:
                    print("продолжаем")
                    time.sleep(1)
        elif nps <= 50:
            print("страх пустился по телу прошол начальник")
            time.sleep(0.5)
            print("начальник - ну привет дружочек как у тебя дела?")
            time.sleep(1.5)
            print("я тут тебя пришёл проверить")
            time.sleep(0.5)
            if balance > 0:
                print("дружочек до меня тут слушок дошёл что ты воруешь это правда?")
                time.sleep(0.5)
                диалог = input("нет\да     ")
                time.sleep(0.5)
                if диалог == "нет":
                    проверка = random.randint(1, 100)
                    if проверка <= 40:
                        print("*смотрит кассу* \n ну вот ты и попался дружок УВОЛЕН")
                        time.sleep(2)
                        exit()
                    else:
                        print("ну ладно я доверюсь тебе")
                        time.sleep(0.5)
                        i = int(input("хотите выйти? 1/2   "))
                        time.sleep(0.5)
                        if i == 1:
                            print("хорошо")
                            time.sleep(0.5)
                            break
                        else:
                            print("продолжаем")
                            time.sleep(0.5)
                else:
                    print("ну ладно рассуж сознался прощяю на первый раз \n *криком* НО НА СЛЕДУЮЩИЙ РАЗ Я ТЕБЕ РУКИ ОТОРВУ")
                    time.sleep(2)
            else:
                print("ну ладно я тебя проверил я пошол пока")
                time.sleep(0.5)
        elif nps <= 75:
            print("что то не так")
            time.sleep(1.5)
            print("НПС - эй слыш быстро гони бабки")
            time.sleep(0.5)
            у = int(input("вы можете сопротивлятся нажав на 1    "))
            time.sleep(0.5)
            if у == 1:
                resist = random.randint(1,100)
                if resist <= 70:
                   print("сопротивление прошло успешно")
                   time.sleep(0.5)
                else:
                   print("сопротивлятся не пролучилось")
                   time.sleep(1.5)
                   vor_gra = random.randint(400, 650)
                   cassa = cassa - vor_gra
                   print(f"вор забрал {vor_gra}")
                   time.sleep(0.5)
                   print(f"новый баланс кассы {cassa}")
                   time.sleep(0.5)
            else:
                print("вы не сопротивлялись и вор взял всё")
                time.sleep(0.5)
                cassa= cassa * 0
                print(f"новый баланс кассы {cassa}")
                time.sleep(0.5)
                i = int(input("хотите выйти? 1/2   "))
                time.sleep(0.5)
                if i == 1:
                    print("хорошо")
                    time.sleep(0.5)
                    break
                else:
                    print("продолжаем")
                    time.sleep(0.5)
        else:
            print("запахло пирожками мммм вкусными")
            time.sleep(1.5)
            print("эй внучок здраствуй")
            time.sleep(1.5)
            print(случайная_бабка)
            time.sleep(5)
            скидка = input("внучок дай скидочку. *как же она надоела балтать* 1/2       ")
            time.sleep(0.5)
            if скидка == 1:
                скидочка = random.randint(50, 70)
                print(f"бабка покупает {товары} за {скидочка}")
                print("нажмите на 1 если хотите украсть", скидочка)
                time.sleep(0.3)
                кража = int(input(   ))
                if кража == 1:
                    print("главное чтоб начальник не заметил")
                    time.sleep(2)
                    balance = balance + скидочка
                    print(f"новый баланс {balance}")
                    time.sleep(1)
                else:
                    print("кража это плохо молодец")
                    time.sleep(1)
                    cassa = cassa + скидочка
                    print(f"новый баланс кассы {cassa}")
                    time.sleep(1)
                    i = int(input("хотите выйти? 1/2   "))
                    time.sleep(1)
                    if i == 1:
                       print("хорошо")
                       time.sleep(1)
                       break
                    else:
                       print("продолжаем")
                       time.sleep(1)
    print("молодец ты прошол игру 'продовец' ")
    exit()
elif a == "охранник":
    HP = 100
    стресс = 0
    HPbot = 120
    print("смена начинается")
    time.sleep(0.5)
    def personash (стресс):
        print("*тук тук тук*")
        time.sleep(0.5)
        print("вы можете открыть дверь \n 1 - открыть \n 2 - не открывать")
        time.sleep(0.5)
        choice = int(input("ваш выбор:   "))
        time.sleep(0.5)
        if choice == 1:
            print("вы решили открыть дверь \n там стоял пьяница и началь что то барматать \n прогнать его? \n 1 - да \n 2 - нет \n 3 - позвать его к себе")
            time.sleep(0.5)
            choice1 = int(input("ваш выбор:   "))
            time.sleep(0.5)
            if choice1 == 1:
                print("вы прогнали его \n и он что то борматал")
                time.sleep(0.5)
                стресс += 5
            elif choice1 == 2:
                print("вы решили его не прогонять и он стоял под дверью и что то говорил")
                time.sleep(0.5)
                стресс += 10
            elif choice1 == 3:
                print("вы решили его не прогонять и пригласить к себе \n в замен он дал вам выпить \n вы проснулись утром")
                time.sleep(0.5)
                стресс -= 50
                exit("вы завершили игру на концовку: бухой продяга")
                time.sleep(2.5)
            else:
                print("надо ввести цифры от 1 до 3")
                time.sleep(0.5)
        elif choice == 2:
            print("вы решили не открывать дверь")
            time.sleep(0.5)
            стресс += 30
        else:
            print("надо ввести цифры от 1 до 2")
            time.sleep(0.5)
        return стресс
    стресс = personash(стресс)
    print(f"ваш новый стресс {стресс}")
    time.sleep(3.5)
    def event (стресс):
        print("вы слышете стук об окно")
        time.sleep(0.5)
        print("это были мальчики которые кидали снежки в окно")
        rando1m = random.randint(10, 30)
        стресс += rando1m
        print(f"стрес = {стресс}")
        time.sleep(0.5)
        return(стресс)
    def event1 (стресс):
        print("вы выходите покурить открываете дверь \n и находите  магическую таблетку \n хотите её принять? \n 1 - да \n 2 - нет ")
        time.sleep(0.5)
        choice = int(input())
        if choice == 1:
            print("вы принимаете эту таблетку (ты псих?)")
            time.sleep(0.5)
            rando1m = random.randint(10, 20)
            стресс -= rando1m
            print(f"стрес = {стресс}")
            time.sleep(0.5)
        else:
            print("как хочешь (ура норм человек)")
            time.sleep(0.5)
        return стресс
    стресс = event1(стресс)
    def event2 (HP):
        print("надо бы почистить пушку")
        time.sleep(0.5)
        rando1m = random.randint(0,100)
        if rando1m >= 70:
            print("вы чистели ружьё и случайно нажали на курок \n вы умерли")
            time.sleep(2.5)
            print("вы закончили игру на концовку: ратяпа")
            time.sleep(1.5)
            HP1 = random.randint(40, 100)
            HP -= HP1
            exit()
        else:
            print("вы замечательно почистели ружьё")
            time.sleep(0.5)
        return HP
    def bot (HP, HPbot):
        print("к вам в хижену вламывается *кто то* \n у вас начинается бой")
        def boi (HP, HPbot):
            while HP > 0 and HPbot > 0:
                print("внимание....")
                time.sleep(5.5)
                print("БЫСТРЕЕ НАЖМИ ЧТО УГОДНО \n чтобы ударить противника")
                start = time.time()
                input()
                end = time.time()
                a = end - start
                if a <= 1:
                    print("критический удар")
                    hp1 = random.randint(70, 140)
                    HPbot -= hp1
                    if HPbot >= 120:
                        print("ОГО ТЫ ВЫРУБИЛ ЕГО")
                    else:
                        print("это был замечательный удар \n но недостаточно")
                elif a <= 2:
                    print("удар!!!")
                    hp1 = random.randint(40, 90)
                    print(f"ваш урон {hp1}")
                    print(f"твоё хп = {HP}, хп врага = {HPbot}")
                    HPbot -= hp1
                elif a <= 3:
                    print("так себе удар")
                    hp1 = random.randint(10, 40)
                    print(f"ваш урон {hp1}")
                    print(f"твоё хп = {HP}, хп врага = {HPbot}")
                    HPbot -= hp1
                else:
                    pot = random.randint(20, 40)
                    print(f"ты не успел \n от нанёс по тебе {pot}")
                    print(f"твоё хп = {HP}, хп врага = {HPbot}")
                    if HP <= 0:
                        print("он тебя вырубил")
                    elif HPbot <= 0:
                        print("ты победил")
            return HP, HPbot
        return boi (HP, HPbot)
    while HP > 0 or стресс < 100:
      print(f"ваше состояние хп = {HP}, стресс = {стресс}")
      time.sleep(1.5)
      cobtia = random.randint(1, 5)
      if cobtia == 1:
          стресс = event1(стресс)
      elif cobtia == 2:
          стресс = event(стресс)
      elif cobtia == 3:
          стресс = personash(стресс)
      elif cobtia == 4:
          HP = event2(HP)
      elif cobtia == 5:
          HP, HPbot = bot(HP, HPbot)