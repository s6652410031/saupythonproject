def inputMoneyPPL () :
    money = float(input('ป้อนเงิน :') )
    person = int(input('ป้อนคน :') )
    return money , person

def calAndShowMoneyShare(money , person) :
    doublefloatmoney = "%.2f" % money
    print(f'จำนวนเงิน {money:.2f} บาท คน {person} คน แชร์กันคนละ {round(money/person)} บาท')
    print("จำนวนเงิน",doublefloatmoney, "บาท คน",person,"คน แชร์กันคนละ" ,round(money/person),"บาท") #ใช้ ,
    print("จำนวนเงิน"+" "+str("%.2f" % money)+" "+"บาท คน"+" "+str(person)+" "+"คน แชร์กันคนละ"+" "+str(round(money/person))+" บาท" ) #ใช้ +
    print("จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท" .format(money,person,(round(money/person)))) #ใช้ format
    print('จำนวนเงิน %.2f บาท คน %d คน แชร์กันคนละ %s บาท' % (money,person, round(money/person)))#ใช้ %

money , person = inputMoneyPPL( )

calAndShowMoneyShare( money , person )
