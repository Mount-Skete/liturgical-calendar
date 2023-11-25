# Календарь Православных Праздников 2024

Проект по автоматическому составлению календаря православных праздников на любой год
в форматах электронных книг (ePub, PDF, AZW) и документов.

Последнюю версию Календаря Православных Праздников на 2024 год можно скачать из раздела [Releases](https://github.com/Mount-Skete/liturgical-calendar/releases).

Календарь составляется с помощью программы на Python, 
которая берет данные праздников в формате `xml` 
и составляет документы с праздниками на каждый месяц
в формате `Markdown`.

Затем данные из `Markdown` они конвертируются 
в форматы `epub3` и `pdf` с помощью [Pandoc](https://pandoc.org).

Используются данные из проекта [Православные Праздники в XML](https://github.com/Mount-Skete/orthodox-typikon-feasts-xml).

# Подготовка текстов

Проект разрабатывается на Python и требует установки зависимостей из файла `requirements.txt`.

```shell
pip install -r requirements.txt
```

Необходимо также наличие русского языкового пакета `language-pack-ru` в случае работы на Ubuntu.
```shell
sudo apt-get install language-pack-ru
```

Запуск программы и составление календаря в формате `Markdown` на указанный год.
Если параметр `-y 2024` не указан, то используется текущий год.
```shell
python3 book/src/main.py -y 2024
```

# Конвертация текстов в ePub, AZW3 и PDF.

## ePub 3

Для конвертации в `ePub3` используется [Pandoc](https://pandoc.org).

На Ubuntu этот пакет можно установить так.
```shell
sudo apt-get install pandoc
```

После этого создать книгу в формате `ePub3` можно с помощью скрипта.
Книга сохранится в папку `output_data/epub`.
```shell
./scripts/md2epub.sh
```

## AZW3

Для создания календаря для Kindle в формате AZW3 нужно дополнительно установить 
[Calibre](https://calibre-ebook.com/download_linux).

Для Ubuntu это можно сделать следующей командой, для других операционных систем по ссылке выше.
```shell
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
```

Затем, с помощью скрипта, можно конвертировать книгу из `ePub` в `AZW3`.
Книга сохранится в папку `output_data/azw`.
```shell
./scripts/epub2azw.sh
```

## PDF

Для создания календаря в формате PDF нужно установить дополнительно [TeX Live](https://tug.org/texlive/).

Для Ubuntu это можно сделать следующей командой.
```shell
sudo apt-get install texlive-xetex
```

Затем с помощью следующей команды можно создать `pdf` в папке `output/pdf`.
```shell
./scripts/md2pdf.sh
```

# План работы

* Планируется добавление перевода на церковно-славянский
* Улучшение форматирование текстов и устранение ошибок

# Лицензия

Проект доступен по лицензии [MIT](LICENSE).