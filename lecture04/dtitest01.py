width = float(input('ป้อนความกว้าง: '))
length = float(input('ป้อนความยาว: '))
height = float(input('ป้อนความสูง: '))
gallon_per_area = float(input('1 แกลลอนทาได้พื้นที่ (ตารางเมตร): '))

area = width * height * length
gallons_needed = area / gallon_per_area

print('------------------------------------------------')
print('พื้นที่ 6 ด้าน {} ตร.ซม จะต้องใช้สี {} แกลลอน'.format(area, round(gallons_needed)))




