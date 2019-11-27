# ! /usr/bin/env python
# coding=utf8
'''
处理脚本中的缓存数据
'''
import functools
import re


class Cache(dict):

    def __new__(cls,*args):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Cache,cls).__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls):
        if not hasattr(cls,'_instance'):
            cls._instance = dict.__new__(cls)
        return cls._instance

    def get(self,name,default=None):
        """Multilevel get function.
        Code:
        Config().get('opt.opt_level2.key','default_value')
        """
        if not name:
            return default
        levels = name.split('.')

        data = self

        for level in levels:
            try:
                data = data[level]
            except:
                return default

        return data

    def set(self,name,value):
        """Multilevel set function
        Code:
        Config().set('opt.opt_level2.key','default_value')
        """
        levels = name.split('.')
        arr = self
        for name in levels[:-1]:
            if name not in arr:
                arr[name] = {}
            arr = arr[name]
        arr[levels[-1]] = value

    def getset(self,name,value):
        """Get cache, if not exists set it and return set value
        Code:
        Config().getset('opt.opt_level2.key','default_value')
        """
        g = self.get(name)
        if not g:
            g = value
            self.set(name,g)
        return g

def scache(func):

    def wrapper(*args, **kwargs):

        cache = Cache.getInstance()
        fn = "scache." + func.__module__ + func.__class__.__name__ + \
             func.__name__ + str(args) + str(kwargs)
        val = cache.get(fn)
        if not val:
            res = func(*args, **kwargs)
            cache.set(fn,res)
            return res
        return val
    return wrapper


if __name__ == '__main__':
    # Initialize
    c = Cache({'data': {'example': 'example data'}})




    @scache
    def func1():
        return 'OK'
    func1()
    print(c)







