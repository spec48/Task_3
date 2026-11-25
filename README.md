## Задание 3: UI-тесты

### Кроссбраузерные автотесты в Google Chrome и Mozilla Firefox для проверки веб-приложения Stellar Burgers

### Реализованные сценарии

С помощью паттерна Page Object Model созданы UI-тесты на функциональность: `Восстановление пароля`, `Личный кабинет`,  
`Основной функционал`, `Раздел "Лента заказов"`.

Создан отчет в Allure-pytest

### Структура проекта

- `locators` - пакет, содержащий файлы с локаторами
- `page_objects` - пакет с классами Page Object
- `tests` - пакет с тестами
  - `test_ingredient_page.py` - файл, содержащий тесты окна с деталями ингредиента
  - `test_main_page.py` - файл, содержащий тесты главной страницы
  - `test_order_feed_page.py` - файл, содержащий тесты раздела "Лента заказов"
  - `test_password_recovery_page.py` - файл, содержащий тесты на восстановление пароля
  - `test_profile_page.py` - файл, содержащий тесты личного кабинета

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и запуск сервера Allure**

>  `$ pytest tests --alluredir=allure_results`  
>  `$ allure serve allure_results`
