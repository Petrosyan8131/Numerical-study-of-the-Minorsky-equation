import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# Инициализация списка для шага
tau_m = np.arange(0.0001, 0.001, 0.0001)
T = 2

# Определение констант и списков погрешностей
a = 1
tl = 1
epsx1 = []
epsx2 = []
epsx3 = []
epsx4 = []

# Определение функции для промежутка [-1, 0]
def f_offset(t):
    return t

# Определение искомой функции для промежутка [0, 1]
def f_set(t):
    return np.exp(-a/2*((t-1)**2-1))-1

for tau in tau_m:
    t = np.arange(0, T, tau)
    
    eps1 = 0
    eps2 = 0
    eps3 = 0
    eps4 = 0
    
    x_t1 = [0]*(round( ( T ) /tau) + round(1/tau))
    x_t2 = [0]*(round((T)/tau) + round(1/tau))
    x_t3 = [0]*(round((T)/tau) + round(1/tau))
    x_t4 = [0]*(round((T)/tau) + round(1/tau))

    # I Метод
    # начальные значения для функции z(t-1)
    for i in range(int(1/tau)):
        x_t1[i] = f_offset(tau * i - tl)

    # реализация метода
    for i in range(1, round(T/tau)):
        x_t1[i + int(1/tau)] = x_t1[i + int(1/tau) - 1] - tau*(a*(t[i-1]-1))*(1+x_t1[i + int(1/tau) - 1])
        eps1 = max(eps1, abs(x_t1[i + int(1/tau)]-f_set(t[i])))
    x_t1 = x_t1[int(1/tau):int(1/tau)+round((T)/tau)]
    
    # II метод
    # начальные значения для функции z(t-1)
    for i in range(int(1/tau)):
        x_t2[i] = f_offset(tau * i - tl)

    for i in range(1, round(T/tau)):
        x_t2[i + int(1/tau)] = (x_t2[i + int(1/tau) - 1] - tau/2*(a*(t[i-1]-1)*(1+x_t2[i + int(1/tau) - 1]) + a*(t[i]-1)))/(1 + tau/2*a*(t[i]-1))
        eps2 = max(eps2, abs(x_t2[i + int(1/tau)]-f_set(t[i])))
    x_t2 = x_t2[int(1/tau):int(1/tau)+round((T)/tau)]

    # III метод
    # начальные значения для функции z(t-1)
    for i in range(int(1/tau)):
        x_t3[i] = f_offset(tau * i - tl)

    for i in range(1, round(T/tau)):
        xt = x_t3[i + int(1/tau) - 1] - tau*(a*(t[i-1]-1))*(1+x_t3[i + int(1/tau) - 1])
        x_t3[i + int(1/tau)] = x_t3[i + int(1/tau) - 1] - tau/2*(a*(t[i-1]-1)*(1+x_t3[i + int(1/tau) - 1]) + a*(t[i]-1)*(1+xt))
        eps3 = max(eps3, abs(x_t3[i + int(1/tau)]-f_set(t[i])))
    x_t3 = x_t3[int(1/tau):int(1/tau)+round((T)/tau)]

    # IV метод
    # начальные значения для функции z(t-1)
    for i in range(int(1/tau)):
        x_t4[i] = f_offset(tau * i - tl)

    for i in range(1, round(T/tau)):
        k1 = -(a*(t[i-1]-1))*(1+x_t4[i + int(1/tau) - 1])
        k2 = -(a*(t[i-1]-1))*(1+x_t4[i + int(1/tau) - 1] + tau/2*k1)
        k3 = -(a*(t[i-1]-1))*(1+x_t4[i + int(1/tau) - 1] + tau/2*k2)
        k4 = -(a*(t[i-1]-1))*(1+x_t4[i + int(1/tau) - 1] + tau*k3)
        x_t4[i + int(1/tau)] = x_t4[i + int(1/tau) - 1] + tau/6*(k1 + 2*k2 + 2*k3 + k4)
        eps4 = max(eps4, abs(x_t4[i + int(1/tau)]-f_set(t[i])))
    x_t4 = x_t4[int(1/tau):int(1/tau)+round((T)/tau)]

    epsx1.append(np.log(eps1))
    epsx2.append(np.log(eps2))
    epsx3.append(np.log(eps3))
    epsx4.append(np.log(eps4))
    
# Создание окна
fig, ax = plt.subplots(2, 2, figsize=(10, 5.4))

# True func
# ax[0, 0].plot(t, f_set(t), label="y(z)")
# ax[0, 0].set_title("True func")

# Метод 1
ax[0, 0].plot(np.log(tau_m), epsx1, label="log(eps1x)")
ax[0, 0].set_title("Method 1")
ax[0, 0].text(-8, -9, "kx = "+str(round(np.polyfit(np.log(tau_m), epsx1, 1)[0], 5)))

# Метод 2
ax[0, 1].plot(np.log(tau_m), epsx2, label="log(eps1x)")
ax[0, 1].set_title("Method 2")
ax[0, 1].text(-8, -9, "kx = "+str(round(np.polyfit(np.log(tau_m), epsx2, 1)[0], 5)))

# Метод 3
ax[1, 0].plot(np.log(tau_m), epsx3, label="log(eps1x)")
ax[1, 0].set_title("Method 3")
ax[1, 0].text(-8, -9, "kx = "+str(round(np.polyfit(np.log(tau_m), epsx3, 1)[0], 5)))

# Метод 4
ax[1, 1].plot(np.log(tau_m), epsx4, label="log(eps1x)")
ax[1, 1].set_title("Method 4")
ax[1, 1].text(-8, -9, "kx = "+str(round(np.polyfit(np.log(tau_m), epsx4, 1)[0], 5)))

for ax in ax.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
fig.tight_layout()
plt.show()
