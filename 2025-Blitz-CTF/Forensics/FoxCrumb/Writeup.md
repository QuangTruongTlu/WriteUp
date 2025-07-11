# 🧠 Forensic/FoxCrumb

**🎯 Mức độ challenge:** Cũng Cũng dễ

**🏆 Số điểm:** 338 points

**📝 Mô tả:** 
`Don't keep the jar of cookies in the open...
Take the file from here: https://drive.google.com/file/d/1oLiJ9NQH9UFv-W1iFvlXbUB4k-0X8e7L/view?usp=sharing`

** Author (of this challenge) : ```vedved```

---

## ✍️ Writeups

Bài sẽ cung cấp cho bạn 1 file khá là nặng 

Theo các bài wu khác sẽ là sử dụng volatility 1 công cụ rất hữu hiệu để phân tích các loại file như này

Nhưng 1 cách thần kì nào đó tôi chọn biện pháp khác khổ hơn đó chính là strings

Không sai tôi đã strings hết cái file nặng 2GB đó ra cùng với câu lệnh grep "cookie"

Và đoán xem vì sao có bài này nào , tôi thật sự đã tìm thấy trong đó có 1 dòng 

``` totallynormalcookie|QmxpdHp7ZjFyM2YweF81aDB1bGRfM25jcnlwdF9jMDBrMTM1fQo% ```

Hẳn là bình thường , và thế là tôi có được flag 

## Flag : Blitz{f1r3f0x_5h0uld_3ncrypt_c00k135}

> *Author : TAS.Truong 


