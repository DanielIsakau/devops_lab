import json
import os
import sys
import yaml


class Inform(object):
    a = sys.version.split()[0]
    b = sys.path[3]
    c = os.environ['VIRTUAL_ENV']
    d = sys.executable
    e = os.popen('which pip').read().strip()
    f = os.popen('echo $python_path').read().strip()
    g = sys.path[-1]

    @staticmethod
    def last():
        tmp = os.popen('pip freeze').read().strip().split()
        h = {}
        for i in tmp:
            key, value = i.split("==")[0], i.split("==")[1]
            h[key] = value
        return h


obj = Inform()
parameters = {
    "version": obj.a,
    "name (alias)": obj.b,
    "virtual environment": obj.c,
    "python exe_loc": obj.d,
    "pip location": obj.e,
    "python_path": obj.f,
    "site-packages location": obj.g,
    "installed packages": obj.last()}
with open('PY_meters.json', "w") as infile:
    infile.write(json.dumps(parameters))
with open('PY_meters.yml', 'w') as infile2:
    yaml.dump(parameters, infile2, default_flow_style=False)
