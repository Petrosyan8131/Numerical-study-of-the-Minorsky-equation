import numpy as np

class Methods:
    def __init__(self, tau=0.00001, T=2, n=3, r=-1, q=-1, eps=0.00007):
        # Инициализация сеточной функции
        self.tau = tau
        self.T = T
        self.pt = np.arange(-1, 0, self.tau)
        self.t = np.arange(0, self.T, self.tau)
        # Определение констант
        self.n = n
        self.r = r
        self.q = q
        self.w = np.pi * self.n
        self.eps = eps

        # начальные значения фнкций y и z
        self.z_t = np.empty(round((self.T)/self.tau)+ round(1/self.tau), dtype=np.float64)
        self.y_t = np.empty(round((self.T)/self.tau), dtype=np.float64)
        # self.z_t[0] = 0
        # self.y_t[0] = 0

        # начальные значения для функции z(t-1)
        for i in range(int(1/self.tau)):
            self.z_t[i] = Methods.f_offset(self.tau * i - 1)

    # Определение функции для промежутка [-1, 0]
    def f_offset(a):
        return a

    # I метод
    def first_method(self):
        # построение
        for i in range(1, round(self.T/self.tau)):
            self.y_t[i] = self.tau * self.z_t[i+int(1/self.tau)-1] + self.y_t[i-1]
            self.z_t[i + int(1/self.tau)] = self.z_t[i+int(1/self.tau)-1] + self.tau * (self.eps * (self.z_t[i-1])**3 - self.r*2*self.z_t[i+int(1/self.tau)-1] - self.w**2*self.y_t[i-1] - self.q*2*self.z_t[i-1])
        y_t = self.y_t.copy()
        x_t1 = self.z_t[int(1/self.tau):int(1/self.tau)+round((self.T)/self.tau)].copy()
        return y_t, x_t1, self.T, self.t

   # II метод
    def second_method(self):
        # построение
        for i in range(1, round(self.T/self.tau)):
            self.z_t[i + int(1/self.tau)] = (self.z_t[i + int(1/self.tau)-1] - self.tau*self.w**2/2*(self.y_t[i-1] + self.tau/2*self.z_t[i + int(1/self.tau)-1]) + self.tau/2*(self.eps*self.z_t[i-1]**3 - self.r*2*self.z_t[i + int(1/self.tau)-1] - self.w**2*self.y_t[i-1] - self.q*2*self.z_t[i-1] + self.eps*self.z_t[i]**3 - self.q*2*self.z_t[i]))/(1+self.r*self.tau+self.w**2*self.tau**2/4)
            self.y_t[i] = self.tau/2 * (self.z_t[i+int(1/self.tau)-1] + self.z_t[i+int(1/self.tau)]) + self.y_t[i-1]
        y_t = self.y_t.copy()
        x_t2 = self.z_t[int(1/self.tau):int(1/self.tau)+round((self.T)/self.tau)].copy()
        return y_t, x_t2, self.T, self.t

    # III метод
    def third_method(self):
        # построение
        for i in range(1, round(self.T/self.tau)):
            ys = self.tau * self.z_t[i+int(1/self.tau)-1] + self.y_t[i-1]
            zs = self.z_t[i+int(1/self.tau)-1] + self.tau * (self.eps * (self.z_t[i-1])**3 - self.r*2*self.z_t[i+int(1/self.tau)-1] - self.w**2*self.y_t[i-1] - self.q*2*self.z_t[i-1])
            self.y_t[i] = self.y_t[i-1] + self.tau/2*(self.z_t[i+int(1/self.tau)-1] + zs)
            self.z_t[i + int(1/self.tau)] = self.z_t[i+int(1/self.tau)-1] + self.tau/2*(self.eps*(self.z_t[i-1])**3 - self.r*2*self.z_t[i+int(1/self.tau)-1] - self.w**2*self.y_t[i-1] - self.q*2*self.z_t[i-1] + self.eps*(self.z_t[i])**3 - self.r*2*zs - self.w**2*ys - self.q*2*self.z_t[i])
        y_t = self.y_t.copy()
        x_t3 = self.z_t[int(1/self.tau):int(1/self.tau)+round((self.T)/self.tau)].copy()
        return y_t, x_t3, self.T, self.t
 
    # IV метод
    def fourth_method(self):
        # построение
        for i in range(1, round(self.T/self.tau)):
            k1y = self.z_t[i+int(1/self.tau)-1]
            k2y = self.z_t[i+int(1/self.tau)-1] + self.tau/2
            k3y = self.z_t[i+int(1/self.tau)-1] + self.tau/2
            k4y = self.z_t[i+int(1/self.tau)-1] + self.tau
            k1z = self.eps*self.z_t[i-1]**3 - 2*self.r*self.z_t[i+int(1/self.tau)-1] - self.w**2*self.y_t[i-1] - 2*self.q*self.z_t[i-1]
            k2z = self.eps*self.z_t[i-1]**3 - 2*self.r*(self.z_t[i+int(1/self.tau)-1] + k1z*self.tau/2) - self.w**2*(self.y_t[i-1] + self.tau/2) - 2*self.q*self.z_t[i-1]
            k3z = self.eps*self.z_t[i-1]**3 - 2*self.r*(self.z_t[i+int(1/self.tau)-1] + k2z*self.tau/2) - self.w**2*(self.y_t[i-1] + self.tau/2) - 2*self.q*self.z_t[i-1]
            k4z = self.eps*self.z_t[i-1]**3 - 2*self.r*(self.z_t[i+int(1/self.tau)-1] + k3z*self.tau) - self.w**2*(self.y_t[i-1] + self.tau) - 2*self.q*self.z_t[i-1]
            self.y_t[i] = self.y_t[i-1] + self.tau/6*(k1y + 2*k2y + 2*k3y + k4y)
            self.z_t[i + int(1/self.tau)] = self.z_t[i + int(1/self.tau) - 1] + self.tau/6*(k1z + 2*k2z + 2*k3z + k4z)
        y_t = self.y_t.copy()
        x_t4 = self.z_t[int(1/self.tau):int(1/self.tau)+round((self.T)/self.tau)].copy()
        return y_t, x_t4, self.T, self.t

if __name__ == "__main__": # pragma: no cover
    a = Methods()
    a.first_method()
