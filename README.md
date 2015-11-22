# ProjectT 2015 v2 - Домашнее задание #4
## Задание 1.
### Использовал, выполнил :)

## Задание 2.
### Посмотреть доклад и ответить на вопросы
https://dl.dropboxusercontent.com/u/16263157/chiefconfetqa_2013_fall_rukol.wmv - видео доклада

https://dl.dropboxusercontent.com/u/16263157/chiefconfetqa_2013_fall_rukol.pdf - слайды доклада

#### Вопросы:
1. почему защита 1 уровня "что-нибудь потестировать" не работает?
Нет целостности тестов. "Что-то" лучше работает, "что-то хуже".
Предвзятость в выборе. Зависимоть тестирования от личных предпочтений тестировщика (найти более простые проверки, чтобы найти больше багов)

2. почему не помогает просто написать больше тестов?
Более высокие затраты на их нахождение, документацию. Найдём больше ошибок, но всё равно неизбежно пропустим многие. Замедлим процесс разработки продукта.

3. зачем нужно анализировать?
Меньше затрат на нахождение всевозможных ошибок. Более адаптивные тесты => меньше ошибок.

4. перечислите какие шаги нам нужноп выполнять, чтобы спроектировать хорошую защиту от багов? иными словами, опишите стратегию действий
Проанализировать продукт, внешние условия.
Выделить цели тестов: Зачем тестируем? В каких объёмах?
Согласовать и учитывать внешние потребности проекта: Ожидание пользователей, критичность потенциальных ошибок и сроки выпуска продукта.
Делим тесты по приоритету и формируем их.

5. что мы должны сделать в рамках анализа? то есть что будет на выходе нашего анализа?
 -Понять, что в нашем продукте есть (карта-функционала или mind map)
 -Выделить взаимосвязи моделей продукта. Что проиходит в модуле и как это влияет на другие.
 -Вести историю ошибок и исходя из неё оценить риск возникновения новых
 -Вести приоретизацию функционала (учёт того, что нужно пользователям в первую очередь)
 -Критичность потенциальных обшибок.(Что чаще ломается и что важнее всего для пользователя)

6. зачем расставлять приоритеты? от чего зависит приоритет функциональности? на основании чего можно определить приоритет функциональности?
Приорететы можно рассмотреть с точки зрения пользователя и с точки зрения рисков. Т.е. если есть какой-то функционал вам не важен и пользователю он не нужен, то его можно отодвинуть на "второй план". Также есть зависимость приоритета от количества в конкретном функционале ошибок, от того без чего пользователь сможет обойтись, от взаимосвязей в продукте, от внешних условий.

7. какие бывают внещние факторы, которые могут повлиять на тестирование? зачем учитывать внешние факторы?
1.Длительность итераций тестирования. (время тестирования)
2.Регулярность публичных релизов.
3.Ограничения по времени на тестирование.
4.Допустимость и недопустимость ошибок.
5.Возможности автоматизации тестирования.

Внешние факторы нужно учитывать для того, чтобы максимально эффективно протестировать продукт и при этом укладываться в сроки сдачи релиза, экономить на ресурсах при возможности автоматицации и учитывать дальнейшее построение продукта на основе потребностей пользователя.

8. охаректеризуйте разные комплекты тестов (зачем? как выбрать тесты в комплект? как часто прогонять? в чем задача каждого набора? нужно проводить для одной сборки или можно на нескольких? и тд): BVT, UAT, FTP? какие интересные особенности для каждого комплекта вы запомнили?
 
BVT. (build verification test)
Нужен чтобы быстро оценить качество ПО.
Сразу найти критические ошибки.
1-й кандидат на автоматизацию.
Согласование с командой по тестированию.

FTP. (full test path)
Все возможные и не возможные тесты. Чаще всего используется при тестировании нового/обновлённоо продукта.
Фиксировать тесты не нужно. Все тесты пройти не возможно в любом случае, поэтому можно отследить процент готовности продукта и использовать его в качестве агрументов для расширения ресурсов. Автоматизируем наиболее важные тесты.

UAT. (use acceptance test)
Иногда тесты предоставляются пользователю, который их проходит.
Цель: Определить готовность к релизу продукта. 
С помощью этих тестов можем объявить о степени готовности продукта к релизу.
Проверять важно в рамках одной сборки, иначе не получим понимания того, что в этой сборке работает.

9. что делать, если пропустили баг в релиз

1.Проанализировать причину пропуска.
2.Выяснить насколько баг критичен.
3.Понять какой из наборов тестов расширять.
4.Выяснить что ещё могли пропустить.
5.Улучшать процесс тестирования, получать опыт от этой ошибки.
