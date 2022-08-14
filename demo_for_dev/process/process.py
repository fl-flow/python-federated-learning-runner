import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from fl_component.processing import Process, StreamRet

from demo_for_dev.process.foo import foo, foo1


p = Process(
    target=foo,
    memory=1,
    objs=['arg1', 'arg2'],
    stream=['aaa', 'bbb']
)
r = p.run()
for i in r:
    if isinstance(i, StreamRet):
        print('strem')
        for j in i:
            print(j)
        continue
    print('obj')
    print(i)


print('\n\n\n\n\n\n\n')


p = Process(
    target=foo1,
    memory=1,
    objs=['arg1', 'arg2'],
    stream=['aaa', 'bbb']
)
r = p.run()
for i in r:
    if isinstance(i, StreamRet):
        print('strem')
        for j in i:
            print(j)
        continue
    print('obj')
    print(i)
