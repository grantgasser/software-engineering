import platform

import mymodule as mm
from mymodule import Motorcyle

mm.hello('world')

print(mm.car['make'])

print('System:', platform.system())
print('Machine:', platform.machine())
print('Node:', platform.node())
print('Mac version:', platform.mac_ver())

mc = Motorcyle('Ducati', 'Italiano', '2020', 500)
print(mc)