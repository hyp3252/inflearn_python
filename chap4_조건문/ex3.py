# 20kg가 이상이면 20,000원의 추가비용
# 20kg 미만이면 수수료 없음. 짐의 무게를 입력받고 지불해야 하는 금액은?


# weight = float(input("짐 무게 : "))

# default_weight = 20
# add_perchase = 20000

# if weight < default_weight:
#     print("free")
    
# elif weight >= default_weight:
#     print("{}원의 추가 비용발생".format(add_perchase))



# 20kg 미만이면 공짜.
# 20kg 이상일 경우 20kg 당 20,000원의 추가비용이면?

weight = float(input("짐의 무게 :"))

default_weight = 20
add_perchase = 20000

if weight < default_weight:
    print("free")
    
elif weight >= default_weight and weight//default_weight >= 1:
    print("{}원이 추가되었습니다.".format(int(add_perchase * (weight//default_weight))))

