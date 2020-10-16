from random import choice
import os


def History():
    level1 = choice(['Земля сгорает',
                     'Земля замерзает',
                     'Земля падает на Солнце',
                     'Земные учёные',
                     'Земля подвергается нашествию',
                     'Земля сталкивается с огромной кометой'])

    if level1 == 'Земля сгорает' or level1 == 'Земля замерзает' or level1 == 'Земля падает на Солнце':
        level2 = choice(['и все гибнут (конец)',
                         'и почти все гибнут (конец)'])
        level3 = level4 = level5 = level6 = level7 = level8 = level9 = level10 = level11 = level12 = ''
        return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12

    elif level1 == 'Земные учёные':
        level2 = choice(['создают',
                         'открывают'])
        level3 = choice(['маленьких',
                         'огромных'])
        level4 = choice(['насекомых,',
                         'пресмыкающихся,',
                         'роботов,',
                         'внеземных существ,'])
        level5 = 'которые'
        level6 = choice(['желают наших женщин',
                         'ведут себя дружелюбно (конец)',
                         'ведут себя дружелюбно, но их никто не понимает',
                         'не понимают нас',
                         'отлично понимают нас',
                         'воспринимают нас только как пищу'])
        if level6 == 'ведут себя дружелюбно (конец)':
            level7 = level8 = level9 = level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        elif level6 == 'желают наших женщин':
            level7 = choice(['похищают их и съедают (конец)',
                             'и являются радиоактивными',
                             'и являются нерадиоактивными'])
            if level7 == 'похищают их и съедают (конец)':
                level8 = level9 = level10 = level11 = level12 = ''
                return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        elif level6 == 'воспринимают нас только как пищу':
            level7 = choice(['и съедают нас (конец)',
                             'и являются радиоактивными',
                             'и являются нерадиоактивными'])
            if level7 == 'и съедают нас (конец)':
                level8 = level9 = level10 = level11 = level12 = ''
                return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        else:
            level7 = choice(['и являются радиоактивными',
                             'и являются нерадиоактивными'])
        level8 = choice(['и могут быть уничтожены',
                         'и не могут быть уничтожены'])
        if level8 == 'и могут быть уничтожены':
            level9 = choice(['толпой парней с факелами (конец)',
                             'сухопутной армией (конец)',
                             'морским флотом (конец)',
                             'авиацией (конец)',
                             'морской пехотой (конец)',
                             'войсками береговой охраны (конец)',
                             'атомной бомбой (конец)'])
            level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        elif level8 == 'и не могут быть уничтожены':
            level9 = choice(['толпой парней с факелами',
                             'сухопутной армией',
                             'морским флотом',
                             'авиацией',
                             'морской пехотой',
                             'войсками береговой охраны',
                             'атомной бомбой'])
            level10 = choice(['но учёные изобретают новое оружие',
                              'но',
                              'но они умирают от чёрной оспы (конец)',
                              'и поэтому они убивают нас (конец)',
                              'и поэтому они устанавливают систему доброжелательной диктатуры (конец)',
                              'и поэтому они съедают нас (конец)'])
            if level10 == 'но учёные изобретают новое оружие':
                level11 = choice(['которое отказывает',
                                  'которое их убивает (конец)',
                                  'которое превращает их в мерзкие глыбы (конец)'])
                if level11 == 'которое отказывает':
                    level12 = choice(['но они умирают от чёрной оспы (конец)',
                                      'и поэтому они убивают нас (конец)',
                                      'и поэтому они устанавливают систему доброжелательной диктатуры (конец)',
                                      'и поэтому они съедают нас (конец)'])
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
                else:
                    level12 = ''
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
            elif level10 == 'но':
                level11 = choice(['один хитрый парень убеждает их, что люди "ОК"',
                                  'священник рассказывает им о Боге',
                                  'влюбляются в красивую девушку'])
                if level11 == 'влюбляются в красивую девушку':
                    level12 = choice(['женятся и живут долго и счастливо (конец)',
                                      'и они превращаются в мерзкие глыбы (конец)',
                                      'и они улетают (конец)',
                                      'и они умирают (конец)'])
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
                else:
                    level12 = choice(['и они превращаются в мерзкие глыбы (конец)',
                                      'и они улетают (конец)',
                                      'и они умирают (конец)'])
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
            else:
                level11 = level12 = ''
                return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        else:
            level9 = level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12

    elif level1 == 'Земля подвергается нашествию':
        level2 = choice(['маленьких',
                         'огромных'])
        level3 = choice(['насекомых,',
                         'пресмыкающихся,',
                         'роботов,',
                         'внеземных существ,',
                         'марсиан,',
                         'селенитов,',
                         'внегалактических чудовищ,',
                         'различных странных предметов,'])
        level4 = 'которые'
        level5 = choice(['желают наших женщин',
                         'ведут себя дружелюбно (конец)',
                         'ведут себя дружелюбно, но их никто не понимает',
                         'не понимают нас',
                         'отлично понимают нас',
                         'воспринимают нас только как пищу'])
        if level5 == 'ведут себя дружелюбно (конец)':
            level6 = level7 = level8 = level9 = level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        elif level5 == 'желают наших женщин':
            level6 = choice(['похищают их и съедают (конец)',
                             'и являются радиоактивными',
                             'и являются нерадиоактивными'])
            if level6 == 'похищают их и съедают (конец)':
                level7 = level8 = level9 = level10 = level11 = level12 = ''
                return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        elif level5 == 'воспринимают нас только как пищу':
            level6 = choice(['и съедают нас (конец)',
                             'и являются радиоактивными',
                             'и являются нерадиоактивными'])
            if level6 == 'и съедают нас (конец)':
                level7 = level8 = level9 = level10 = level11 = level12 = ''
                return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        else:
            level6 = choice(['и являются радиоактивными',
                             'и являются нерадиоактивными'])
        level7 = choice(['и могут быть уничтожены',
                         'и не могут быть уничтожены'])
        if level7 == 'и могут быть уничтожены':
            level8 = choice(['толпой парней с факелами (конец)',
                             'сухопутной армией (конец)',
                             'морским флотом (конец)',
                             'авиацией (конец)',
                             'морской пехотой (конец)',
                             'войсками береговой охраны (конец)',
                             'атомной бомбой (конец)'])
            level9 = level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        elif level7 == 'и не могут быть уничтожены':
            level8 = choice(['толпой парней с факелами',
                             'сухопутной армией',
                             'морским флотом',
                             'авиацией',
                             'морской пехотой',
                             'войсками береговой охраны',
                             'атомной бомбой'])
            level9 = choice(['но учёные изобретают новое оружие',
                             'но',
                             'но они умирают от чёрной оспы (конец)',
                             'и поэтому они убивают нас (конец)',
                             'и поэтому они устанавливают систему доброжелательной диктатуры (конец)',
                             'и поэтому они съедают нас (конец)'])
            if level9 == 'но учёные изобретают новое оружие':
                level10 = choice(['которое отказывает',
                                  'которое их убивает (конец)',
                                  'которое превращает их в мерзкие глыбы (конец)'])
                if level10 == 'которое отказывает':
                    level11 = choice(['но они умирают от чёрной оспы (конец)',
                                      'и поэтому они убивают нас (конец)',
                                      'и поэтому они устанавливают систему доброжелательной диктатуры (конец)',
                                      'и поэтому они съедают нас (конец)'])
                    level12 = ''
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
                else:
                    level11 = level12 = ''
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
            elif level9 == 'но':
                level10 = choice(['один хитрый парень убеждает их, что люди "ОК"',
                                  'священник рассказывает им о Боге',
                                  'влюбляются в красивую девушку'])
                if level10 == 'влюбляются в красивую девушку':
                    level11 = choice(['женятся и живут долго и счастливо (конец)',
                                      'и они превращаются в мерзкие глыбы (конец)',
                                      'и они улетают (конец)',
                                      'и они умирают (конец)'])
                    level12 = ''
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
                else:
                    level11 = choice(['и они превращаются в мерзкие глыбы (конец)',
                                      'и они улетают (конец)',
                                      'и они умирают (конец)'])
                    level12 = ''
                    return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
            else:
                level10 = level11 = level12 = ''
                return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12

    elif level1 == 'Земля сталкивается с огромной кометой':
        level2 = choice(['и разрушается (конец)',
                         'и остаётся невредимой (конец)',
                         'и не разрушается, но'])
        if level2 == 'и не разрушается, но':
            level3 = choice(['все гибнут (конец)',
                             'почти все гибнут (конец)'])
            level4 = level5 = level6 = level7 = level8 = level9 = level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12
        else:
            level3 = level4 = level5 = level6 = level7 = level8 = level9 = level10 = level11 = level12 = ''
            return level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12


historyamount = 0
while historyamount < 1000:
    if not os.path.isfile('histories.txt'):
        open('histories.txt', 'w', encoding='utf-8').close()
    file = open('histories.txt', 'r', encoding='utf-8')
    histories = file.readlines()
    file.close()
    historylevels = History()
    history = ''
    for level in historylevels:
        if level != '':
            history += level + ' '
    history = history[:-1] + '\n'
    if history not in histories:
        with open('histories.txt', 'a+', encoding='utf-8') as historiesfile:
            historiesfile.write(history)
            historyamount += 1
            historiesfile.close()
