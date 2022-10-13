# 지구에서 다른별까지의 거리
# 다른별은 지구로부터 40 * 10^12 km 떨어져있다.
# 빛의 속도로 간다면 지구에서 이 별 까지의 걸리는 시간은?



light_speed = 300000 # 1초에 빛의 속도가 갈 수 있는 거리

distance = 40 * pow(10,12)
print(distance)
second_time = distance/light_speed
print(second_time)

print("second :", second_time)
print("minute :", second_time / 60)
print("hour :", second_time / (60*60))
print("liht_year :", second_time / (60*60*24*365))