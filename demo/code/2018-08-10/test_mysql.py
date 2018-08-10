from multiprocessing import pool
import dataset


def test(_):
    db = dataset.connect('mysql://testuser:abc123456@localhost/testdb')
    for id in range(1000000):
        db['foo'].insert(dict(name='lsl{}'.format(id), num=id))


p = pool.Pool(16)

p.map(test, range(16))
