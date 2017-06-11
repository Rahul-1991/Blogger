from datetime import datetime
from collections import OrderedDict


# Used to make the BlogDataStructure class as a singleton

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Data Structure Format
'''
{
    '1': {'content': 'This is a post', 
            'published_time_diff': 'published 0 secs ago', 
            'pk': 1, 
            'created_at': datetime.datetime(2017, 6, 11, 6, 14, 17, 767177), 
            'upvote_count': 1, 
            'updated_at': datetime.datetime(2017, 6, 11, 6, 14, 21, 417014), 
            'downvote_count': 0},
    
    '2': {'content': 'This is another post', 
            'pk': 2, 
            'created_at': datetime.datetime(2017, 6, 11, 6, 14, 30, 70538), 
            'upvote_count': 0, 
            'updated_at': datetime.datetime(2017, 6, 11, 6, 14, 30, 70550), 
            'downvote_count': 0}
}
'''





# Main Data structure which provides the CRUD operations

class BlogDataStructure(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.blog_dict = dict()

    @staticmethod
    def _current_time():
        return datetime.now()

    # used as an auto increment for generating the key for data structure which acts as primary key
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

    # sort the dictionary by upvotes_count in descending order
    def get_sorted_keys(self):
        return sorted(self.blog_dict.keys(),
                             key=lambda x: self.blog_dict.get(x, {}).get('upvote_count', 0), reverse=True)[:20]

    # convert to Ordered Dict
    def get_sorted_dict(self, sorted_keys):
        sorted_dict = OrderedDict()
        for key in sorted_keys:
            sorted_dict[key] = self.blog_dict.get(key)
        return sorted_dict

    # generate dict sorted by upvotes to display top 20 posts
    def get_list(self):
        sorted_keys = self.get_sorted_keys()
        return self.get_sorted_dict(sorted_keys)
