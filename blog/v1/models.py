from datetime import datetime


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BlogDataStructure(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.blog_dict = dict()

    @staticmethod
    def _current_time():
        return datetime.now()

    def get_primary_key(self):
        if self.blog_dict:
            return max(self.blog_dict.keys()) + 1
        else:
            return 1

    def create(self, data):
        pk = self.get_primary_key()
        data.update({
            'created_at': self._current_time(),
            'updated_at': self._current_time(),
            'pk': pk,
            'upvote_count': 0,
            'downvote_count': 0,
        })
        self.blog_dict[pk] = data

    def update(self, pk, data):
        data.update({'updated_at': self._current_time()})
        self.blog_dict[pk].update(data)

    def delete(self, pk):
        del self.blog_dict[pk]

    def read(self, pk):
        return self.blog_dict[pk]

    def get_list(self):
        return self.blog_dict
