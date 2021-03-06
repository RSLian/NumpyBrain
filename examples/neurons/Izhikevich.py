import matplotlib.pyplot as plt

import npbrain as nn

nn.profile.set_backend('numba')
nn.profile.set_dt(0.02)

if __name__ == '__main__':
    izh = nn.Izhikevich(10, noise=1.)
    mon = nn.StateMonitor(izh, ['V', 'u'])
    net = nn.Network(hh=izh, mon=mon)
    net.run(duration=100, inputs=[izh, 10], report=True)

    ts = net.run_time()
    fig, gs = nn.vis.get_figure(2, 1, 3, 12)

    indexes = [0, 1, 2]

    fig.add_subplot(gs[0, 0])
    nn.vis.plot_potential(mon, ts, neuron_index=indexes)
    plt.xlim(-0.1, net.current_time + 0.1)
    plt.legend()

    fig.add_subplot(gs[1, 0])
    nn.vis.plot_value(mon, ts, 'u', val_index=indexes)
    plt.xlim(-0.1, net.current_time + 0.1)
    plt.xlabel('Time (ms)')
    plt.legend()

    plt.show()
