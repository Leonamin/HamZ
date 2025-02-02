# x y 와 같은 입력을 통해 (x, y) 좌표를 반환하는 함수
def make_point():
    raw = input()
    x, y = raw.split()
    
    return (int(x), int(y))

# 유클리드 거리 공식 두개의 점(map1, map2) 사이의 거리를 반환
def euclidean_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    
# 브루트 포스 방식으로 가장 가까운 두 점 거리 구하는 함수
def brute_force(points):
    distance = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            temp = euclidean_distance(points[i], points[j])
            
            if distance is None or temp < distance:
                # print("temp: {0}, distance: {1}".format(temp, distance))
                # print("points[i]: {0}, points[j]: {1}".format(points[i], points[j]))
                distance = temp

    return distance
        
        
def recursive(points):
    # mid = len(points)
    if len(points) <= 3:
        return brute_force(points)
        
    else:
        mid = len(points) // 2
        left = points[:mid]
        right = points[mid:]
        
        left_min = recursive(left)
        right_min = recursive(right)
        
        d = min(left_min, right_min)
        
        # 경계선 근처를 찾아야한다는데 무슨 뜻이지?
        
        return d
    

# 테스트 코드
def print_points(points):
    for point in points:
        print("x: {0}, y: {1}".format(point[0], point[1]))

"""
5
0 0
3 4
7 6
10 2
6 9
"""

if __name__ == "__main__":
    points = []
    count = input()
    
    for i in range(int(count)):
        points.append(make_point())
    
    points.sort()
        
    answer = recursive(points)
    # answer = brute_force(points)
    print(answer)