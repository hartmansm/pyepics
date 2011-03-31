import sys
from epics import caget

import instrument

db = instrument.InstrumentDB('Test.einst')

pvlist = ['13XRM:m1.VAL','13XRM:m2.VAL','13XRM:m3.VAL']

iname = 'sample_stage'

inst = db.get_instrument(iname)
if inst is None:
    inst = db.add_instrument(iname, pvs=pvlist)

inst = db.get_instrument(iname)
print inst, inst.pvs
 
values = {}
for pv in pvlist:
    values[pv] = 0

db.save_position('Origin', inst, values)

values = {}
for pv in pvlist:
    values[pv] = caget(pv)

db.save_position('Current', inst, values)


print '====='
origin = db.get_position('Current')

print origin, origin.pvs
