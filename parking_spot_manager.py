
class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude):   #parking_spot 클래스 초기화 하는 생성자
        self.__item = {'name': name,
                       'city': city, 
                       'district': district,
                       'ptype': ptype, 
                       'longitude': longitude, 
                       'latitude': latitude}

    def get(self, keyword= 'name'):   #keyword를 매개변수로 가지고 기본인수가 name 인 get 메소드
        return self.__item[keyword]

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):    
    class_list= []  #결과 저장할 list 생성
    
    for i in range(len(str_list)):           #str_list를 매개변수로 받아 list 의 개수만큼 반복                  
        item = str_list[i].split(',')        #하나의 list를 쉼표단위로 나눈 후 item list에 저장                               
        class_list.append(parking_spot(item[1], item[2], item[3], item[4], item[5], item[6]))
         
    return class_list                        #class_list에 객체 형태로 item 삽입 후 반환

def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for list in spots:
        print(list)         #list 길이 출력 후 객체 list 하나씩 출력



# spots 과 키워드를 매개변수로 받는 필터링 함수.
# list 함축 사용하여 spots의 객체 중 키워드와 일치하는 값이 존재할 경우 result list에 저장

def filter_by_name(spots, name):
    result = [data for data in spots if name in data.get('name')]
    return result

def filter_by_city(spots, city):
    result = [data for data in spots if city in data.get('city')]
    return result

def filter_by_district(spots, district):
    result = [data for data in spots if district in data.get('district')]
    return result

def filter_by_ptype(spots, ptype):
    result = [data for data in spots if ptype in data.get('ptype')]
    return result


def filter_by_location(spots, locations):
    # 일치하는지 판단하는 위 함수들과 다르게 범위 안에 값이 있는지 판단하는 필터링 함수.
    
    min_lat, max_lat, min_long, max_long = locations # menu_slelctor 에서 keyword 로 4가지 범위값을 입력받음
    result = [data for data in spots if min_lat < float(data.get('latitude')) < max_lat and min_long < float(data.get('longitude')) < max_long] 
    return result         # string 인 data.get() 값을 실수형으로 바꿔줌.

def sort_by_keyword(spots, keyword):       # spots 와 keyword를 매개변수로 받는 sort 함수. 
    result = sorted(spots, key = lambda data: data.get(keyword))        # 정렬의 기준이 되는 key값은 lambda 기능사용
    return result
    
# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)