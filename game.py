import random
import time
print("добро пожаловать это игра")
s = "продовец"
b = "охраник"
balance = 0
cassa = 1000
фразы = ["здравствуйте", "кгм здаров" ,"добрый день", "эу слыш дарова"]
товары = ["молоко", "хлеб" ,"яблоки", "валерьянки", "воды"]
бабка = ["а вот в наше время....*очень долгий расказ о ссср*", "вот у вас молодых всё одно на уме..... игры!!!", "а нам по новостям рассказали что нас всех заменит дипсик"]
a = input(f"где вы можете выбрать за кого играть. {s}/{b}:     ")
if a == "продовец":
    while cassa <= 1750:
        nps = random.randint(1, 100)
        случайная_фраза = random.choice(фразы)
        случайный_продукт = random.choice(товары)
        случайный_продукт1 = random.choice(товары)
        случайная_бабка = random.choice(бабка)
        print("вы выбрали играть за продовца хороший выбор!")
        time.sleep(0.5)
        print("день идёт и к вам подошёл первый покупатель ")
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
