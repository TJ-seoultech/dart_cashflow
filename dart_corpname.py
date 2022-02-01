import OpenDartReader
import dart_fss as dart
import os

import openpyxl
import pandas as pd
import numpy as np
api_key='61aa7750da362362a64ef46a79ca0198d2d41452'
dart.set_api_key(api_key=api_key)

# # DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 기업리스트와 재무자료 파일 이름 지정(지금 파이썬 파일과 같은 폴더 내에 있는 것을 전제로 함).
def name_dependency_test():
    namefile="기업리스트.txt"
    # 라디에이터 생산품과 연관된 공시대상
    if not os.path.exists(namefile):
        automotive_parts_manufacturer = corp_list.find_by_product('자동차부품')
        file=open(namefile,'w')
        man_len=0
        for manufacturer in automotive_parts_manufacturer:
            file.write('{}\n'.format(manufacturer._info['corp_name']))
            man_len+=1
        file.close()
    else:
        file=open(namefile,"r")

def finance_dependency_test():
    financefile="기업회계자료.xlsx"
    if not os.path.exists(financefile):
        wb=openpyxl.Workbook()
        wb.active.title="회계자료"
        wb.save(financefile)
    else:
        wb=openpyxl.load_workbook(financefile)

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
'''

if __name__ == "__main__":
    name_dependency_test()
    finance_dependency_test()
    # 삼성전자 code
    corp_code = '00126380'
    # 모든 상장된 기업 리스트 불러오기
    corp_list = dart.get_corp_list()
    # 삼성전자
    samsung = corp_list.find_by_corp_code(corp_code=corp_code)
    # 사업보고서 검색
    reports = samsung.search_filings(bgn_de='20190101', pblntf_detail_ty='a001')

    # 첫번째 리포트 선택
    report = reports[0]

    # 리포트의 xbrl 데이터
    xbrl = report.xbrl

    # 연결재무제표 존재 여부 확인( True / False)
    xbrl.exist_consolidated()

    # 감사 정보 (영문) -> DataFrame 형태로 반환됨
    audit = xbrl.get_cash_flows()

    # 연결 현금흐름표 추출 (리스트 반환)
    cf = xbrl.get_cash_flows()

    # 연결 현금프름표
    print(cf)
    cf = cf[0]

    # Pandas DataFrame으로 변환
    df = cf.to_DataFrame()
    print("이것은 df의 index")
    print(df.index)
    print("이것은 df의 value")
    print(df.values)
    df.to_excel('samsung_pandas.xlsx')
    print(df)
    '''
    # ------------------------------------------------------------------------------------------------------------------
    # 2012년 01월 01일 부터 연결재무제표 검색
    # fs = samsung.extract_fs(bgn_de='20120101') 와 동일
    fs = dart.fs.extract(corp_code=corp_code, bgn_de='20190101')
    fs.save("totalFS.xlsx")
    # 연결재무상태표
    df_fs = fs['bs']  # 또는 df = fs[0] 또는 df = fs.show('bs')
    # 연결재무상태표 추출에 사용된 Label 정보
    labels_fs = fs.labels['bs']

    # 연결손익계산서
    df_is = fs['is']  # 또는 df = fs[1] 또는 df = fs.show('is')
    # 연결손익계산서 추출에 사용된 Label 정보
    labels_is = fs.labels['is']

    # 연결포괄손익계산서
    df_ci = fs['cis']  # 또는 df = fs[2] 또는 df = fs.show('cis')
    # 연결포괄손익계산서 추출에 사용된 Label 정보
    labels_ci = fs.labels['cis']

    # 현금흐름표
    df_cf = fs['cf']  # 또는 df = fs[3] 또는 df = fs.show('cf')
    # 현금흐름표 추출에 사용된 Label 정보
    labels_cf = fs.labels['cf']
    print(labels_cf)

    # 재무제표 일괄저장 (default: 실행폴더/fsdata/{corp_code}_{report_tp}.xlsx)
    fs.save()

    # 재무제표 일괄저장
    # filename = '삼성전자'
    # fs.save(filename=filename)

# # 2012년부터 연간 연결재무제표 불러오기
# fs = samsung.extract_fs(bgn_de='20120101')
#
# # 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
# fs.save()
'''
