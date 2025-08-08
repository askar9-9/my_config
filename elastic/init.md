# Запуск Elasticsearch в Docker

Простой пошаговый гид по развёртыванию Elasticsearch в контейнере Docker для локальной разработки.

## 1. Создание Docker-сети

```bash
docker network create elastic
````

**Описание:** создаёт изолированную сеть `elastic` для взаимодействия контейнеров.


## 2. Загрузка образа Elasticsearch

```bash
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.1.1
```

**Описание:** скачивает официальный Docker-образ Elasticsearch версии 9.1.1.


## 3. Запуск контейнера Elasticsearch

```bash
docker run --name es01 --network elastic \
  -p 9200:9200 \
  -e discovery.type=single-node \
  -e xpack.security.enabled=false \
  -e xpack.security.http.ssl.enabled=false \
  -e network.host=0.0.0.0 \
  -m 1g \
  -d docker.elastic.co/elasticsearch/elasticsearch:9.1.1
```

**Описание параметров:**

* `--name es01` – имя контейнера.
* `--network elastic` – подключает контейнер к сети `elastic`.
* `-p 9200:9200` – перенаправляет порт 9200 контейнера на хост.
* `-e discovery.type=single-node` – запускает одиночный узел.
* `-e xpack.security.enabled=false` – отключает авторизацию.
* `-e xpack.security.http.ssl.enabled=false` – отключает HTTPS.
* `-e network.host=0.0.0.0` – позволяет принимать запросы со всех интерфейсов.
* `-m 1g` – выделяет контейнеру 1 ГБ оперативной памяти.
* `-d` – запускает контейнер в фоне.



## 4. Проверка подключения

```bash
curl http://localhost:9200 | jq .
```

**Описание:** выполняет HTTP-запрос к Elasticsearch и выводит отформатированный JSON.