# hw_01_task1

Проект в рамках домашнего задания #1, задача #1 по курсу Data Scientist.

## Постановка задачи:
  1. Выбрать источник данных.
  2. Собрать данные и сохранить их локально.
  3. Преобразовать данные в табличный вид и сохранить в формате csv.
  4. Используя pandas посчитать статистики и вывести информацию о данных.


В качестве источника данных было выбрано API от https://data.police.uk,
позволяющее получить сводку по преступлениям в указанной области Англии за выбранный месяц.
Были загружены данные по преступлениям в городе Leicester за июль 2018 года.

## Описание параметров запуска:

Для сбора данных и сохранения полученного JSON в локальный txt файл:

  `python -m gathering gather`

Для сохранения полученных данных в csv файл:

  `python -m gathering transform`

Для вывода информации по загруженным данным:

  `python -m gathering stats`

Последней командой будет выведено:

"Date" - рассматриваемый период (в формате YYYY-MM)

"Total Crimes" - сколько всего преступлений попало в выборку

"Crimes by category" - список преступлений по категориям отсортированный по количеству

"Status on "Bicycle theft" crimes" - статистика статусов по преступлениям о воровстве велосипедов
