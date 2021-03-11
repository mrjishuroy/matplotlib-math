import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.001, 0.5001, 0.00001)

s = input('Enter Values of Am Ac Wm Wc\n').split()
res = list(map(int, s))

Am, Ac, Wm, Wc = res

YM = Am * np.sin(Wm * t)

YC = Ac * np.sin(Wc * t)

YMod = (Ac+YM) * np.sin(Wc * t)

Vmax, Vmin = Ac + (max(YM)), Ac - (max(YM))
Mod_Index = (Vmax - Vmin)/(Vmax + Vmin)

fig = plt.figure()
ax1 = fig.add_subplot(311, autoscale_on=True, xlim=(0, 0.5), ylim=(-Am-2, Am+2))
ax2 = fig.add_subplot(312, autoscale_on=True, xlim=(0, 0.5), ylim=(-Ac-2, Ac+4.5))
ax3 = fig.add_subplot(313, autoscale_on=True, xlim=(0, 0.5), ylim=(-Ac-Am-1, 1.2*Ac+Am+2))

line1, = ax1.plot([], [], lw=2)
line1.set_data(t, YM)
ax1.text(0.175, Am+0.5, f'$Yₘ = {Am} Sin({Wm}Hz t)$', fontsize=15)
ax1.axhline(y=0.0, color='black', linestyle='-', linewidth='0.8')
ax1.grid()


line2, = ax2.plot([], [], lw=2)
line2.set_data(t, YC)
ax2.set_ylabel('Amplitude---->', fontsize=20, fontweight='bold')
ax2.text(0.175, Ac+1.0, f'$Yc= {Ac} Sin({Wc}Hz t)$ ', fontsize=15)
ax2.axhline(y=0.0, color='black', linestyle='-', linewidth='0.8')
ax2.grid()


line3, = ax3.plot([], [], lw=2)
line3.set_data(t, YMod)
ax3.set_xlabel('Time---->', fontsize=20, fontweight='bold')
ax3.text(0.175, Ac+Am+1.5, f'$Yₘₒ = ({Ac} + {Am} Sin({Wm}Hz t)) Sin({Wc}Hz t)$', fontsize=15)
ax3.text(0.05, Ac+Am+1.5, r'Vₘₐₓ = '+str('%.2f' % Vmax), fontsize=10)
ax3.text(0.01, Ac+Am+1.5, r'Vₘᵢₙ  = '+str('%.2f' % Vmin), fontsize=10)
ax3.text(0.4, Ac+Am+1.5, r'μ  = '+str('%.3f' % Mod_Index), fontsize=10)
ax3.axhline(y=0.0, color='black', linestyle='-', linewidth='0.8')
ax3.grid()


plt.subplots_adjust(left=0.05, right=0.99, top=0.97, bottom=0.06)
plt.show()
