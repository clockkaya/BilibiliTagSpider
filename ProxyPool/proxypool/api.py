from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    随机获取一个权值高的代理
    :return: 随机代理
    """
    conn = get_conn()
    return conn.get_random()


@app.route('/count')
def get_counts():
    """
    获取代理池的总数
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.get_count())


if __name__ == '__main__':
    app.run()
