FROM python:3.8-slim

# PROJECT_ROOT - путь до каталога внутри контейнера, в который будет
# копироваться приложение
ENV PROJECT_ROOT=/application

# Путь до исходников
ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

# Путь до библиотек и скриптов
ENV PATH=$PATH:$PROJECT_ROOT/scripts/

# Обновление пакетов в системе
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip poetry

# пакеты, которые необходимы для работы в runtime
# ENV RUNTIME_PACKAGES \
#     gettext \
#     git

# Пакеты, которые необходимы для установки зависимостей.
# Не останутся в итоговом образе.
ENV BUILD_PACKAGES \
    npm

COPY pyproject.toml poetry.lock $PROJECT_ROOT/
COPY frontend/package.json frontend/package-lock.json $PROJECT_ROOT/frontend/

# # Создание директорий
# RUN mkdir -p $PROJECT_ROOT/static && \
#     mkdir $PROJECT_ROOT/media && \
#     mkdir $PROJECT_ROOT/courses

WORKDIR $PROJECT_ROOT

# Запускаем установку зависимостей одной командой, чтобы облегчить образ
RUN set -ex && \
    # Установка зависимостей apt
    apt-get install $BUILD_PACKAGES --no-install-recommends -y && \
    # Установка зависимостей через poetry
    poetry install --no-root --no-dev -n && \
    # Установка зависимостей через npm и сборка фронтенда
    cd fronend && npm install --no-audit && npm build && \
    # Чистим кеш
    npm cache clean --force && \
    apt-get autoremove $BUILD_PACKAGES -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD ./ $PROJECT_ROOT

# Service scripts
RUN for i in $PROJECT_ROOT/scripts/*; do \
    sed -i 's/\r//' $i; \
    chmod +x $i; \
    done

EXPOSE 8000

CMD start_gunicorn