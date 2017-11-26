from prettytable import PrettyTable


discountFactor = 0.9
groundspin = -1
grounddont = 0
lowspin = 8
lowdont = 0
medspin = 8
meddont = 0
highspin = 8
highdont = 0

calcs =[(-1.00, 0.00), (8.00, 0.00), (8.00, 0.00), (8.00, 0.00)]

t = PrettyTable(['0', 'G', '1', 'L', '2', 'M', '3', 'H', '4'])
t.add_row(['iter', 'spin', 'don\'t', 'spin', 'don\'t', 'spin', 'don\'t', 'spin', 'don\'t'])
for i in range(1, 30):
    zm = max(calcs[0])
    om = max(calcs[1])
    tm = max(calcs[2])
    trm = max(calcs[3])

    r0 = '{0:.2f}'.format(calcs[0][0]) if calcs[0][0] != zm else '{0:.2f}*'.format(calcs[0][0])
    r1 = '{0:.2f}'.format(calcs[0][1]) if calcs[0][1] != zm else '{0:.2f}*'.format(calcs[0][1])
    r2 = '{0:.2f}'.format(calcs[1][0]) if calcs[1][0] != om else '{0:.2f}*'.format(calcs[1][0])
    r3 = '{0:.2f}'.format(calcs[1][1]) if calcs[1][1] != om else '{0:.2f}*'.format(calcs[1][1])
    r4 = '{0:.2f}'.format(calcs[2][0]) if calcs[2][0] != tm else '{0:.2f}*'.format(calcs[2][0])
    r5 = '{0:.2f}'.format(calcs[2][1]) if calcs[2][1] != tm else '{0:.2f}*'.format(calcs[2][1])
    r6 = '{0:.2f}'.format(calcs[3][0]) if calcs[2][0] != trm else '{0:.2f}*'.format(calcs[3][0])
    r7 = '{0:.2f}'.format(calcs[3][1]) if calcs[2][1] != trm else '{0:.2f}*'.format(calcs[3][1])

    t.add_row(['{0}'.format(i), r0, r1, r2, r3, r4, r5, r6, r7])

    gs = discountFactor * max(calcs[1]) + groundspin
    gd = discountFactor * max(calcs[0]) + grounddont

    ls = discountFactor * max(calcs[2]) + lowspin
    ld = discountFactor * max(calcs[1]) + lowdont

    ms = discountFactor * max(calcs[3]) + medspin
    md = discountFactor * max(calcs[1]) + meddont

    hs = discountFactor * max(calcs[3]) + highspin
    hd = discountFactor * max(calcs[2]) + highdont

    calcs = [(gs, gd), (ls, ld), (ms, md), (hs, hd)]

print(t)












# from prettytable import PrettyTable
#
#
# discountFactor = 0.8
# lowspin = -1
# lowdont = 0
# medspin = 2
# meddont = 3
# highspin = 2
# highdont = 3
#
# calcs =[(-1.00, 0.00), (2.00, 3.00), (2.00, 3.00)]
#
# t = PrettyTable(['1', 'L', '2', 'M', '3', 'H', '4'])
# t.add_row(['iter', 'spin', 'don\'t', 'spin', 'don\'t', 'spin', 'don\'t'])
# for i in range(1, 30):
#     zm = max(calcs[0])
#     om = max(calcs[1])
#     tm = max(calcs[2])
#
#     r1 = '{0:.2f}'.format(calcs[0][0]) if calcs[0][0] != zm else '{0:.2f}*'.format(calcs[0][0])
#     r2 = '{0:.2f}'.format(calcs[0][1]) if calcs[0][1] != zm else '{0:.2f}*'.format(calcs[0][1])
#     r3 = '{0:.2f}'.format(calcs[1][0]) if calcs[1][0] != om else '{0:.2f}*'.format(calcs[1][0])
#     r4 = '{0:.2f}'.format(calcs[1][1]) if calcs[1][1] != om else '{0:.2f}*'.format(calcs[1][1])
#     r5 = '{0:.2f}'.format(calcs[2][0]) if calcs[2][0] != tm else '{0:.2f}*'.format(calcs[2][0])
#     r6 = '{0:.2f}'.format(calcs[2][1]) if calcs[2][1] != tm else '{0:.2f}*'.format(calcs[2][1])
#
#     t.add_row(['{0}'.format(i),
#                r1,
#                r2,
#                r3,
#                r4,
#                r5,
#                r6])
#
#     ls = discountFactor * max(calcs[1]) + lowspin
#     ld = discountFactor * max(calcs[0]) + lowdont
#
#     ms = discountFactor * max(calcs[2]) + medspin
#     md = discountFactor * max(calcs[0]) + meddont
#
#     hs = discountFactor * max(calcs[2]) + highspin
#     hd = discountFactor * max(calcs[1]) + highdont
#
#     calcs = [(ls, ld), (ms, md), (hs, hd)]
#
# print(t)