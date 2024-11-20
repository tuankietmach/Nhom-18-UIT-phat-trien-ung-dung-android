import multiprocessing  

#                     F(9999)
#                    /      \
#               F(9998)    F(9997)
#              /      \    /     \
#         F(9997)     F(9996)    F(9995)  
#                      ...      
#     F(3)     F(2) F(2) F(1) F(2) F(1) F(1) F(0)
#     / \      /  \
#  F(2) F(1)  F(1) F(0)


def fibonacci_recursive(n, result):
    if n <= 1:  # Dieu kien dung
        result.put(n) 
        return n
    else:
        left_result = multiprocessing.Queue()
        right_result = multiprocessing.Queue()
        
        left_process = multiprocessing.Process(target=fibonacci_recursive, args=(n - 1, left_result))   # fibonacci_recursive(9998, left_result), fibonacci_recursive(9998, left_result) tao fibonacci_recursive(9997, left_result_2) + fibonacci_recursive(9996, right_result_2), tiep tuc den dieu kien dung
        left_process.start()

        right_process = multiprocessing.Process(target=fibonacci_recursive, args=(n - 2, right_result))  # fibonacci_recursive(9997, right_result), tuong tu
        right_process.start()
        
        left_process.join()
        right_process.join()
        
        result.put(left_result.get() + right_result.get()) # fibonacci_recursive(9998, left_result) + fibonacci_recursive(9997, right_result)

def fibonacci_parallel(n):
    result = multiprocessing.Queue()  
    fibonacci_recursive(n, result) 
    return result.get()  

if __name__ == "__main__":
    n = 9999 
    fibonacci_number = fibonacci_parallel(n)  
    print(f"Số Fibonacci thứ {n} là: {fibonacci_number}")  
