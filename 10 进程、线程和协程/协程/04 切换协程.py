from urllib import request
import gevent
from gevent import monkey

monkey.patch_all()


def func(url):
    print('Get: %s' % url)
    response = request.urlopen(url)
    content = response.read().decode('utf8')
    print('%d bytes received from %s.' % (len(content), url))


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(func, 'https://www.birdpython.com/'),
        gevent.spawn(func, 'https://www.birdpython.com/columns/1/'),
        gevent.spawn(func, 'https://www.birdpython.com/video/')
    ])
