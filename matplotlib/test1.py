import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# ͨ��rcParams����ȫ�ֺ����������С
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

np.random.seed(42)

# x��Ĳ�����
x = np.linspace(0, 5, 100)

# ͨ���������߼��������������ݣ��������ģ�;���y�ˡ���
y = 2*np.sin(x) + 0.3*x**2
y_data = y + np.random.normal(scale=0.3, size=100)

# figure()ָ��ͼ������
plt.figure('data')

# '.'������ɢ��ͼ��ÿ��ɢ�����״�Ǹ�Բ
plt.plot(x, y_data, '.')

# ��ģ�͵�ͼ��plot����Ĭ�ϻ�����ͼ
plt.figure('model')
plt.plot(x, y)

# ����ͼ��һ��
plt.figure('data & model')

# ͨ��'k'ָ���ߵ���ɫ��lwָ���ߵĿ��
# ����������������ɫҲ����ָ�����Σ�����'r--'��ʾ��ɫ����
# �������Կ��Բο�������http://matplotlib.org/api/pyplot_api.html
plt.plot(x, y, 'k', lw=3)

# scatter���Ը����׵�����ɢ��ͼ
plt.scatter(x, y_data)

# ����ǰfigure��ͼ���浽�ļ�result.png
plt.savefig('result.png')

# һ��Ҫ�����������û��õ�ͼ��ʾ����Ļ��
plt.show()