import numpy as np

list1=[1,2,3,4]
a=np.array(list1)
# print(a)
# print(a.shape)
list2=[[1,2,3],[1,2,3,],[1,2,3],[1,2,3]]
b=np.array(list2)
# print(b)
# print(b.shape)
list3=[[],[],[]]
c=np.array(list3)
# print(c)
# print(c.shape)
# numpy에서 배열의 차원을 판단할 때에는, 반드시 하나의 요소들이 리스트여야만 두번째 차원으로 세기 시작한다.(4,0)이런 식..
# 요소들이 a와 같이 숫자일 경우에는 numpy에서는 차원이 하나만 있다고 판단한다. 이게 맞는게, 실제로도 차원이 하나 뿐이다.
# 아래의 경우, 차원이 세 개인 경우이다.
list4=[[[1,2,3,4],[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]]]
d=np.array(list4)
# print(d)
# print(d.shape)
# 데이터사이언스스쿨
# 연습문제3-1
array3_1=np.array(range(8)).reshape((8,))
array3_1=(array3_1+1)*10
print(array3_1)
# 연습문제3-2
array3_2 = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])
an1=array3_2[1,2]
an2=array3_2[2,4]
an3=array3_2[1,1:3]
an4=array3_2[1:,2]
an5=array3_2[:2,0:2]
print([an1,an2,an3,an4,an5])

# 내가 세울 데이터 프레임은, 18,19,20,21 년도 별로 나뉘며, 첫번째 차원 안에는 코드, 매출액, 영업이익, EBIT배수가 적힌다.
Data=np.zeros(shape=(4,4),dtype=int)
print(Data)
# numpy array에 데이터 입력법
Data[(0,0)]=4
print(Data)