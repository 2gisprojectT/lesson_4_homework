# ProjectT 2015 v2 - Домашнее задание #4
## Задание 1.
### Попытаться использовать изученные техники тест-дизайна и дополнить тесты из домашки 2
Done!

## Задание 2.
### Посмотреть доклад и ответить на вопросы
https://dl.dropboxusercontent.com/u/16263157/chiefconfetqa_2013_fall_rukol.wmv - видео доклада

https://dl.dropboxusercontent.com/u/16263157/chiefconfetqa_2013_fall_rukol.pdf - слайды доклада

#### Вопросы:
1. почему защита 1 уровня "что-нибудь потестировать" не работает?
Потому, что нет целостности, существует предвзятость в выборе

2. почему не помогает просто написать больше тестов?
Наличие документированных тестов ситуацию не спасает, а вот затраты увеличиваются

3. зачем нужно анализировать?
Поймем, какие риски самые основные, разберемся в архитектуре, тесты становятся более адаптивными

4. перечислите какие шаги нам нужноп выполнять, чтобы спроектировать хорошую защиту от багов? иными словами, опишите стратегию действий
- Анализ продукта и условий
- Цели тестирования
- Согласование и учет потребностей
- Понять какие тесты нам собственно нужно делать

5. что мы должны сделать в рамках анализа? то есть что будет на выходе нашего анализа?
- Карта функционала
- История ошибок, риски возникновения
- Приоритизация функционала
- Критичность потенциальных ошибок
- Результаты: карта функционала, что с чем важно тестить, что важнее всего, типы тестирования, условия окружения, что чаще всего ломается, что критичнее для пользователя

6. зачем расставлять приоритеты? от чего зависит приоритет функциональности? на основании чего можно определить приоритет функциональности?
Мы понимает "что тестировать", приоритеты могут быть у всех разные, например у банковского ПО любая ошибка может стоить больших денег

7. Какие бывают внещние факторы, которые могут повлиять на тестирование? зачем учитывать внешние факторы?
- Длительность итераций
- Регулярность публичных релизов
- Ограничение по времени
- Допустимость и недопустимость определенных ошибок
- Возможность автоматизации
Потому что вн факторы, напирмер дедлайн, могу сильно влиять на процесс, например мы не сможем выполнять длительные итерации если у нас завтра дедлайн. Строит систему в зависимости от внешних условий

8. охаректеризуйте разные комплекты тестов (зачем? как выбрать тесты в комплект? как часто прогонять? в чем задача каждого набора? нужно проводить для одной сборки или можно на нескольких? и тд): BVT, UAT, FTP? какие интересные особенности для каждого комплекта вы запомнили?
BVT(почти что смоук): максимально быстро оцениваем качество ПО, находим самые критичные ошибки сразу, тольько важные и опасные ошибки, минимизация сроков выполнения, максимальная автоматизация, каждый раз в новом билде
FTP(полное тестирование): максимально полно, тщательнейший анализ, все возможные тесты, оценка так сказать максимальной проверки качества продукта, ищем возможности для расширения ресурсов, автоматизации и прочего, могут выполняться несколько сборок подряд
UAT(готовность к релизу):тесты необходимые для успешного использования продукта пользователями, выполнять на одной сборке, готовы мы к релизу или нет
Сначала BVT самые быстрые и маленькие, потом UAT. На самом нижнем уровне с самыме мелкими ошибками FTP.

9. что делать, если пропустили баг в релиз
- Паникуем!)
- Анализируем причину пропуска
- Насколько это критично
- Какой набор расширить
- Расширяем первоначальный анализ

#### Интересные вопросы и ответы к презентации:
###### Q: А кто должен устанавливать контакт с пользователяими? Аналитики? Тестировщики? Специально обученные люди?[Sergey Petrov] 
Я не знаю стандартного решения :( Есть компании, где к пользователю близко подходить нельзя, писать ему письма нельзя, но можно упросить РМа выслать ему анкету с вопросами от нашей команды. В некоторых командах очень даже общаемся лично. В некоторых тестировщики совмещают задачи с ролью бизнес-аналитика и даже часто ездят к заказчику.
Универсальных решений нет, главное стремиться к получению максимума информации от пользователя, чтобы не жить в информационном вакууме и не тестировать "как-то, не знаю, как там настоящие пользователи это делают и что им важно".

###### Q: BVT 2 часа? Это же много! BVT - это до 15 минут, разве не так?[Natalya Suhanova] 
Если ваше BVT за 15 минут гарантирует что весь основной функционал как-то запускается, то это хорошо! Когда тестируется клиент-серверное приложение, устанавливающее БД, веб-сервер и т.д. при установке, то у нас зачастую при старте автотестов 30 минут уходит только на поднятие окружения. А если из полусотни тысяч тестов в BVT мы включили 400, то это ещё 3 часа на прогон (было бы критично - параллелили бы :)). На небольших веб-проектах, действительно, 15 минут вполне достаточно.

###### Q: Иногда на BVT и 4 часа мало. Зависит от сложности проекта[Nikolay Kalin]
###### Q: названий много, суть одна: "можно начать тестить или нельзя". думаю длительность зависит от системы... но не более одного дня)[Stanislav Polyakov] 

Вопрос исследования условий: есть ли у вас эти 4 часа? Есть ли целый день? Многие привыкли что-то делать, а как начинают задавать вопросы, обсуждать, и оказывается, что 4 или 8 часов на BVT - большая проблема для проекта, особенно если релизы частые. В этом случае надо искать способы укорачивать: убирать лишнее, автоматизировать, параллелить и т.д.

###### Q: Наташа, у нас проектная команда очень маленькая и при нахождении ошибок на BVT их исправляют локально на стенде. и нет возможности вести статистику по неудачным сборкам (они у нас все удачные получаются). Есть ли смысл глобально менять процесс и отслеживать эту статистику?[Наталья Боброва] 
Повторю устный ответ: чаще всего, это полезная статистика! Заводить все ошибки по отдельности не обязательно, а вот помечать фейлы тестов для того, чтобы оценивать, как часто у нас не проходит BVT и как часто не проходит каждый конкретный тест - очень полезно!

###### Q: Все вышесказанное за сколько времени можно реализовать в отделе тестирования из 6-ти человек? Или одной жизни не будет достаточно?[Igor Cherednichenko]
Размер отдела не очень показателен... Если бы тебе вместо 6 дали 40, то тебе стало бы проще это сделать :) В зависимости от проекта и загруженности "текучкой", я думаю 2-12 месяцев.

###### Q: а если продукт библиотечного типа (модульный) и может быть внедрен только частями (отдельными модулями). Как определить достаточность UAT?[Наталья Боброва] 
Но интеграцию модулей надо тестировать? И могут быть разные комбинации модулей у пользователей? Смотреть для BVT основную конфигурацию, для UAT основные, для FTP все существующие :)

###### Q: Стратегию тестирования для проекта писать надо, в ней все сие и описывать. Есть примеры в стандартах, да и в интернетах. [Максим Гриневич] 
Примеры-то есть, но брать использовать любую из интернета не советую, всегда надо адаптировать под себя. Сколько я ни стараюсь шаблонизировать задачу "написать стратегию" и сделать её чем-то одинаковым, ремесленнической работой - ни разу не получалось, всегда свои особенности и свои форматы получаются.

###### Q: почему тогда не делать всегда FTP? Наимаскимальнейшее покрытие же[Екатерина Скорых] 
В идеально мире при наличии ресурсов так и надо. Я увы с таким не сталкивалась, только на ОЧЕНЬ маленьких проектах.

###### Q: А если ошибка стратегии - до свидания мэр? =([Stanislav Polyakov] 
Кто никогда не ошибался, пусть первый кинет в меня камень :) Ошибки - это опыт. Надо оперативно их отлавливать и решать проблемы.

###### Q: Уровень качества продукта и количества пропущенных ошибко зависит от проекта, перфекционизм тут не помощник - приходит профф выгорание. [Максим Гриневич] 
У каждого есть право на свою религию :) Согласиться не могу, но и спорить смысла не вижу.

###### Q: Еще нужна качественная техподдержка - оперативное реагирование на репорты пользователей и исправление баг может повысить лояльность сильнее чем отсутствие бага[Natalya Suhanova] 
Да! Согласна, из проблемы хорошая техподдержка всегда даже пользу выбьет :)

###### Q: что по вашей схеме соответствует Regression ?[Viktor Bezhenar]
 BVT и UAT - регрессионное тестирование. FTP расширяется новым функционалом и постепенно тоже становится в основном регрессионным.

###### Q: Если сборка состоит ещё из аппаратной части, часто делать сборки очень проблематично, точнее долго обновлять тестовый стенд. Поэтому вопрос по срокам ..[Sergey Tolkunov] 
Я мало работала с АПК, но в наших случаях "железо" менялось раз в полгода - надо было только заливать на него обновления ПО, а это так же быстро и автоматизируемо. 
