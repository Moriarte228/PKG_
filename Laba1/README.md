▎Описание

Color Model Converter — это приложение на Python, которое позволяет конвертировать цвета между моделями RGB, CMYK и HSL. Приложение предоставляет простой интерфейс для работы с цветами и их преобразования.

▎Зависимости

Для работы приложения необходимы следующие зависимости:

- Python 3.6 или выше
- Библиотека Tkinter

▎Инструкция по сборке

1. Скачайте или клонируйте репозиторий:

   
   git clone https://github.com/Moriarte228/PKG_.git
   cd Laba1

2. Установите необходимые зависимости (в частности библиотеку Tkinter)

▎Изображения

Цвет, который соответствует данным параметрам текущей цветовой модели, показан в квадратной окне в центре. Плавно меняется цвет при использовании ползунков.

▎Функционал

В центре приложение располагается квадратное окно, которое отражает текущий цвет, заданный пользователем с помощью текущей цветовой модели. Узнать текущую цветовую модель можно по надписи над квадратом. При запуске по умолчанию стоит модель RGB.
Вверху над этой надписи располагаются кнопки, красная и синяя, которые позволяют переключаться на другую цветовую модель, указанную на кнопке. При смене цветовой модели надписи на кнопках меняются автоматически на те цветовые модели, которые отличаются от текущей. Конвертация происходит автоматически.
Внизу квадратного окна располагается весь нужный функционал для изменения параметров цвета для текущей цветовой модели. Зелёная кнопка "Choose Color" позволяет изменить цвет с помощью палитры. Ниже располагается поля для ввода значений параметров для данной цветовой модели, а также ползунки для плавного изменения цвета. Изменения цвета происходит без задержек, синхронно.


▎Пределы входных данных

- Для RGB: значения R, G и B должны находиться в диапазоне от 0 до 255, целочисленные.
- Для CMYK: значения C, M, Y и K должны находиться в диапазоне от 0 до 255, целочисленные.
- Для HSL: значение H должно быть в диапазоне от 0 до 360, целочисленные; S и L должны находиться в диапазоне от 0 до 100б целочисленные.

При попытке ввести некорректные значения приложение само исправит на ближайшее число, лежайшее в данном диапазоне

▎Как запустить и посмотреть тесты

1. Exe файл находится в папке dist. Также для запуска приложения используйте следующую команду:

   
   python app.py
   

2. Чтобы запустить тесты, убедитесь, что у вас установлены библиотеки для тестирования (например, unittest), и выполните команду:

   
   python -m unittest test_colors.py
   

Тесты проверяют корректность конвертации между цветовыми моделями и обеспечивают надежность приложения.

▎Заключение

ColorConverter — это удобный инструмент для работы с цветами. Надеемся, что данная документация поможет вам быстро начать работу с приложением и использовать его функционал на полную мощность!




