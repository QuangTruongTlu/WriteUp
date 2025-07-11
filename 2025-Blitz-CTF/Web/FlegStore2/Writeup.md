# Web/Fleg Store 2.0

**🎯 Mức độ challenge:** Dễ

**🏆 Số điểm:** 50 points

**📝 Mô tả:** 
`My friend tried my flag store and thought it was cliche. He says his fleg store is better. But I think its cliche too. What do you think?`

**Author (of this challenge)** :```Shadowh```

---

## ✍️ Writeups

Khi vào link được cung cấp trước mắt chúng ta sẽ hiện lên 1 giao diện như sau
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore2/Evidence/Evd1.png">
Gồm có 4 chức năng bao gồm bộ đếm số lần click , tạo file backup , khôi phục file backup và mua flag
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore2/Evidence/Evd2.png">
Và như bạn thấy để mua flag bạn cần có 9999 điểm mới đổi được flag

Vậy phải làm như nào ???

Bạn còn nhớ file backup chứ , ta có thể tạo và load lại nó , file backup được tạo ra là 1 file json 

Đây là 1 số nội dung có trong file backup và có 1 dòng đặc biệt

<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore2/Evidence/Evd3.png">

Dòng clickStore : là dòng lưu trữ số lượng click của mình 

Vậy ta sẽ chỉnh sửa dòng này thành 9999 và tải lên lại xem thử

<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore2/Evidence/Evd3.png">

<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore2/Evidence/Evd3.png">

Và giờ chỉ còn việc đi mua flag và flag là của bạn!

## Flag:Blitz{FlEg_l00t3R_sh0p_Butt_w1th_cl1qu35}


> *Author : TAS.Truong 


