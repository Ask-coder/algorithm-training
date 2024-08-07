'''
Задача процентная ставка по кредиту (X% годовых), срок кредитования (N месяцев) и сумма кредита (M рублей)

Необходимо рассчитать размер аннуитетного ежемесячного платежа

Решение подзадачи о ежемесячном платеже
Ежемесячный процент не равен X/12! подберём его бинпоиском

Будем перебирать сумму платежа бинпоиском, а в качестве проверки моделировать процесс ежемесячной выплаты, 
уменьшая тело кредита на разницу между суммой платежаи ежемесячным процентом


'''
def checkmonthlyperc(mperc, yperc):
    msum = 1 + mperc / 100
    ysum = 1 + yperc / 100
    return msum ** 12 >= ysum

def checkcredit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return creditsum <= 0


def fbinsearch(l, r, eps, check, checkparams):
    while(l + eps) < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l


x = 12 
eps = 0.0001
mperc = fbinsearch(0, x, eps, checkmonthlyperc, x)


eps = 0.01
m = 1000000
n = 300
monthlypay = fbinsearch(0, m, eps, checkcredit, (n, m, mperc))
print(monthlypay)
