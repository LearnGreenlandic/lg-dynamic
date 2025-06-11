#!/usr/bin/env python3
import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
sys.path.append(dir + '/../../_lib')
from shared import *
import shared as S


subprocess.run(['rm', '-f', f'{S.name}.sqlite.new'])
subprocess.run(['sqlite3', f'{S.name}.sqlite.new', '-init', f'{S.dir}/schema.sql'], input='', stdout=subprocess.PIPE)
con = sqlite3.connect(f'{S.name}.sqlite.new')
db = con.cursor()
for n in [1, 2, 3, 4, 5, 6, 7, 8]:
	db.execute(f"ATTACH DATABASE '8-1-{n}x.sqlite' AS part")
	db.execute("INSERT INTO qs SELECT * FROM part.qs")
	con.commit()
	db.execute(f"DETACH DATABASE part")
con.commit()

db.execute("VACUUM")
con.commit()
con.close()

os.rename(f'{S.name}.sqlite.new', f'{S.name}.sqlite')
