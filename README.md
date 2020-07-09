# python KakaoTalk

[Python] KakaoTalk windows api 

Script description : Send automatic messages in KakaoTalk chat

# Example

<p align=center>
  <img width="250" src="https://github.com/Xenia101/KakaoTalk-python/blob/master/descriptionImg.PNG?raw=true">
</p>

# Usage

1. Variable setting
  ```python
  chatroom = ""               # 카카오톡 친구 이름
  ```

  ```python
  message = "Hello World!"    # 보내고자 하는 메세지
  ```
2. Send a message
```python
FindChatroom(chatroom)      # 채팅 창 찾기
SendMessage(chatroom, msg)  # 메세지 보내기
```
