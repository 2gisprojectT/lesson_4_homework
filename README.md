# ProjectT 2015 v2 - Домашнее задание #4
## Задание 1.
Домашнее задание №2 уже выполнено ранее, полностью (оба задания), и ждет проверки и замечаний )))

## Задание 2.
#### Вопросы:
1. почему защита 1 уровня "что-нибудь потестировать" не работает?
   Потому что тестирование такого уровня проводится как бы наобум, без особого планирования, и есть риски протестировать не там и пропустить существенные серьезные ошибки.

2. почему не помогает просто написать больше тестов?
   Потому что на то, чтобы написать много тестов, нужно время и силы. И вполне возможно, что большинство тестов окажется ненужным или ненадежным. Может быть, пропущенных ошибок даже будет меньше, чем при подходе «протестировать что-нибудь», но все равно нет определенной уверенности в том, что все ошибки найдены.

3. зачем нужно анализировать?
   Затем, чтобы познакомиться с продуктом, его функционалом, прежде чем что-то предпринимать в тестировании. Когда хорошо знаешь продукт, его функции, особенности, архитектуру, взаимосвязи, то лучше представляешь, что требуется протестировать у продукта и как. И чтобы хорошо спланировать проверку продукта с наименьшими затратами времени, созданием и подбором наиболее продуктивных тестов. А хорошее планирование невозможно без анализа.

4. перечислите какие шаги нам нужноп выполнять, чтобы спроектировать хорошую защиту от багов? иными словами, опишите стратегию действий
   Чтобы спроектировать хорошую защиту от багов, необходимо:
   - проанализировать продукт, его функционал
   - определить риски, архитектуру, взаимосвязи, критичность
   - согласовать и учесть все потребности
   - определить цели тестов
   - распределить тесты, каждому тесту свое место и свое время
   - на основе всего этого разработать стратегию

5. что мы должны сделать в рамках анализа? то есть что будет на выходе нашего анализа?
   В рамках анализа мы должны:
   - декомпозировать продукт на объекты
   - сделать карту функционала и карту архитектуры (MindMup)
   - классифицировать риски возникновения
   - вести историю ошибок
   - определить приоритеты функционала
   - оценить критичность потенциальных ошибок

6. зачем расставлять приоритеты? от чего зависит приоритет функциональности? на основании чего можно определить приоритет функциональности?
   Приоритет – это порядок (очередность), в котором дефекты должны быть исправлены. Чем выше стоит приоритет, тем скорее нужно исправить дефект. Ресурсы времени ведь ограничены. Все проверить и исправить невозможно. Поэтому тестируются и исправляются в первую очередь самые серьезные дефекты. Приоритет функциональности зависит от ее востребованности, важности, срочности, взаимосвязей. На этих же основаниях и определяют приоритет функциональности.

7. какие бывают внещние факторы, которые могут повлиять на тестирование? зачем учитывать внешние факторы?
   Внешние факторы:
   - длительность итераций
   - регулярность публичных релизов
   - ограничения по времени тестирования
   - допустимость и недопустимость ошибок
   - возможность автоматизации
   Например, если есть такой внешний фактор, как ограничения по времени тестирования, то нужно определить, что будем тестировать, а что – нет. Какие тесты будем и не будем использовать, это тоже имеет значение. В общем, внешние факторы влияют на стратегию, поэтому чтобы продуктивно протестировать продукт, нужно учитывать вешние факторы.

8. охаректеризуйте разные комплекты тестов (зачем? как выбрать тесты в комплект? как часто прогонять? в чем задача каждого набора? нужно проводить для одной сборки или можно на нескольких? и тд): BVT, UAT, FTP? какие интересные особенности для каждого комплекта вы запомнили?
   Есть три вида комплектов:
   - BVT (Build Verification Test) – рассчитывается на то, чтобы как можно быстрее оценить качество продукта и найти наиболее критичные ошибки за очень короткое время (например за 2-4 часа, все зависит от сложности проекта). Для этого комплекта отбираются тесты для выявления важных и опасных дефектов (используется автоматизация, если есть такая возможность).
   - FTP (Full Test Path) – рассчитывается для полного тщательного тестирования продукта, для контроля и оценки его качества. В этот комплект включаются все возможные и невозможные тесты (даже в том случае, если не хватает ресурсов на их прохождение).
   - UAT (User Asseptance Test) – применяется для того, чтобы определить, готов ли продукт к релизу или нет. В этот комплект входят тесты, необходимые для успешного использования продукта пользователями, и которые укладываются в критерии сроков на критерии, а также допускается комбинаторика. Успешное применение UAT придает уверенность в продукте, в том, что продукт в ответственный момент не подведет, и тем самым помогает сохранить себе нервы, избежать предрелизной паники и стресса.

9. что делать, если пропустили баг в релиз
   В таком случае нужно проанализировать, почему пропустили баг. И насколько это было критично, во что это обошлось. Расширить первоначальный анализ, дополнить набор тестов недостающими тестами, чтобы в будущем не допустить больше таких промахов.

