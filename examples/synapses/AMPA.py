import matplotlib.pyplot as plt

import npbrain as nn

nn.profile.set_backend('numba')


def run_ampa(cls, num_pre=5, num_post=10, prob=1., duration=650.):
    pre = nn.FreqInput(num_pre, 10., 100.)
    post = nn.generate_fake_neuron(num_post)
    conn = nn.conn.fixed_prob(pre.num, post.num, prob)
    ampa = cls(pre, post, conn, delay=2.)
    mon = nn.StateMonitor(ampa, ['g_post', 's'])
    net = nn.Network(ampa, pre, post, mon)

    net.run(duration, report=True)

    ts = net.run_time()
    fig, gs = nn.vis.get_figure(1, 1, 5, 10)
    fig.add_subplot(gs[0, 0])
    plt.plot(ts, mon.g_post[:, 0], label='g_post')
    plt.plot(ts, mon.s[:, 0], label='s')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    for num in [1, 10]:
        run_ampa(nn.AMPA1, num, num)
        run_ampa(nn.AMPA2, num, num)
