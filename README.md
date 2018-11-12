# tensorflow

- day1 

```python
import tensorflow as tf
import numpy as np

# tensorflow의 자료형(?)은 크게 3가지이다.
# placeholder, Variable, constant 
# type과 shape은 생략 가능하나 웬만하면 명시하자.


#                    데이터타입         [3,3]->리스트도 무방!
x = tf.placeholder(tf.float32, shape = (3, 3))
# placeholder는 input data로 많이 씀.   



y = tf.Variable([1,2,3,4,5,6], dtype = tf.float32)
# Variable은 보통은 weight를 저장할 때 많이 씀
# Variable은 반드시 초기화가 필요함 


z = tf.constant([10, 20, 30, 40, 50], dtype=tf.float32)




# tensorflow에서 더하기를 하려면? 
# 그래프를 만들고 연산 순서에 따라 연산을 해간다.  
# 1. constant의 경우 

a = tf.constant([5])
b = tf.constant([10])
c = tf.constant([2])

sum = a+b+c

sess = tf.Session()
result = sess.run(sum)
print (result)


# 2. variable의 경우는? 


a = tf.Variable([5])
b = tf.Variable([10])
c = tf.Variable([2])

sum = a+b+c

sess = tf.Session()
intit = tf.initialize_all_variable() # 초기화
sees.run(init) # 실행 --> 그때야 비로서 값들이 할당됨
result = sess.run(sum)
print (result)


# 3. placeholder의 경우는?
# feeding 딕셔너리 형태로 매핑을 시킴 
# input data와 placeholder를 딕셔너리로 함께 묶어준다고 이해하면 편할듯
# 세션 돌리기전에 feeding 필수

val1 = 5
val2 = 3
val2 = 2

ph1 = tf.placeholder( dtype=tf.float32 )
ph2 = tf.placeholder( dtype=tf.float32 )
ph3 = tf.placeholder( dtype=tf.float32 )
sum = ph1 + ph2 + ph3

feed_dict = {ph1: val1, ph2:val2, ph3:val3}
#     placeholder가 key   입력 값이 value

sees = tf.Session()
result = sess.run(sum, feed_dict=feed_dict)
print (result)


# placeholder를 헷갈려하는 경우가 많으니 한번 더 보자
image = [1,2,3,4,5,
        [5,4,3,2,1],
        [10,20,30,40,50]]
label = [10,20,30,40,50]

ph_image = tf.placeholder( dtype=tf.float32)
ph_label = tf.placeholder( dtype=tf.float32)

feed_dict = {ph_image:image, ph_label:label}

result_tensor = ph_image + ph_label

sess = tf.Session()
result = sess.run(result_tensor, feed_dict=feed_dict)
print (result)
  
```





- day2
- 가장 기본적인 신경망

```python 
import tensorflow as tf
import numpy as np

input_data = [1,5,3,7,8,10,12]
label_data = [0,0,0,1,0]

x = tf.placeholder(tf.float32, shape=[None, 7])
#shape의 경우 batch size(알 수 없는 경우가 일반적) 뒤에는 차원(열의 갯수, 여기서는 7)
y = tf.placeholder(tf.float32, shape=[None, 5])

# TIP! 
# 좋은 코딩은 숫자 직접 입력하는 것보다 상수로 만들어 주는 것
# 가급적이면 이렇게 합시다

INPUT_SIZE = 7
HIDDEN1_SIZE = 10
HIDDEN2_SIZE = 8
CLASSES = 5 


x = tf.placeholder(tf.float32, shape=[None, INPUT_SIZE])
y_ = tf.placeholder(tf.float32, shape=[None, CLASSES])


feed_dict = {x:input_data,y_:label_data}
W1 = tf.Variable(tf.truncated_normal([INPUT_SIZE,HIDDEN1_SIZE])) 

# weight는 랜덤으로 지정해주기 때문에 tf.truncated_nomal 해준 것
# weight의 shape은 INPUT_SIZE, HIDDEN1_SIZE

bias1 = tf.Variable( tf.zeros(shape = [HIDDEN1_SIZE]), dtype=tf.float32)
# 일반적으로 bias는 zero로 많이 둠 



hidden1 = tf.matmul(x, W1) + bias1

W2 = tf.Variable(tf.truncated_normal([HIDDEN1_SIZE,HIDDEN2_SIZE])) 
# 첫번째 레이어의 아웃풋이 인풋으로 들어가고 두 번째 레이어가 아웃풋
bias2 = tf.Variable( tf.zeros(shape = [HIDDEN2_SIZE]), dtype=tf.float32)

hidden2 = tf.matmul(hidden1, W2) + bias2



```











