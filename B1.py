print("---- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ----")

# Khởi tạo biến tổng ngân sách trước vòng lặp
total_budget = 0  

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    
    # Nhập mức lương
    salary = int(input("Nhập mức Lương (VND): "))
    
    # Cộng dồn lương vào tổng ngân sách
    total_budget = total_budget + salary  

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print(" KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")
