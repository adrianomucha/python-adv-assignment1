'''Extend the python dict class to enable accessing item by attribute.
    exapmle:
        your_dict = YourDict()
        your dict['a'] = 1
        print your_dict.a
        your_dict.b = 2
        print your_dict ['b']

       '''

class YourDict(dict):

    def __setattr__(self,attr,value):
        self[attr] = value

    def __getattr__(self, attr):
        return self.get(attr)

