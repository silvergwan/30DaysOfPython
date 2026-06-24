'''

과제 2 — 배열 정보 확인

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 1. arr.shape 출력 — 배열 모양
# 2. arr.dtype 출력 — 데이터 타입
# 3. arr.ndim 출력 — 몇 차원인지
shape이 제일 중요합니다. ML 코드에서 에러 나면 90%가 shape 불일치 때문입니다. 나중에 "expected shape (32, 768) but got (32, 512)" 같은 에러를 자주 보게 됩니다.

'''
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)
print(arr.dtype)
print(arr.ndim)