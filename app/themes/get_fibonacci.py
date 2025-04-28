from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

# レスポンスの型定義
class FibonacciResponse(BaseModel):
    number: int
    fibonacci: int

# フィボナッチ数を計算
def calculate_fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# エンドポイント
@router.get("/fibonacci", response_model=FibonacciResponse)
async def get_fibonacci(number: int = Query(..., ge=1, le=40)):
    fib = calculate_fibonacci(number)
    return FibonacciResponse(number=number, fibonacci=fib)