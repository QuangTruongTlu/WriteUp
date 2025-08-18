# Web/Renderer
> `Point` : `100`

> `Description` : `Introducing Renderer! A free-to-use app to render your images!`

> `Attachments` : [chall.zip](https://example.com)

> `Flag` : `scriptCTF{my_c00k135_4r3_n0t_s4f3!_9f3fab868a42}`
***

## 1. Phân tích

>Đến với challenge web đầu tiên của giải này, sau khi mở instant lên và truy cập bạn sẽ thấy giao diện như sau :

![giaodien](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_1.png?raw=true)
![uploadfile](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_2.png?raw=true)
>Như bạn đã thấy thì chức năng chính duy nhất của nó là upload file.
>Có vẻ không có quá nhiều thông tin nên chúng ta sẽ đi thẳng vào Source code được cung cấp.
>Khi giải nén file chall.zip ta sẽ có được cấu trúc file như sau:
```
chall
├── static
│   └── uploads
│       └── secrets
│           └── secret_cookie.txt
├── templates
│   ├── display.html
│   └── upload.html
├── app.py
└── flag.txt

```
>Có 1 file mà ngay lúc giải nén ra mình để ý tới đó chính là : 
>>```secret_cookie.txt```
>>```
>>
>>```
>>_Nó trống trơn không có nội dung gì bên trong cả_

>Vì Vậy mình quyết định đi thẳng vào phân tích ```app.py``` (Phân tích từng hàm 1 nhé)
```python
def allowed(name):
    if name.split('.')[1] in ['jpg','jpeg','png','svg']:
        return True
    return False
```
>_Ở hàm này thì nó kiểm tra xem phần mở rộng của file hay [extension](https://bkhost.vn/blog/phan-mo-rong-file/) có phải là hợp lệ hay không. Điều này có nghĩa nó chỉ cho phép các file có đuôi là ```.jpg``` ```.jpeg``` ```.png``` và ```.svg```_

```python
@app.route('/',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed(file.filename):
            filename = file.filename
            hash = sha256(os.urandom(32)).hexdigest()
            filepath = f'./static/uploads/{hash}.{filename.split(".")[1]}'
            file.save(filepath)
            return redirect(f'/render/{hash}.{filename.split(".")[1]}')
    return render_template('upload.html')
```
>_Ở phần này dev đã định nghĩa cho route ```/``` , có 2 phương thức được cho phép là ```GET``` và ```POST```.
>Khi truy cập vào ```/``` thì ngoài việc render ra web ra thấy ở trên còn cung cấp 1 hàm đó chính là ```upload()```
>Hàm này sẽ kiểm tra xem file tải lên có hợp lệ hay không nếu không thì quay lại trang ban đầu , nếu có thì sẽ tạo 1 mã hash gồm 64 kí tự hex , dùng nó thay tên file và lưu vào ```/static/uploads/```. Sau đó chuyển hướng sang trang ```/render/{file}``` để render nó lên.
>Điều này giúp tránh các lỗi liên quan đến việc khai thác đường dẫn như ```path traversal (directory traversal)``` khiến tin tặc có thể thay thế file quan trọng gây lỗi hệ thống_

```python
@app.route('/render/<path:filename>')
def render(filename):
    return render_template('display.html', filename=filename)
```
>_Cái này thì chỉ là khi truy cập ```/render/(filename)``` thì sẽ render ra trang ```display.html``` và render ảnh lên như ta thấy sau khi upload thôi_

```python
@app.route('/developer')
def developer():
    cookie = request.cookies.get("developer_secret_cookie")
    correct = open('./static/uploads/secrets/secret_cookie.txt').read()
    if correct == '':
        c = open('./static/uploads/secrets/secret_cookie.txt','w')
        c.write(sha256(os.urandom(16)).hexdigest())
        c.close()
    correct = open('./static/uploads/secrets/secret_cookie.txt').read()
    if cookie == correct:
        c = open('./static/uploads/secrets/secret_cookie.txt','w')
        c.write(sha256(os.urandom(16)).hexdigest())
        c.close()
        return f"Welcome! There is currently 1 unread message: {open('flag.txt').read()}"
    else:
        return "You are not a developer!"
```
>_Cái này hàm này có vẻ thú vị hơn khi ta biết được có 1 đường dẫn khác là ```/developer```
>Cụ thể khi truy cập đến đường dẫn này, nó sẽ check xem ```developer_secret_cookie``` hiện tại của bạn có phải là ```cookie``` bên trong file ```secret_cookie.txt``` hay không.
>Nhưng trước đó nếu trong file ```secret_cookie.txt``` không có gì thì sẽ tự tạo 1 cookie mới ngẫu nhiên rồi mới tiến hành check.
>Nếu đúng thì sẽ mở file ```flag.txt``` ra để đọc và in ra màn hình , còn không sẽ in ra ```You are not a developer```_

>Cách lấy flag quá rõ ràng chỉ cần có được đúng cookie sau đó truy cập vào ```/developer``` là xong.
Nhưng lấy kiểu gì ? Nếu bạn đã xem qua code bạn có thể thấy không có một giới hạn nào đặt ra cho việc truy cập file từ client side cả điều đó có nghĩa rằng bạn có thể truy cập được file ```secret_cookie.txt``` kia mà không có ràng buộc nào cả.

## Quá trình thực hiện ý tưởng

> Đầu tiên ta sẽ truy cập thử đường dẫn ```https://webchallenge:port/static/uploads/secrets/secret_cookie.txt```
để kiểm chứng xem suy đoán có đúng hay không :

![secret_cookie](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_3.png?raw=true)

> Và chúng ta đã đúng , cơ mà tại sao chưa có gì hết ? Theo như hàm ```developer()``` thì nếu như file secret_cookie.txt này trống sẽ tạo ra 1 cookie mới nhưng để kích hoạt hàm này thì ta cần đến ```/developer``` trước : 

![developer](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_4.png?raw=true)

>Sau đó quay lại ```/static/uploads/secrets/secret_cookie.txt``` lúc này ta sẽ thấy : 

![secret_cookie](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_5.png?raw=true)

>Quay lại ```/developer``` dùng devtool trên chrome để điều chỉnh cookie, thêm vào tên ```developer_secret_cookie``` và giá trị là ```chuỗi ta có được ở treen```:

![cookie](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_6.png?raw=true)

>Và quay lại ```/developer``` và lấy flag thôi :3 

![flag](https://github.com/QuangTruongTlu/WriteUp/blob/main/ScriptCTF-2025/ImageSource/Renderer_7.png?raw=true)

***
