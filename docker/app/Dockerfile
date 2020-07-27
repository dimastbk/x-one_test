FROM python:3.8-slim

# PROJECT_ROOT - путь до каталога внутри контейнера, в который будет
# копироваться приложение
ENV PROJECT_ROOT=/application

# Путь до исходников
ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

# Путь до библиотек и скриптов
ENV PATH=$PATH:$PROJECT_ROOT/docker/scripts/

# Отключаем DEBUG (для сборки Vue)
ENV ENVIRONMENT=production

# Пакеты, которые необходимы для работы в runtime
ENV RUNTIME_PACKAGES \
    nodejs \
    yarn

# Пакеты, которые необходимы для установки зависимостей.
# Не останутся в итоговом образе.
ENV BUILD_PACKAGES \
    curl \
    gnupg

COPY pyproject.toml poetry.lock $PROJECT_ROOT/
COPY frontend/package.json frontend/yarn.lock $PROJECT_ROOT/frontend/

WORKDIR $PROJECT_ROOT

# Запускаем установку зависимостей одной командой, чтобы облегчить образ
RUN set -ex && \
    # Обновление пакетов в системе
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install $BUILD_PACKAGES --no-install-recommends -y && \
    pip install --upgrade pip && \
    # Добавляем репозитории NodeJS и Yarn
    curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    echo "deb https://deb.nodesource.com/node_12.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    # Установка зависимостей apt
    apt-get install $RUNTIME_PACKAGES --no-install-recommends -y && \
    # Установка poetry
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
    export PATH=$PATH:$HOME/.poetry/bin && \
    # Отключаем создание виртуального окружения
    poetry config virtualenvs.create false && \
    # Установка зависимостей через poetry
    poetry install --no-root --no-dev -n && \
    # Чистим кеш
    apt-get autoremove $BUILD_PACKAGES -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD ./ $PROJECT_ROOT

# Установка зависимостей nodejs
RUN cd frontend && \
    yarn install && \
    # Сборка фронтенда
    yarn build && \
    # Чистим кеш
    yarn cache clean --force

# Service scripts
RUN for i in $PROJECT_ROOT/docker/scripts/*; do \
    sed -i 's/\r//' $i; \
    chmod +x $i; \
    done

EXPOSE 8000

CMD start_gunicorn