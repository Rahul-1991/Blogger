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

    def get_primary_key(self):
        if self.blog_dict:
            return max(self.blog_dict.keys()) + 1
        else:
            return 1

    def create(self, data):
        pk = self.get_primary_key()
        time_now = datetime.now().strftime("%Y-%m-%d")
        data.update({'created_at': time_now, 'pk': pk})
        self.blog_dict[pk] = data

    def update(self, pk, data):
        self.blog_dict.update({pk: data})

    def delete(self, pk):
        del self.blog_dict[pk]

    def read(self, pk):
        return self.blog_dict[pk]

    def get_list(self):
        return self.blog_dict
