# zeltir
Автоматизация инвентаризации игрушек и переделывании отчёта из прекрасной таблицы в ужасный формат, нужный моему начальнику на тот момент


# В общем то почему зачем и что это
История началась просто - я устроился по знакомым по низшей ставке в тир с пневматикой и посредственного качества игрушками. Всё шло неплохо до одного момента: До пересчёта.
Пересчёт мы скидывали в самом что худшем варианте из всех возможных - сообщением в телеграмме и смотреть на это было больно.

Оно даже не вмещается на один экран:

![Вот С ЭТИМ нужно было иметь дело](https://i.imgur.com/8AKTfID.png)

Этот отчёт сделал человек вручную, можно увидеть что некоторые числа там просто пропущенны, часто можно встретить ошибки в подсчёте суммы и всё остальное что зависит от человеческого фактора.

# Как исправлять решил

Заносить значения в сообщение по одному - мерзко и неприятно, так что у нас есть отличный вариант - таблица. Я создал таблицу в google sheets и дал доступ туда каждому.
Дальше создал сервисный аккаунт чтоб собирать информацию оттуда, таким образом я переношу её уже на сервер в формате json и могу наконец то нормально оперировать хоть чем то.

![Крассивая таблица](https://imgur.com/nsJOG1M.png)

Перевод в формат страха ужаса и начальника репера производится через телеграмм бота, для удобства в пересылка сообщения, никто даже не заподозрил ничего пока я прямо об этом не сказал начальнику
![фу](https://imgur.com/p0Rrcw6.png)

# Настройка

Все настройки хранятся в отдельном файле config.py, там всё что нужно менять для подключения предположим другой точки
