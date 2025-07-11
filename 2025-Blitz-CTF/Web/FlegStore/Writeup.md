# Web/FlegStore

**🎯 Mức độ challenge:** Dễ

**🏆 Số điểm:** 50 points

**📝 Mô tả:** 
`I usually want to use this vulnerability in real stores but somehow they are always impenetrable by me. So I decided why not make a store myself. LOL`

**Author (of this challenge)** :```Shadowh```
    
---

## ✍️ Writeups

Khi vào link được cung cấp hiện trước mắt ta sẽ có 1 giao diện đăng nhập như sau 
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd1.png">
Đơn nhiên vì không có tài khoản nên ta sẽ tạo tài khoản với cred là test:test
Đây là giao diện khi login vào
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd2.png">
Ta có các chức năng bao gồm 
- Dashboard 
- Shop : để mua flag 
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd3.png">
- Cart : Giỏ hàng
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd4.png">

- Redeem : Nhập coupon giảm giá
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd5.png">
Và 1 chức năng generate coupon
- Nói nhanh qua các chức năng thì cụ thể ta cần phải mua flag.txt với giá 70$ 
- Cách duy nhất để có tiền đó là thông qua coupon , cứ mỗi coupon sẽ được 10 tiền nhưng nó bị giới hạn chỉ tạo được duy nhất 5 coupon duy nhất
- Vậy hướng giải là gì : tìm cách tạo nhiều coupon hơn ? bằng 1 cách nào đấy để có được nhiều tiền trong 1 coupon ?
- Nếu bạn nghĩ thế thì bạn giống tôi lúc đầu -)))) 
- Nhưng sau khi tôi check source code bằng devtool trên chrome tôi đã phát hiện rằng 
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd6.png">
Đúng vậy đấy nút checkout bị disabled và thậm chí còn có 1 thẻ input bị ẩn đi và ta có thể thay đổi value hay chính là giá tiền
- Bây giờ chỉ cần thay giá tiền về 0 vào xóa dòng disabled trên thẻ button để có thể sử dụng được checkout 
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd7.png">
<img src="https://github.com/QuangTruongTlu/WriteUp/blob/main/2025-Blitz-CTF/Web/FlegStore/Evidence/Evd8.png">
Và bây giờ vào /flag.txt và flag là của bạn

## Flag: Blitz{FLEG_L00T3R_SH0P}



> *Author : TAS.Truong 
> *Toàn bộ file có trong repo là từ link phía dưới chứ giải không cung cấp nhé <3
> ```https://github.com/Shadowh2501/BlitzCTF-2025```

