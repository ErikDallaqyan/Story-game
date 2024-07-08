menu_english = ["|------------MENU------------|", "|Escape                      |", "|From                        |", "|Alkatraz                    |", "|Jail                        |", "|                            |", "|1.Play                      |", "|2.Settings                  |", "|____________________________|"]
menu_russian = ["|------------МЕНЮ------------|", "|Escape                      |", "|From                        |", "|Alkatraz                    |", "|Jail                        |", "|                            |", "|1.Играть                    |", "|2.Настройки                 |", "|____________________________|"]

def print_menu_english():
    for element in menu_english:
            print(element, end="\n")
    return " " 
def print_menu_russian():
    for item in menu_russian:
        print(item, end="\n")
    return " "
x = "***"
Language_x = 0
    
while True:
    if Language_x == 1 or Language_x == 0:
        print(print_menu_english())
    elif Language_x == 2:
        print(print_menu_russian())

    if Language_x == 1 or Language_x == 0:
        play_settings = int(input("Choose(1 for Play, 2 for Settings): "))
        if play_settings == 1:
            break
    
        if play_settings == 2:
            print("1.Language")
            print("2.Authors")
            Language_authors = int(input("Choose: "))
            if Language_authors == 2:
                print(x)
                print("The authors are: Erik Dallakyan and Alik Grigoryan")
            elif Language_authors == 1:
                print(x)
                print("1.English\n2.Russian")
            Language = int(input("Choose the language: "))
            if Language == 1:
                print("Language is set to English")
                Language_x = 1
            elif Language == 2:
                Language_x = 2
                print("Language is set to Russian")
                back_to_menu = input("Do you want to go back to the menu ('y' for Yes, 'n' for No): ").lower()
                if back_to_menu != "y":
                    break
    elif Language_x == 2:
        play_settings = int(input("Выбирай (1 чтобы начать игру, 2 чтобы открыть настройки): "))
        if play_settings == 1:
            break
        if play_settings == 2:
            print("1.Язык")
            print("2.Авторы")
            Language_authors = int(input("Выбирай: "))
            if Language_authors == 2:
                print(x)
                print("Авторы Алик Григорян, Эрик Даллакян")
            elif Language_authors == 1:
                print(x)
                print("1.Английский\n2.Русский")
                Language = int(input("Выбирай язык: "))
                if Language == 1:
                    print("Язык установлен на английский")
                    Language_x = 1
                elif Language == 2:
                    Language_x = 2
                    print("Язык установлен на русский")
                    back_to_menu = input("Хочешь ли ты вернуться в главное меню ('y' значит Да, 'n' значит Нет): ").lower()
                    if back_to_menu != "y":
                        break

if Language_x == 1 or Language_x == 0:
        if play_settings == 1:
            print(x)
            print("Your name is Jack․You got a prison sentence for bank robbery." "\n" "It was an ordinary morning, 2 policemen came to check on me. As always, they started making fun of me, after a while they said that someone gave me a cake.")
            cake_inside = int(input("What you will find in the cake?(1.file, 2.NRG drink, 3.Teleporter, 4.Rocket Launcher, 5.Cell phone):"))

            if cake_inside == 1:
                print(x)
                print("You use a file to leave the cell when suddenly a policeman notices you")
                policemen_room = int(input("What you will do?(1.Kick policeman, 2.Run away to an unknown room):"))
                if policemen_room == 1:
                    print(x)
                    print("Another police officer stuns you from behind")
                    print("*You loosed!*")
                elif policemen_room == 2:
                    print(x)
                    print("You run away into an unknown room, and a policeman runs after you")
                    grenade_chair = int(input("What do you use to escape?(1.Grenade, 2.Chair):"))
                    if grenade_chair == 1:
                        print(x)
                        print("You take a grenade and throw it towards the policeman, but it bounces off the wall and falls at your feet")
                        print("*You loosed!*")
                        print("Uhh... I don't know what to say about that one... ")
                    elif grenade_chair == 2:
                        print(x)
                        print("You use a chair to enter the ventilation")
                        ventilation = int(input("Where to go?(1.To left, 2.To right):"))
                        if ventilation == 1:
                            print(x)
                            print("You walk through the ventilation and hear some sounds. Suddenly you fall to where the police are talking")
                            print("*You loosed!*")
                        elif ventilation == 2:
                            print(x)
                            print("You end up on the roof")
                            roof = int(input("What will you use to jump off the roof?(1.Parachute, 2.Rope, 3.Plungers):"))
                            if roof == 1:
                                print(x)
                                print("You jump with a parachute, but it turns out to be an ordinary backpack.", "\n","You loosed", "\n", "Better luck next time.")
                            elif roof == 2:
                                print(x)
                                print("You use the rope and successfully descend. But you are crushed by robbers in a car who robbed the bank")
                                print("*You loosed!*")
                                print("This seems awfully familiar...")
                            elif roof == 3:
                                print(x)
                                print("You use plungers to go down. You have successfully descended.", "\n", "*Congratulations, you have successfully escaped from Alcatraz prison!!!*")
            elif cake_inside == 2:
                print(x)
                print("You are drinking NRG drink․ You are overwhelmed with energy, time seems to have slowed down, you leave prison without any obstacles. When suddenly you have a heart attack and die")
                print("*You loosed!*")
            elif cake_inside == 3:
                print(x)
                print("You use the teleporter to get out of prison. You find yourself in a shooting range and they accidentally shoot at you․")
                print("*You loosed!*")
                print("You just can't seem to get the hang of that thing can you?")
            elif cake_inside == 4:
                print(x)
                print("You fire a rocket launcher, but you don't notice that you're holding it backwards and you explode")
                print("*You loosed!*")
                print("Uh... Way to aim buddy...")
            elif cake_inside == 5:
                print(x)
                print("You call a lawyer and are taken to court. You are accused of robbing a bank. Your lawyer is trying to refute it. To do this, he needs to put forward evidence.")
                print("1.Floor Plans to bank. A diagram of the bank and it's surroundings.")
                print("2.Disgusting bag. The bag the defentant hid in in order to sneak into the bank.The knot is tied on the outside of the bag.")
                print("3.Shovel. Found near the bank.Bears fingerprints of the defentant")
                print("4.Mysterious device. A device whose use is unknown")
                print("5.Security Footage. Security footage of the night the intrusion.Shows the defendant leaving his disguise and setting off the alarm")
                print("6.Doctor's Analysis. Doctor's exam of the defentant done after arrest.Defentant suffered many bruises and cuts")
                Case = int(input("What you will choose to win the Case:"))
                if Case == 1:
                    print(x)
                    print("This has nothing to do with the case!")
                    print("*You loosed!*")
                    print("What kind of third-rate lawyer did you hire?")
                elif Case == 2:
                    print(x)
                    print("After much discussion, you have successfully won the case!")
                    print("*Congratulations, you have successfully escaped from Alcatraz prison!!!*")
                elif Case == 3:
                    print(x)
                    print("This has nothing to do with the case!")
                    print("*You loosed!*")
                    print("What kind of third-rate lawyer did you hire?")
                elif Case == 4:
                    print(x)
                    print("This has nothing to do with the case!")
                    print("*You loosed!*")
                    print("What kind of third-rate lawyer did you hire?")
                elif Case == 5:
                    print(x)
                    print("This has nothing to do with the case!")
                    print("*You loosed!*")
                    print("What kind of third-rate lawyer did you hire?")
                elif Case == 6:
                    print(x)
                    print("This has nothing to do with the case!")
                    print("*You loosed!*")
                    print("What kind of third-rate lawyer did you hire?")
elif Language_x == 2:
    if play_settings == 1:
        print(x)
        print("Твое имя Иван․Ты сел в тюрьму за ограбление банка." "\n" "Это было самое обычное утро,2 полицейских пришли меня проверить. Как всегда, они начали подшучивать надо мной, спустья некоторое время они сказали что кто-то попросил передать мне торт.")
        cake_inside = int(input("Что ты найдешь в торте?(1.Напильник, 2.Энергетик, 3.Телепортер, 4.Базука, 5.Сотовый телефон):"))
        if cake_inside == 1:
            print(x)
            print("Ты выбираешься из камеры спомощью напильника, вдруг тебя замечает полицейский")
            policemen_room = int(input("Что ты будешь делать?(1.Ударить полицейского, 2.Убежать в неизвестную комнату):"))
            if policemen_room == 1:
                print(x)
                print("Другой полицейский бьет тебя сзади электрошокером")
                print("*Ты проиграл!*")
            elif policemen_room == 2:
                print(x)
                print("Ты убегаешь в неизвестную комнату.За тобой бежит полицейский")
                grenade_chair = int(input("Что ты используешь чтобы сбежать?(1.Граната, 2.Стул):"))
                if grenade_chair == 1:
                    print(x)
                    print("Ты берешь гранату и кидаешь ее в сторону полицейского,но она отскакивает от стены и падает у тебя под ногами")
                    print("*Ты проиграл!*")
                    print("Охх... Я даже не знаю что скачать насчет этого... ")
                elif grenade_chair == 2:
                    print(x)
                    print("Ты используешь стул чтобы войти в вентиляцию")
                    ventilation = int(input("В какую сторону пойти?(1.На лево, 2.На право):"))
                    if ventilation == 1:
                        print(x)
                        print("Ты идешь по вентиляции и слышишь какие то голоса.Как вдруг ты падаешь прамо туда где проводили собеседование полицейские")
                        print("*Ты проиграл!*")
                    elif ventilation == 2:
                        print(x)
                        print("Ты забираешься на крышу")
                        roof = int(input("Что ты используешь чтобы спрыгнуть с кришы?(1.Парашют, 2.Крюк, 3.Присоски):"))
                        if roof == 1:
                            print(x)
                            print("Вы прыгаете с парашютом, а это оказывается обычный рюкзак.", "\n","*Вы проиграли!*", "\n", "Удачи в следующий раз.")
                        elif roof == 2:
                            print(x)
                            print("Ты используешь крюк и успешно спускаешся.Но вы попадаете под машину грабителей которые только что ограбили банк")
                            print("*Вы проиграли!*")
                            print("Это кажется ужасно знакомым...")
                        elif roof == 3:
                            print(x)
                            print("Вы используете присоски, чтобы спуститься вниз. Вы успешно спустились.", "\n", "*Поздравляем, вы успешно сбежали из тюрьмы Алькатрас!!!*")
        elif cake_inside == 2:
            print(x)
            print("Ты выпиваешь энергетик․ Вас переполняет энергия, время как будто замедлилось, вы беспрепятственно выходите из тюрьмы. Когда вдруг у тебя случится сердечный приступ и ты умираешь")
            print("*Вы проиграли!*")
        elif cake_inside == 3:
            print(x)
            print("Вы используете телепортер, чтобы выбраться из тюрьмы.Но вы оказываетесь в тире и в вас случайно стреляют․")
            print("*Вы проиграли!*")
            print("Кажется, ты просто не можешь разобраться в этой штуке, не так ли?")
        elif cake_inside == 4:
            print(x)
            print("Вы стреляете из базуки, но не замечаете, что держите ее задом на перед и вы взрываетесь.")
            print("*Вы проиграли!*")
            print("Э-э... Прицеливайся приятель...")
        elif cake_inside == 5:
            print(x)
            print("Вы звоните адвокату и вас везут в суд. Вас обвиняют в ограблении банка. Ваш адвокат пытается это опровергнуть. Для этого ему необходимо представить доказательства.")
            print("1.Планы банка. Схема банка и его окрестностей.")
            print("2.Отвратительная сумка. Сумка, в которой обвиняемый спрятался, чтобы проникнуть в банк. Узел завязывается на внешней стороне сумки.")
            print("3.Лопата. Найден возле банка. Есть отпечатки пальцев обвиняемого.")
            print("4.Таинственное устройство. Устройство, использование которого неизвестно")
            print("5.Видеозаписи безопасности. Кадры с камер видеонаблюдения в ночь вторжения. Видно, как обвиняемый выходит из маскировки и включает сигнализацию.")
            print("6.Анализ врача. Осмотр врача подсудимого проводился после ареста. Подсудимый получил множество синяков и порезов.")
            Case = int(input("Что ты выберешь чтобы выиграть суд:"))
            if Case == 1:
                print(x)
                print("Это не имеет никакого отношения к делу!")
                print("*Вы проиграли!*")
                print("Какого третьесортного адвоката вы наняли?")
            elif Case == 2:
                print(x)
                print("После долгих обсуждений вы успешно выиграли дело!")
                print("*Поздравляем, вы успешно сбежали из тюрьмы Алькатрас!!!*")
            elif Case == 3:
                print(x)
                print("Это не имеет никакого отношения к делу!")
                print("*Вы проиграли!*")
                print("Какого третьесортного адвоката вы наняли?")
            elif Case == 4:
                print(x)
                print("Это не имеет никакого отношения к делу!")
                print("*Вы проиграли!*")
                print("Какого третьесортного адвоката вы наняли?")
            elif Case == 5:
                print(x)
                print("Это не имеет никакого отношения к делу!")
                print("*Вы проиграли!*")
                print("Какого третьесортного адвоката вы наняли?")
            elif Case == 6:
                print(x)
                print("Это не имеет никакого отношения к делу!")
                print("*Вы проиграли!*")
                print("Какого третьесортного адвоката вы наняли?")