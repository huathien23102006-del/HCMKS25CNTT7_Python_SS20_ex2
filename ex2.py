"""
(1) Phân tích lỗi (Code Review)
1. Vì sao lỗi IndexError: tuple index out of range xảy ra ở dòng r = p[2]?

Dòng code:

r = p[2]

có nghĩa là lấy phần tử thứ 3 trong tuple.

Ví dụ với Levi:

("Levi", 120, 2500)

Tuple có 3 phần tử:

Index	Giá trị
0	Levi
1	120
2	2500

Nên:

p[2]

lấy được:

2500

=> Chạy bình thường.

Nhưng với SofM:

("SofM", 150)

Tuple chỉ có 2 phần tử:

Index	Giá trị
0	SofM
1	150

Không tồn tại:

p[2]

Python cố truy cập vị trí thứ 3 nhưng không có nên báo:

IndexError: tuple index out of range

Nghĩa là:

Truy cập vào index nằm ngoài phạm vi của tuple.

2. Nếu sửa SofM thành:
("SofM", 150, 2800)

thì chương trình chạy tiếp tới Optimus:

("Optimus", 100, "N/A")

Dòng lỗi:

b = (m * 10) + (int(r) * 0.5)

Lúc này:

r = "N/A"

Python chạy:

int("N/A")

Nhưng "N/A" không phải số.

Vì vậy lỗi:

ValueError: invalid literal for int() with base 10
3. Lệnh debug:
print("Đang xử lý:", p)

đặt sau:

for p in ds:

sẽ giúp biết chương trình đang xử lý tới tuyển thủ nào trước khi lỗi.

Ví dụ:

Đang xử lý: ('Levi', 120, 2500)
Tuyển thủ Levi nhận được 2450.0 RP

Đang xử lý: ('SofM', 150)

Nhìn vào đây biết ngay:

Lỗi xảy ra ở SofM
SofM bị thiếu dữ liệu MMR

Đây là kỹ thuật debug bằng cách theo dõi trạng thái dữ liệu.

4. Đổi tên biến theo Clean Code

Code cũ:

Tên cũ	Tên mới	Ý nghĩa
ds	player_records	Danh sách hồ sơ tuyển thủ
p	record	Một bản ghi tuyển thủ
t	name	Tên tuyển thủ
m	matches	Số trận đã chơi
r	mmr	Điểm MMR
b	bonus	Tiền thưởng RP
(2) Refactoring + Exception Handling
# Dữ liệu từ API
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]

"""
# Dữ liệu từ API
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


# Hàm tính tiền thưởng
def calculate_bonus(matches, mmr):

    mmr = int(mmr)

    return (matches * 10) + (mmr * 0.5)



# Hàm xử lý danh sách tuyển thủ
def process_players(player_records):

    print("--- BẢNG TÍNH THƯỞNG RP ---")


    for record in player_records:

        print("Đang xử lý:", record)

        try:

            name = record[0]
            matches = record[1]
            mmr = record[2]

            bonus = calculate_bonus(matches, mmr)

            print(
                f"Tuyển thủ {name} nhận được {bonus} RP"
            )


        except IndexError:

            name = record[0]

            print(
                f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!"
            )

            continue


        except ValueError:

            name = record[0]

            print(
                f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!"
            )

            continue


    print("--- HOÀN TẤT ---")



# Chạy chương trình
process_players(player_records)