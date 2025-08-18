# Forensics/Just Some Avocado

> `Point` : `302`

> `Description` : 
> >```!
> >just an innocent little avocado!
> >```

> `Attachments` : [avocado.jpg](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado.jpg)

> `Flag` : `scriptCTF{1_l0ve_d41_v3r0n}`
***

> Challenge này cung cấp cho ta 1 file avocado.jpg.

![avocado](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado.jpg?raw=true)

> Đơn nhiên bước đầu tiên mình sẽ làm chính là đưa lên [aperisovle](https://www.aperisolve.com/) để phân tích file ảnh này : 

![aperisolve1](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado_1.png?raw=true)
![aperisolve1](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado_2.png?raw=true)

>Có vẻ `foremost` đã phát hiện ra có file được giấu trong tấm ảnh này , thông qua strings thì ta thấy có 2 file gồm `justsomezip.zipUT` và `staticnoise.wavUT`
>Ngay lập tức mình tải file foremost về và giải nén ra :
```
foremost
├── audit.txt
├── jpg
│   └── 00000000.jpg
└── zip
    └── 00000196.zip
```
> File .jpg là file ảnh ban đầu và file .zip là file chứa các file bị ẩn 

![file](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado_3.png?raw=true)

> Nhưng file zip này lại yêu cầu mật khẩu , nhưng mật khẩu ở đâu bây giờ ?
> Tìm loanh quanh 1 hồi thì mình nghĩ đến 1 phương án khá thường thấy ở ctf đó chính là crack luôn file zip đấy bằng cách dùng `zip2john` để lấy mã `hash` và dùng `john` với dictionary là [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) `ദ്ദി/ᐠ｡‸｡ᐟ\`

![john](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado_4.png?raw=true)

> Vậy là ta có được password giải nén là `impassive3428`
> Tiến hành giải nén file zip ta có được 2 file ta cần `justsomezip.zip` và `staticnoise.wav`
> Với file wav ta sẽ đem lên web phân tích [Spectrogram](https://spectrogram.sciencemusic.org/) và sẽ được : 

![spectrogram](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado_5.png?raw=true)

> Và ta có được chuỗi `d41v3ron` . Theo suy đoán của mình thì đây là pass của file zip còn lại nên mình tiến hành giải nén nó, và có được file `flag.txt` và lấy được flag

![flag](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/avocado_6.png?raw=true)

>   `(ദ്ദി ๑>؂•̀๑)`
