import json
import pickle
import hashlib
from pathlib import Path


协议 = {
    'pickle': [
        pickle.dumps,
        pickle.loads,
        'pkl',
    ],
    'json': [
        lambda x: json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf8'),
        json.loads,
        'json',
    ],
}


def disk_cache(path, protocol='pickle'):
    dump, load, ext = 协议[protocol]
    path = Path(path)
    if path.is_file():
        raise Exception('你不对劲')
    path.mkdir(parents=True, exist_ok=True)
    def q(func):
        name = func.__name__
        def 假func(*li, **d):
            i = [name, li, d]
            md5 = hashlib.md5(dump(i)).hexdigest()
            名字 = f'{name}_{md5}.{ext}'
            if (path/名字).is_file():
                with open(path/名字, 'rb') as f:
                    i, o = load(f.read())
                    return o
            else:
                o = func(*li, **d)
                s = dump([i, o])
                with open(path/名字, 'wb') as f:
                    f.write(s)
                return o
        return 假func
    return q
