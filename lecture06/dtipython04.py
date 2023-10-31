#if-else-if

score = int(input('ป้อนคะแนน: '))

if score >= 80:
    print('A')
elif 70 <= score < 80:
    print('B')
elif 60 <= score < 70:
    print('C')
elif 50 <= score < 60:
    print('D')
else:
    print('F')

print('-----------------------------------')
print('Created by DTI-SAU')

