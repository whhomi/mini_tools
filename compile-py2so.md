### compile by nuitka3
```shell
nuitka3 --module --include-module=<dir name> <dir>
```

### compile by python module compileall
```shell
python3 -m compileall -b <dir>
```

### compile by python setup.py file
``` shell
python3 setup.py bdist_wheel

### install
cd dist
pip3 install zrpc-1.0.1-py3-none-any.whl

#if error you should update your setuptools
pip3 install -U setuptools
```
