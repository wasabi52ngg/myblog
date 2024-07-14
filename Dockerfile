# Используем базовый образ Ubuntu
FROM ubuntu:22.04

# Устанавливаем временную зону, чтобы избежать интерактивного ввода
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Обновляем пакеты и устанавливаем необходимые зависимости для Python и Django
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv build-essential libpq-dev tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл требований в контейнер
COPY requirements.txt /app/

# Создаем и активируем виртуальное окружение и устанавливаем зависимости
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем содержимое проекта в контейнер
COPY . /app/

# Выполняем миграции базы данных
RUN ./venv/bin/python manage.py migrate

# Открываем порт, который будет использоваться приложением
EXPOSE 8000

# Команда для запуска сервера
CMD ["./venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
