money = input("ป้อนจำนวนเงิน: ")
people = input("ป้อนจำนวนคน: ")
productValue = int(money)/float(people)
productValueText = format(productValue, ".2f")
print("หลังจากหารแล้วจะได้คนละ", productValueText, "บาท")
print("หลังจากหารแล้วจะได้คนละ " + productValueText + " บาท")
print("หลังจากหารแล้วจะได้คนละ {} บาท".format(productValueText))
print(f"หลังจากหารแล้วจะได้คนละ {productValueText} บาท")