Муратов Евгений
Тестовое задание: https://drive.google.com/file/d/1DU2-MSCNN-FzCa8ksB3rx2GQy23LSt5T/view

Проект состоит из сущностей города, улицы и магазины, обрабатываютсяя соответствующие запросы.
Из тз реализован весь функционал, кроме фильтраций для GET /shops/ Помимо прочего не удалось скрыть id при GET/shops/. 
Знаю, что нужно использовать slugrelatedfield.Но возникли трудности (ошибки) при использовании данного подхода

Подготовительные действия:
1) pip install Django, psycopg2, djangorestframework
2) sudo -u postgres psql
  CREATE DATABASE shops;
  CREATE USER shop_user WITH PASSWORD 'postgres';
  GRANT ALL PRIVILEGES ON DATABASE shops TO shop_user;
Запуск проекта:
В директории проекта выполнить комманду python3 manage.py runserver

О тестах:
Написад тесты для запросов GET /city/ и GET /street/, которые полность работают, а также тест для POST и GET /shops/, которые не приводятся в нужную форму,
но по сути верны.

Рассчитываю на обратную связь с ревью данного проекта!
