# Открытый Церковный календарь

Проект по автоматическому составлению календаря церковных праздников 
в форматах электронных книг (ePub, PDF, AZW) и документов.

# Установка
```shell
pip install -r requirements.txt
```
Установка Pandoc и Xelatex для Ubuntu, необходимых для конвертации форматов.
```shell
sudo apt-get install pandoc texlive-xetex
```
Загрузка источников и их конвертация в HTML.
```shell
./scripts/source_books_download.sh
./scripts/source_books_convert.sh
```
Извлечение текстов, преоброзвание его в XML 
и распределения его по датам в папке `output_data/xml`.
```shell
python3 main.py --parse-sources
```
Создание исходного текста календаря в формате Markdown в папке `output_data/markdown`.
```shell
python3 main.py
```
Создание книг в формате ePub (`output_data/epub`), 
для Kindle в AZW (`output_data/azw`) и PDF (`output_data/pdf`).
```shell
./scripts/md2epub.sh
./scripts/epub2azw.sh
./scripts/md2pdf.sh
```


## Источники

* [Жития святых по изложению свт. Димитрия Ростовского](https://ru.wikisource.org/wiki/%D0%96%D0%B8%D1%82%D0%B8%D1%8F_%D1%81%D0%B2%D1%8F%D1%82%D1%8B%D1%85_%D0%BF%D0%BE_%D0%B8%D0%B7%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8E_%D1%81%D0%B2%D1%82._%D0%94%D0%B8%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D1%8F_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE)