import parking_spot_manager
import file_manager

def start_process(path):
    input_list = file_manager.read_file(path)     # file_manager로 input_list를 생성 후  
    spots = parking_spot_manager.str_list_to_class_list(input_list)   #input_list를 parking_spot 클래스 객체로 변환
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
           parking_spot_manager.print_spots(spots)    #print_spots 호출
           
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:                      # spots 와 keyword를  매개변수로 받는 filter_by_ 함수들 호출 
                keyword = input('type name:')    # 각 함수들은 기존에 생성된 객체 삭제 후 새 list 저장
                spots = parking_spot_manager.filter_by_name(spots, keyword)            
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))             #위의 함수들과는 다르게 filter_by_location 함수는  
                min_lon = float(input('type min long:'))            #4개의 실수를 keyword 값으로 받는다.
                max_lon = float(input('type max long:'))
                keyword = (min_lat, max_lat, min_lon, max_lon)      
                spots = parking_spot_manager.filter_by_location(spots, keyword)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:                       #4번 메뉴 선택시 Exit 출력 후 프로그램 종료
            print("Exit")
            break
            
        else:
            print("invalid input")