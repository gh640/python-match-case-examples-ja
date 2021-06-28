# `3.10` は未リリースなので `3.10-rc-buster` を使う
FROM python:3.10-rc-buster

RUN python -m pip install pytest

CMD ["pytest", "-v"]
