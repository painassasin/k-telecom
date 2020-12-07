# Тестовое задание (K-Telecom)
## Описание
Приложение позволяет добавлять серийные номера для определенного типа оборудования.
Для этого необходимо из выпадающего списка выбрать тип оборудования, в поле `textarea`
ввести один или несколько номеров (каждый номер на отдельной строке) 
и нажать кнопку `Добавить`.  
Если все номера соответствуют маске, серийные номера будут добавлены в базу.
В противном случае приложение сообщит об ошибке.

# Инструменты
- Python 3.8
- MariaDB
- Docker + docker-compose

## Инструкция по запуску
**Установка Docker + docker-compose**
> [ Инструкция](https://docs.docker.com/engine/install/)

**Сборка контейнеров**
```bash
$ docker-compose build 
```
**Запуск**
```bash
$ docker-compose up
```
**Удаление контейнера и образа**
```bash
$ docker-compose down -v --rmi local
```