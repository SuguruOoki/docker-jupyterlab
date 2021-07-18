FROM jupyter/datascience-notebook

USER root

# GoogleAnalyticsClient のインストール
RUN pip install --upgrade google-api-python-client redash-dynamic-query ipython-sql jupytext jupyterlab_vim


# Redash用のプラグイン https://github.com/MasamichiIdeue/redquery
RUN pip install git+https://github.com/MasamichiIdeue/redquery.git

# 黒背景設定を追加
RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension
RUN echo '{"theme":"JupyterLab Dark"}' > \
	/home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

RUN echo 'c.ContentsManager.default_jupytext_formats = "ipynb,py"' >> \
	/home/jovyan/.jupyter/jupyter_notebook_config.py

RUN mkdir /home/jovyan/notebooks
RUN chown jovyan:users /home/jovyan/notebooks

USER jovyan
WORKDIR /home/jovyan