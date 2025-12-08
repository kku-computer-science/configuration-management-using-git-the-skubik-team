
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x>= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    try:
        input_num = input("ใส่ค่า Integer : ")
        arr = list(map(int, input_num.split()))
        print("เลือก Algorithm: 1 สำหรับ Bubble Sort, 2 สำหรับ Quick Sort")
        algorithm = input("ใส่ตัวเลือกของคุณ: ").strip()

        if algorithm == "1":
            bubbleSort(arr)
        elif algorithm == "2":
            arr = quick_sort(arr)
        else:
            print("กรุณาเลือก 1 หรือ 2 เท่านั้น")
            return

        print("Sort array:", arr)
    except ValueError:
        print("กรุณาใส่ค่า Integer ให้ถูกต้อง")

if __name__ == "__main__":
    main()



