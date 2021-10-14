import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
print(tf.__version__)


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


print(f'Training samples {len(x_train):,}')
print(f'Test samples {len(x_test):,}')


def show(idx):
    print(y_train[idx])
    plt.imshow(x_train[idx])

show(2)


np.random.seed(23)
tf.random.set_seed(23)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28,1)))
model.add(tf.keras.layers.Dense(300, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(0.0003),
              metrics=['accuracy'])
model.summary()


model.fit(x_train, y_train, batch_size=32, epochs=20)
model.evaluate(x_test, y_test)

model.save('model')