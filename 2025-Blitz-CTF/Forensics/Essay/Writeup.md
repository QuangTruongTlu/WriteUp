# 🧠 Forensics/Essay

**🎯 Mức độ challenge:** Trung Bình

**🏆 Số điểm:** 368

**📝 Mô tả:** 

`I've written an essay for my assignment. Could you please take a look at it?`

** Author (of this challenge) : `zwique`

---

## ✍️ Writeups

Bài cung cấp cho ta 1 file docm 

Vào đọc file thì cũng không có gì nhiều , chỉ là 1 bài essay và có đường link rickroll ở phía dưới cùng

Như bạn biết docm hay docx thực chất đều là 1 file zip , vì thế ta có thể giải nén nó ra 

Khi giải nén bạn sẽ có khá nhiều file xml , và đơn nhiên mục tiêu của chúng ta không phải nó

Trong thư mục /Word ta có thể thấy 1 file vbaProject.bin 

Khi tôi strings và đọc qua thì tôi thấy có 1 vài dòng khả nghi liên quan đến 1 cái secret.zip nào đó

Tôi quyết định strings hết file đấy vào 1 file sus.txt và tôi đã nhờ đến người bạn GPT của minh phân tích thử có những gì trong file vba đó

Tôi được biết rằng đây là 1 file độc hại , đã bị làm rối 

Tôi nhờ GPT phục hồi lại dữ liệu từ file text tôi gửi thì nó gồm 2 phần 1 là phần bài essay mà ta có thể đọc được và 1 phần khác là phần mã thực thi bị chèn vào trong đấy 

```vba
Sub AutoOpen()
MsgBox "Welcome to Cybersecurity Briefing", vbInformation
RunCounter
EmbedDesktopZip
DecodeHiddenBase64
End Sub

Sub RunCounter()
Static count As Integer
count = count + 1
If count >= 5 Then
MsgBox "You have opened this document 5 times!", vbExclamation
End If
End Sub

Sub EmbedDesktopZip()
Dim desktopPath As String
Dim zipName As String
Dim embeddedShape As InlineShape
On Error Resume Next
desktopPath = Environ("USERPROFILE") & "\Desktop\"
zipName = Unscramble("zcrseet.ip")
Set embeddedShape = ThisDocument.InlineShapes.AddOLEObject( _
ClassType:="Package", _
FileName:=desktopPath & zipName, _
DisplayAsIcon:=True, _
IconLabel:="Confidential Files", _
IconFileName:="shell32.dll,4")
If Err.Number <> 0 Then
MsgBox "Could not embed resources. Ensure '" & zipName & "' exists on your Desktop.", vbCritical
End If
End Sub

Function Unscramble(obfuscated As String) As String
Dim reversed As String
reversed = StrReverse(obfuscated)
reversed = Replace(reversed, "pi.", ".zip")
Unscramble = reversed
End Function

Sub DecodeHiddenBase64()
Dim encoded As String
Dim decoded As String
encoded = "QmxpdHp7MGwzX0QzTXBfTTNsMTBzfQo"
If Len(encoded) Mod 4 <> 0 Then
encoded = encoded & String(4 - (Len(encoded) Mod 4), "=")
End If
decoded = Base64Decode(encoded)
MsgBox "Decoded message: " & decoded, vbInformation
End Sub

Function Base64Decode(ByVal strData As String) As String
Dim xmlObj As Object
Dim node As Object
Dim byteData() As Byte
Set xmlObj = CreateObject("MSXML2.DOMDocument.6.0")
Set node = xmlObj.createElement("b64")
node.DataType = "bin.base64"
node.Text = strData
byteData = node.nodeTypedValue
Base64Decode = StrConv(byteData, vbUnicode)
End Function
```

Đây là đầy đủ nội dung của mã vba , len lỏi trong đó ta thấy có 1 dòng encode theo sau là 1 chuỗi base 64 là ```QmxpdHp7MGwzX0QzTXBfTTNsMTBzfQo```'

Sau khi decode nó bạn sẽ có flag!

## Flag : Blitz{0l3_D3Mp_M3l10s}



> *Author : TAS.Truong 


