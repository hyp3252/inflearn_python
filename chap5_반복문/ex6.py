# 화씨, 섭씨 변환

# for문으로 실수형

# 화씨 0-100도 까지 10도 단위로 증가시키며 섭씨 온도 출력

# 'C = ('F - 32) * 5 / 9
c = 0
for temp in range(0,101,10):
    c = ((temp-32)*5) / 9
    print("화씨온도 : {}, 섭씨온도 : {}".format(round(temp,2), round(c,2)))