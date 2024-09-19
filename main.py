import matplotlib.pyplot as plt
import numpy as np
from Methods import Methods

a = Methods()

b1 = a.first_method()
y_t1, x_t1, t = b1[0], b1[1], b1[3]
b2 = a.second_method()
y_t2, x_t2, t = b2[0], b2[1], b2[3]
b3 = a.third_method()
y_t3, x_t3, t = b3[0], b3[1], b3[3]
b4 = a.fourth_method()
y_t4, x_t4, t = b4[0], b4[1], b4[3]

# Создание окна
fig, ax = plt.subplots(2, 4, figsize=(12, 6.2))
plt.setp(ax, xlim=(0, b1[2]), ylim=(-4, 4))

# Метод 1
ax[1, 0].axis(xmin=min(x_t1)-0.2,xmax=max(x_t1)+0.2)
ax[1, 0].axis(ymin=min(y_t1)-0.02,ymax=max(y_t1)+0.02)
ax[1, 0].plot(x_t1, y_t1, label="y(z)")
ax[1, 0].set_title("explicit Euler scheme")

ax[0, 0].plot(t, x_t1, label="z(t)")
ax[0, 0].plot(t, y_t1, label="y(t)")
ax[0, 0].set_title("explicit Euler scheme")

# Метод 2
ax[1, 1].axis(xmin=min(x_t2)-0.2,xmax=max(x_t2)+0.2)
ax[1, 1].axis(ymin=min(y_t2)-0.02,ymax=max(y_t2)+0.02)
ax[1, 1].plot(x_t2, y_t2, label="y(z)")
ax[1, 1].set_title("implicit Euler scheme")

ax[0, 1].plot(t, x_t2, label="z(t)")
ax[0, 1].plot(t, y_t2, label="y(t)")
ax[0, 1].set_title("implicit Euler scheme")

# Метод 3
ax[1, 2].axis(xmin=min(x_t3)-0.2,xmax=max(x_t3)+0.2)
ax[1, 2].axis(ymin=min(y_t3)-0.02,ymax=max(y_t3)+0.02)
ax[1, 2].plot(x_t3, y_t3, label="y(z)")
ax[1, 2].set_title("Runge-Kutta method (2 order)")

ax[0, 2].plot(t, x_t3, label="z(t)")
ax[0, 2].plot(t, y_t3, label="y(t)")
ax[0, 2].set_title("Runge-Kutta method (2 order)")

# Метод 4
ax[1, 3].axis(xmin=min(x_t4)-0.2,xmax=max(x_t4)+0.2)
ax[1, 3].axis(ymin=min(y_t4)-0.02,ymax=max(y_t4)+0.02)
ax[1, 3].plot(x_t4, y_t4, label="y(z)")
ax[1, 3].set_title("Runge-Kutta method (4 order)")

ax[0, 3].plot(t, x_t4, label="z(t)")
ax[0, 3].plot(t, y_t4, label="y(t)")
ax[0, 3].set_title("Runge-Kutta method (4 order)")

for ax in ax.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
fig.tight_layout()
plt.show()