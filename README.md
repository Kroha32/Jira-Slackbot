# Alfabot

![Картиночка](https://github.com/Kroha32/Jira-Slackbot/blob/master/images/Смайл2.png "Аватар")

[схема]:https://gitlab-test.alfastrah.ru/rosnou/jirabot/raw/master/images/bot_Vlad_.png
Это бот "alfabot" для удобного информирования альфанаселения в Slack'е.

#### Содержание

+  [Что это за бот?](#что-это?)
+  [А что он умеет?](#что-умеет)
+  [Что надо, чтобы использовать его?](#что-нужно-для-того-чтобы-начать-пользоваться-alfabot)
+  [Помощь.](#инструкции)
+  [Документы.](#документы)
+  [Лицензия.](#лицензия)

#### Что это?

Бот "alfabot" позволяет, не выходя из Slack'а, проверить назначенные Вам задачи, написать или посмотреть комментарии в Jira.

![схема2](https://github.com/Kroha32/Jira-Slackbot/blob/master/images/bot2(Vlad).png "Схема2")

#### Что умеет?

Бот знает команды:
* __help__ - выводит список всех доступных команд.
* __my_tasks__ - выводит все назначенные Вам задачи в Jira в виде [jirakey] задачи, её [описание] и ссылки на каждую.
* __comment _issue-00 Example message___ -  пишет коммент [message] в обозначенной задаче [jirakey].
* __my_email__ - выводит вашу почту под которой вы залогинились.
* __show_comments _issue-00___ - показывает все текущие комментарии к указанной задаче.
* __get_api__ -
* __library__ - даёт ссылку на страницу в confluence с библиотекой ДИТ и полезными книгами.
* __strategy__ - даёт ссылку на страницу в confluence "ДИТ дом".
* __agile__ - ссылка на базовый тренинг по Scrum для членов команды разработчиков
* __customize__ -

![схема1](https://github.com/Kroha32/Jira-Slackbot/blob/master/images/bot(Vlad).png "Схема1")

#### Что нужно для того чтобы начать пользоваться "alfabot"

1. В клиенте Slack выбрать или создать нужный вам канал.
2. Открыть окно "__Details__" в правом верхнем углу.
3. Выбрать "__More__" далее "__Add apps__"
4. В открывшемся окне поиска приложений ввести название "alfabot" и нажать кнопку "__Add__"
5. Увидеть в чате сообщение о том, что бот добавлен, и попробовать ввести тестовую команду "@alfabot help", ответ вы должны получить в комментариях к своему сообщению

### Инструкции
#### Инструкция по командам бота

Данная [схема] лучше всего визуально описывает работу бота с командами.

Из неё видно, что каждый запрос должен начинаться с обращения к боту "@alfabot", далее ключ команды, которую нужно исполнить, если это команда которая состоит из нескольких ключей, такая как "_comment_" то в ней первым ключом будет само слово "__comment__", далее вам нужно указать ключ задачи "__issue-00__", которую вы хотите закомментировать, далее пишите текст комментария (все ключи разделяются "_Пробелом_")

#### Инструкция как создать бота в Slack

* Нужно открыть окно приложения Slack (можно и в браузере)
* Выбрать в левом верхнем углу функцию "__Apps__"
* В появившемся окне приложений ввести в поиск "Bots" и выбрать приложение "__Bots__" и кликнуть кнопку "__Add__"
* Вас перебросит в браузер с этим приложением, там нужно будет вновь нажать "__Add to Slack__"
* Далее вам предложат выбрать имя своему боту (в дальнейшем его можно будет изменить), вводим его и жмём "__Add bot integration__"
* Вас перенесло в окно настройки бота, где вы можете изменить имя бота, аватарку и т.п., но самое главное вам будет выдан "__API token__" через этот токен вы и будете далее подключать бота к чему-либо, токен следует тщательно хранить и никому не говорить, в противном случае завладев вашим токеном, завладеют и ботом.
* Жмём "__Save Integration__"
* Вуаля, ваш бот создан, а как его подключать вы можете посмотреть выше в инструкции по подключению "alfabot"

#### Инструкция для разработчиков по настройке бота

Здесь мы кратко расскажем вам что следует изменить в коде, чтобы например добавить новые фичи.

Для логина бота на какой-либо сервис (как например Jira), лучше использовать аккаунт какого-либо из админов или создать админа-бота и соответственно в коде написать его логин и пароль, вместо localhost.com - указать адрес вашей рабочей области.

    <data2 = {"os_username":"admin", "os_password":"admin"}
     url2 = "https://localhost.com/login.jsp">

Здесь вам нужно указать токен вашего бота в Slack (созданного ранее)

    <slack_token ="xoxb-******...">

Для того чтобы добавить новую команду, вам нужно найти этот фрагмент кода и написать её название:
![схема1](https://github.com/Kroha32/Jira-Slackbot/blob/master/images/объяснение.png "Одно словные команды")

Далее вы создаёте функцию для вашей новой команды (посредством нового _if_), если она однословная:
![схема1](https://github.com/Kroha32/Jira-Slackbot/blob/master/images/одно.png "Описание")

И здесь если состоит из нескольких ключей:
![схема1](https://github.com/Kroha32/Jira-Slackbot/blob/master/images/два.png "Схема1")


#### ___Благодарности___

_Спасибо Исанину Антону за терпение, понимание и поддержку и Северцеву Андрею за предоставленную возможность._

[Можно вернуться к содержанию](#содержание)
