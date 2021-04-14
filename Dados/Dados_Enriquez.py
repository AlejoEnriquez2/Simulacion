# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:54:34 2021

@author: alejo
"""
import numpy as np
import matplotlib.pyplot as plt
import random



list = [random.randint(1,6) + random.randint(1,6) for i in range(10)]
fig, ax = plt.subplots()
ax.set_xlabel("Suma de los dados")
ax.set_ylabel("Cantidad de ocurrencias")
ax.set_title("10 lanzamientos")
ax.hist(list, bins=11, rwidth=0.6)
fig.savefig('10.png')

list = [random.randint(1,6) + random.randint(1,6) for i in range(100)]
fig, ax = plt.subplots()
ax.set_xlabel("Suma de los dados")
ax.set_ylabel("Cantidad de ocurrencias")
ax.set_title("100 lanzamientos")
ax.hist(list, bins=11, rwidth=0.6)
fig.savefig('100.png')

list = [random.randint(1,6) + random.randint(1,6) for i in range(1000)]
fig, ax = plt.subplots()
ax.set_xlabel("Suma de los dados")
ax.set_ylabel("Cantidad de ocurrencias")
ax.set_title("1000 lanzamientos")
ax.hist(list, bins=11, rwidth=0.6)
fig.savefig('1000.png')

list = [random.randint(1,6) + random.randint(1,6) for i in range(10000)]
fig, ax = plt.subplots()
ax.set_xlabel("Suma de los dados")
ax.set_ylabel("Cantidad de ocurrencias")
ax.set_title("10000 lanzamientos")
ax.hist(list, bins=11, rwidth=0.6)
fig.savefig('10000.png')

list = [random.randint(1,6) + random.randint(1,6) for i in range(100000)]
fig, ax = plt.subplots()
ax.set_xlabel("Suma de los dados")
ax.set_ylabel("Cantidad de ocurrencias")
ax.set_title("100000 lanzamientos")
ax.hist(list, bins=11, rwidth=0.6)
fig.savefig('100000.png')

list = [random.randint(1,6) + random.randint(1,6) for i in range(1000000)]
fig, ax = plt.subplots()
ax.set_xlabel("Suma de los dados")
ax.set_ylabel("Cantidad de ocurrencias")
ax.set_title("1000000 lanzamientos")
ax.hist(list, bins=11, rwidth=0.6)
fig.savefig('1000000.png')