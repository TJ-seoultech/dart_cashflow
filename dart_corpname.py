import OpenDartReader
import dart_fss as dart
import numpy as np
api_key='61aa7750da362362a64ef46a79ca0198d2d41452'
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 라디에이터 생산품과 연관된 공시대상
automotive_parts_manufacturer = corp_list.find_by_product('자동차부품')
file=open("기업리스트.txt",'w')
man_len=0
for manufacturer in automotive_parts_manufacturer:
    file.write('{}\n'.format(manufacturer._info['corp_name']))
    man_len+=1
print(man_len)
file.close()
'''
# 내가 조사할 기업들
corp_dict={
    '라디에이터':['삼성공조', '한온시스템'],
    '배기조직':['세종공업','코렌스'],
    '안전벨트':['삼송','코오롱인더','효성','원태','파워텍코리아'],
    '에어백':['현대모비스','SNT모티브','효성첨단소재','코오롱인더스트리'],
    '연료탱크':[]
}
category=corp_dict.keys()
unidentified_corp=list()
Data=np.array(shape=(4,))
print(Data)

class cashflow_corp():
    def __init__(self, company_name):
        self.name=company_name
        self.element_serial_info=np.zeros(shape=(4,))

    def show_element_name(self):
        print(self.name)

    def get_element_code(self):
        element_code= corp_list.find_by_corp_name(self.name)[0].corp_code
        print(element_code)


radiator = cashflow_corp('삼성전자')
radiator.show_element_name()
radiator.get_element_code()

for parts in category:
    # print(corp_dict[parts])
    for company in corp_dict[parts]:
        try:
            corp_list.find_by_corp_name(company)
            company = cashflow_corp(company)
            company.show_element_name()
            company.get_element_code()
        except:
            unidentified_corp.append(company)
print(unidentified_corp)

# # 2012년부터 연간 연결재무제표 불러오기
# fs = samsung.extract_fs(bgn_de='20120101')
#
# # 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
# fs.save()
'''
