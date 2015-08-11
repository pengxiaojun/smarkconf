# -*-coding: utf-8 -*-


import configparser


class ConfDict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(ConfDict, self).__init__(kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(r'ConfDict has no attribute %s', k)

    def __setattr__(self, k, v):
        self[k] = v


def toDict(d):
    cd = ConfDict()
    for k, v in d.items():
        cd[k] = toDict(v) if isinstance(v, dict) else v
    return cd


class SmartConf():
    def __init__(self):
        self.cd = ConfDict()
        self.cf = configparser.ConfigParser()

    def load(self, file):
        self.file_path = file
        self.cf = configparser.ConfigParser()
        self.cf.read(file)
        sections = self.cf.sections()
        for section in sections:
            sd = dict()
            options = self.cf.options(section)
            for option in options:
                sd[option] = self.cf.get(section, option)
                self.cd[section] = sd

        self.cd = toDict(self.cd)
        return self.cd

    def save(self, saveas=None):
        for k, v in self.cd.items():
            if not self.cf.has_section(k):
                self.cf.add_section(k)
            if isinstance(v, dict):
                for subk, subv in v.items():
                    self.cf.set(k, subk, subv)
                else:
                    pass  # no section
        # handle remove section
        sections = self.cf.sections()
        for section in sections:
            if section not in self.cd:
                self.cf.remove_section(section)
            else:
                options = self.cf.options(section)
                for option in options:
                    if option not in self.cd[section]:
                        self.cf.remove_option(section, option)

        with open(saveas if saveas else self.file_path, 'w') as f:
            self.cf.write(f)


if __name__ == '__main__':
    s = SmartConf()
    cd = s.load('a.ini')
    print(cd.hostconf.name)
    print(cd.baseconf.auth)
    cd.hostconf.name = 'ubuntu'
    cd.aa = dict()
    cd.aa['bb'] = 'cc'
    cd.aa['xx'] = 'yy'
    print('-'*20, cd)
    cd.foo = dict()
    cd.foo['foo'] = 'bar'
    cd.pop('foo')
    cd.aa.pop('xx')
    print(cd)
    s.save()
