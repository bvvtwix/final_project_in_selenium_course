# final_project_in_selenium_course

ООП: 
https://stepik.org/lesson/24461/step/1?unit=6767
https://tproger.ru/translations/oop-principles-cheatsheet/
Code Style:
https://docs.python-guide.org/writing/style/
https://www.python.org/dev/peps/pep-0008/
https://habr.com/ru/post/266969/
https://habr.com/ru/post/206868/
https://pep8.ru/doc/pep8/
https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html
POM: 
https://page-objects.readthedocs.io
https://selenium-python.readthedocs.io/page-objects.html
https://github.com/SeleniumHQ/selenium/wiki/PageObjects
https://martinfowler.com/bliki/PageObject.html
https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b
Исключения: 
http://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html 
Splinter: 
Документация: https://splinter.readthedocs.io/en/latest/index.html
Код: https://github.com/cobrateam/splinter
Код и документация pytest-splinter: https://github.com/pytest-dev/pytest-splinter
Selene:
Документация: https://selene-docs-test.readthedocs.io/en/latest/introduction.html
Код: https://github.com/yashaka/selene
Презентация: https://www.youtube.com/watch?v=BzfOeHJrguQ
PyPOM:
Документация: https://pypom.readthedocs.io/en/latest/
Код: https://github.com/mozilla/PyPOM
Webium: 
Документация: http://wgnet.github.io/webium/
Код: https://github.com/wgnet/webium
Презентация: https://www.youtube.com/watch?v=XrL1BLgkKyA

Для дальнейшего развития в роли тестировщика-автоматизатора вам понадобится изучить следующие важные темы:

Запуск тестов на удаленных серверах с помощью Selenium Grid, Selenoid или других подобных инструментов. Это позволит организовать автоматический запуск тестов, ускорение прогона тестов, а также организовать кросс-браузерное и кросс-платформенное тестирование. 
Базовые знания технологии Docker для управления контейнерами с браузерами на удаленных серверах. Например, существуют готовые контейнеры, которые можно использовать в Selenium Grid: https://hub.docker.com/u/selenium.
Настройка Continious Integration сервера для построения процесса непрерывной интеграции. Тесты должны запускаться автоматически по расписанию или на каждый коммит.
Настройка отчетов по результатам прогона тестов с детальной информацией об ошибках, что позволяет быстрее локализовать найденные автотестами баги. Вы можете использовать плагин pytest-html для PyTest или фреймворк Allure.
Генерация скриншотов и видео в случае падения тестов для упрощения анализа и воспроизведения проблемы. Некоторые инструменты уже поддерживают данную возможность, например, pytest-splinter.
Подготовка тестовых данных с помощью запросов к базе данных или с помощью API.