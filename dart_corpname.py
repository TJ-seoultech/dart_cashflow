import OpenDartReader
import dart_fss as dart

api_key='61aa7750da362362a64ef46a79ca0198d2d41452'
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()
# # 텍스트파일에 회사 리스트 출력해서 확인해보기
# f=open("기업리스트.txt",'w')
# for corp in corp_list:
#     f.write('{}\n'.format(corp._info['corp_name']))
# f.close()

# # 삼성그룹 검색
# samsung_group = corp_list.find_by_corp_name('삼성', exactly=1)
# for element in samsung_group:
#     print(element.info['corp_name'])
corp_dict={
    '라디에이터':['삼성공조', '한온시스템'],
    '배기조직':['세종공업','코렌스'],
    '안전벨트':['삼송','코오롱인더','효성','원태','파워택코리아'],
    '에어백':['현대모비스','SNT모티브','효성첨단소재','코오롱인더스트리'],
    '연료탱크':[]
}
category=corp_dict.keys()
unidentified_corp=list()


class cashflow_corp():
    def __init__(self, company_name):
        self.name=company_name

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
        # dart 리스트에 없는 기업들에 대해 먼저 클래스 선언후, 아무 검증과정없이 show_element_name과 get_element_code를
        # 해버려서 에러가 발생한다. 이에 대한 대책으로 클래스 선언 전에 미리 리스트 내에 있는 지 검증하기로 결정
        # 그 수단으로 try&except문을 작성했는데, 작성법을 모른다.
        try:
            corp_list.find_by_corp_name(company)
        except:
            unidentified_corp.append(company)
        company=cashflow_corp(company)
        company.show_element_name()
        company.get_element_code()
#       이게 맞나 모르겠다.

# # 2012년부터 연간 연결재무제표 불러오기
# fs = samsung.extract_fs(bgn_de='20120101')
#
# # 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
# fs.save()



# 출처: http://blog.quantylab.com/2020-10-09-dart.html
'''import requests
from io import BytesIO
import zipfile
import xmltodict
import json

api = 'https://opendart.fss.or.kr/api/corpCode.xml'
res = requests.get(api, params={'crtfc_key': '61aa7750da362362a64ef46a79ca0198d2d41452'})
data_xml = zipfile.ZipFile(BytesIO(res.content))
names = data_xml.read('CORPCODE.xml').decode('utf-8')
data_odict = xmltodict.parse(data_xml)
data_dict = json.loads(json.dumps(data_odict))
data = data_dict.get('result', {}).get('list')
for item in data:
    if item['corp_name'] in ["삼성전자", "SK하이닉스", "NAVER"]:
        print(item)'''
