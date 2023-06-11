
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


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)