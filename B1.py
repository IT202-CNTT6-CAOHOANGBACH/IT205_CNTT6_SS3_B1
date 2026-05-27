print("---- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ----")
total_budget = 0;
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input(" Nhập mức lương (VND): "))

    total_budget = total_budget + salary

print("➡ KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")


#code này sai vì vòng lặp for sẽ duyệt lại từng lần mỗi khi xong 1 đk
# biến total dc tạo trong khi lặp lại nên sẽ cứ reset liên tục