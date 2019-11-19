# docker-jupyterlab

## 前提環境

- Docker
- docker-compose

のインストールが必要。

### Mac

ターミナルにおいて以下のコマンドを実行

```
brew install docker
```
↑HomeBrewをインストールしていない場合は、その[インストール](https://brew.sh/index_ja)から。


### Windows

- [こちら](https://docs.docker.com/docker-for-windows/install/)からダウンロードし、インストーラーを使ってインストール。

↑手順については、以下を参考に進めること
https://ops.jig-saw.com/techblog/docker-for-windows-install/


## 使い方

```
git clone git@github.com:SuguruOoki/docker-jupyterlab.git
cd docker-jupyterlab
docker-compose up -d --build
```
