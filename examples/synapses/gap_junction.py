import numpy as np
import matplotlib.pyplot as plt
import npbrain as nn

nn.profile.set_backend('numba')


def run_gj(cls, num_neu, prob=1., gjw=0.1, k_spikelet=0., Iext=12., run_duration=300):
    lif = nn.LIF(num_neu)
    connection = nn.conn.fixed_prob(lif.num, lif.num, prob)
    if k_spikelet > 0.:
        gj = cls(lif, lif, gjw, connection, delay=1., k_spikelet=k_spikelet)
    else:
        gj = cls(lif, lif, gjw, connection, delay=1., )
    neu_mon = nn.StateMonitor(lif)
    syn_mon = nn.StateMonitor(gj)

    net = nn.Network(gj=gj, syn_mon=syn_mon, lif=lif, neu_mon=neu_mon)
    net.run(run_duration, inputs=[lif, np.array([Iext, 0])])

    fig, gs = nn.vis.get_figure(2, 1, 3, 10)
    nn.vis.plot_potential(net.run_time(), neu_mon, (0, 1), fig.add_subplot(gs[0, 0]))
    nn.vis.plot_value(net.run_time(), syn_mon, 'g', (0, 1), fig.add_subplot(gs[1, 0]))
    plt.show()


if __name__ == '__main__':
    run_gj(nn.GapJunction, 2, Iext=15, gjw=0.5, k_spikelet=0.)
    run_gj(nn.GapJunction, 2, Iext=10, gjw=0.5, k_spikelet=0.)
    run_gj(nn.GapJunction_LIF, 2, Iext=15, gjw=0.5, k_spikelet=1)
