# Init PostgreSQL

## Запустить в Docker

1. **Проверить установку Docker** (если ещё не установлено):

   ```bash
   docker --version
   ```

2. **Запустить контейнер PostgreSQL**:

   ```bash
   docker run -d \
     --name my_postgres \
     -e POSTGRES_USER=appuser \
     -e POSTGRES_PASSWORD=secret \
     -e POSTGRES_DB=appdb \
     -p 5432:5432 \
     postgres:latest
   ```

   * `-d` — запуск в фоне
   * `--name my_postgres` — имя контейнера
   * `-e ...` — переменные окружения для пользователя, пароля и базы
   * `-p 5432:5432` — проброс порта локально

3. **Проверка статуса**:

   ```bash
   docker ps | grep my_postgres
   ```


## Получить DSN

1. **Формат DSN**:

   ```text
   postgres://<user>:<password>@<host>:<port>/<database>?sslmode=disable
   ```

2. **Пример экспорта переменной**:

   ```bash
   export DATABASE_URL="postgres://appuser:secret@localhost:5432/appdb?sslmode=disable"
   ```

3. **Проверка подключения из Go**:

   ```go
   import (
     "database/sql"
     _ "github.com/lib/pq"
   )

   func main() {
     dsn := os.Getenv("DATABASE_URL")
     db, err := sql.Open("postgres", dsn)
     if err != nil {
       log.Fatal(err)
     }
     defer db.Close()
     // тестовый запрос
     if err := db.Ping(); err != nil {
       log.Fatal(err)
     }
     fmt.Println("Connected to Postgres!")
   }
   ```
