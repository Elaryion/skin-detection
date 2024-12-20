# Use the official Fedora base image
FROM debian:latest

RUN apt-get update && apt-get install -y curl

RUN curl --proto '=https' --tlsv1.2 -LsSf https://github.com/astral-sh/uv/releases/download/0.4.18/uv-installer.sh | sh && mv /root/.cargo/bin/uv /bin/uv
COPY ./pyproject.toml /serv/pyproject.toml
COPY ./uv.lock /serv/uv.lock

# WORKDIR /home/sun

# RUN mkdir -r /root/.cache/uv

# RUN --mount=type=bind,src=/home/sun/.cache/uv,dst=/root/.cache/uv

WORKDIR /serv

RUN ls /home
# RUN --mount=type=cache,src=~ ls /home/sun
# RUN --mount=type=cache,target=. uv sync -v
RUN uv sync -v
# RUN --mount=type=cache,target=/root/.cache/uv uv sync -v

COPY . /serv

EXPOSE 5000

CMD ["uv", "run", "src/serv.py"]

