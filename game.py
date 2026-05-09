import random
from colorama import Fore

# """Biz hozir bu joyda random modulidzn foidalanib games tuzmamisz"""

# number = random.randint(1 , 10)

# objects = ['Cobalt' , 'Damas' , 'Non' , 'Gugurt' , 'Hech nima' , 'Hech nima' , 'Lampichka' , 'Salfetka' , 'Baqloshka' , 'telfon']
# sovgalar = random.choices(objects)

# print('-----------------------------------------------------------------------------')
# qimor = f"Siz bu oyinda {number} raqamdagi maxsulot : {sovgalar} ni yutib oldingiz."
# print(qimor)
# print('-----------------------------------------------------------------------------')






# tanishtiruv = Fore.GREEN + """Siz bu oyinda 1 dan boshlab 10 gacha bo'lgan sonni ichida raqam tanlang va 
# sovg'aga ega bo'ling ."""

# print('-----------------------------------------------------------------------------')
# print(tanishtiruv)
# print('-----------------------------------------------------------------------------')

# number = int(input('Raqam kiriting :'))

# sovgalar = ['Iphone 11 pro' , 'Damas' , 'Televizor' , '2-xonali uy' , 'Gugurt' , 'Lampichka' , 'Fanta' , 'Hech nima ' , 'Salfetka' ]
# rent = random.choices(sovgalar)


# if number == 1:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 2:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 3:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 4:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 5:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 6:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 7:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 8:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 9:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# elif number == 10:
#     a = f"Siz {number} raqami ostida : {rent} yutib oldingiz",
#     print('-----------------------------------------------------------------------------')
#     print(a)
#     print('-----------------------------------------------------------------------------')
# else:
#     print('-----------------------------------------------------------------------------')
#     print("Siz bu oyinda xatolik yuzaga keldi, afsuski yana qayta uruning")
#     print('-----------------------------------------------------------------------------')



about = Fore.LIGHTYELLOW_EX + """Siz bu oyinda 1 dan boshlab 10 gacha bolgan sonlarni ichida 
son tanlang va sizga sovrin o'yin qo'yamisz va siz o'zingiz ko'nglizdan chiqariib 
pul soling va sovga yutib oling ?? 👮🏻‍♂️"""

print('-----------------------------------------------------------------------------')
print(about)
print('-----------------------------------------------------------------------------')

get_Money = float(input('Siz nech pul kiritmoqchisz :'))

if get_Money > 10:
    sort = Fore.GREEN + f"Siz {get_Money} o'yinni davom etirishingiz mumkin "
    print('-----------------------------------------------------------------------------')
    print(sort)
    print('-----------------------------------------------------------------------------')
elif get_Money < 10:
    sort = Fore.RED + f"Siz bu oyinda {get_Money} bilan qatnasha olmaysiz 10 ko'p bo'lishligi lozim"
    print('-----------------------------------------------------------------------------')
    print(sort)
    print('-----------------------------------------------------------------------------')
elif get_Money == 10:
    sort = Fore.GREEN + f"Siz bu oyinda {get_Money} bilan o'yinda qatnasha olasiz qatnasha olasiz"
    print('-----------------------------------------------------------------------------')
    print(sort)
    print('-----------------------------------------------------------------------------')
else:
    print('-----------------------------------------------------------------------------')
    print(Fore.RED + "Siz bu oyinda qonunlardan roiya qilmadiz yana qayta uruning ?")
    print('-----------------------------------------------------------------------------')

Kiritilgan_Somma = f"Siz {get_Money} kiritdingiz tabriklaymisz 🤡 hozir sizda bir matta imkoniyat bor " 
print('-----------------------------------------------------------------------------')
print(Fore.GREEN + Kiritilgan_Somma , "So'm" )
print('-----------------------------------------------------------------------------') 
choices_Number = int(input('Sizning tanlagan raqaminingiz :'))
sovgalar = ['Iphone 11 pro' , 'Damas' , 'Televizor' , '2-xonali uy' , 'Gugurt' , 'Lampichka' , 'Fanta' , 'Hech nima ' , 'Salfetka' ]

full_Code = f"Siz bu o'yinga {Kiritilgan_Somma} so'm kiritib . {choices_Number} raqami ostida : {random.choices(sovgalar)} ni yutib oldingiz"
print('-----------------------------------------------------------------------------') 
print(full_Code)
print('-----------------------------------------------------------------------------') 

