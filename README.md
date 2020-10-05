OOP에서

class, instance

class on Disk(static - resourece)
instance on Memory(dynamic - resource)
생성자 (constructor) 외에는 instance를 만들 수 없다.

생성자는 클래스명(ㄷ문자로 시작하는) 예 parameter - zone 이라 불리는 () 구조

instance = Constructor(param)

notation : 표기법 a = '1' (str)   a = 1 (int)     a = 1.0(float)
annotation : 주석

JavaScript                                  Java
constant => const           상수            static
variable => let             변수            int, String 등등

data -> constant + variable => state

variable은 change 요소를 가지고 있는 존재 -> True
constant 는 change 요소를 가지고 있지 않은 존재 -> False

state를 종류에 따라 (추상화) : 4가지로 분류, CRUD(create, read, update, delete)

REST(Representational State Transfer)
6가지 조건
1) CS 구조(client, server)
2) stateless : 클라이언트의 콘텍스트가 False        즉, 클라이언트의 콘텍스트가 서버에 저장되어서는 안된다.
    client context - true
    server context - false
3) 캐서 처리 가능(Cacheable)
4) 중간 서버            예)WAS(tomcat)
5) URI를 사용하여 data를 JSON 형식으로 전송
6)




SQL : Language

react 는 REST 방식으로

pip install Flask-RESTful
을 사용해 설치해준다.


controller 라는 이름도 사용하지만 같은 의미로 라우터()


