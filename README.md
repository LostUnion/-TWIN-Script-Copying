<h1>COPYING SCRIPT</h1>

<b>Данная программа позволяет производить привычное копирование намного быстрее и с минимальным участием пользователя, буквально, одной командой.</b>

<h3>Запуск программы</h3>

Запускается программа из командной строки следующей командой с указанием аргументов:
```
py run.py -s [script] -c [cabinet]
```
При первом запуске программы, будет создана локальная база данных, а также будет запрошен логин и пароль от личного кабинета.
После ввода валидных логина и пароля, программа продолжит свое выполнение.


<span><b>Обратите внимание!</b></span> При возникновении сбоя в сохранении сценария, требуется ручное сохранение с ожиданием информационного окна с подтверждением успешной операции. После этого программа продолжит свою работу.

***После успешного завершения работы программы, в консоли появится готовый шаблонный скрипт, который мы сможем отправить в сообщении клиенту.***

---

<h3>Установка зависимостей</h3>

Для работы программы необходимо иметь установленный Python 3.12, а так же пакетный менеджер pip.

Скачать и установить Python можно с официального сайта.

<a href="https://www.python.org/downloads/"><img src="https://www.python.org/static/img/python-logo.png" alt="Описание изображения" style="width: 200px;"></a>

Файл get_pip.py уже находится в папке с программой.
Установить pip можно следующей командой.
```python
python get_pip.py
```

Последним шагом подготовки программы к работе будет установка зависимостей из файла requirements.txt
```
pip install -r requirements.txt
```
<h4>✅ Программа готова к работе.</h4>

---

<div align="center">

Libraries in this project
[![Python](https://img.shields.io/badge/Python-3.12-brightgreen?logo=python&color=orange)](https://www.python.org/downloads/) [![Requests](https://img.shields.io/badge/Requests-2.31-brightgreen?logo=Requests&color=green)](https://requests.readthedocs.io/en/latest/) [![Selenium](https://img.shields.io/badge/Selenium-4.15-brightgreen?logo=selenium&color=green
)](https://www.selenium.dev/)

<i>Version 1.0.0 | Release Date: November 15, 2023</i>
</div>