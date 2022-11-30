import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
import numpy as np
import math


def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples


avg_h = []
avg_h.append(np.average(read("20mm.txt")))
avg_h.append(np.average(read("40mm.txt")))
avg_h.append(np.average(read("60mm.txt")))
avg_h.append(np.average(read("80mm.txt")))
avg_h.append(np.average(read("100mm.txt")))
avg_h.append(np.average(read("120mm.txt")))
v = [20, 40, 60, 80, 100, 120]
#h = [math.log10(x/1000) for x in h1]
fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

#ax.axis([math.log10(0.13), 0, 0, v.max()])s

ax.set_title('Зависимость сигнала АЦП от глубины жидкости')
ax.set_ylabel("Величина сигнала")
ax.set_xlabel("Глубина, мм")


#ax.scatter(h[0:5:100], v[0:5:100], marker = 's', c = 'green', s=10)


z = np.polyfit(v, avg_h, 4)
p = np.poly1d(z)

xp = np.linspace(20, 120, 100)
pyplot.plot(xp, p(xp), '-', c='red', label='S(t)')
ax.scatter(v, avg_h, c='black', linewidth=1)
ax.legend(shadow = False, loc = 'right', fontsize = 30)
pyplot.grid()
fig.savefig('graphic.png')
#fig.savefig('graphic.svg')


pyplot.show()