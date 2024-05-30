import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 创建一个简单的CNN模型
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(20, 20, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(4, activation='softmax')  # 输出层，4个可能的移动方向（上、下、左、右）
])

# 编译模型
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 训练模型
# 这里我们使用一些随机生成的数据作为训练数据
x_train = np.random.rand(100, 20, 20, 1)
y_train = np.random.randint(0, 4, size=(100, ))

# 训练模型
model.fit(x_train, y_train, epochs=10)

# 使用训练好的模型
# 这里我们生成一个随机输入，让模型预测输出方向
input_data = np.random.rand(1, 20, 20, 1)
prediction = model.predict(input_data)

# 打印预测方向
print("Predicted direction:", np.argmax(prediction))
