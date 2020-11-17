from keras.datasets import mnist
from keras import models, layers
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
d1 = network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
d2 = network.add(layers.Dense(10, activation='softmax'))

train_images = train_images.reshape(60000, 784).astype('float32') / 255
test_images = test_images.reshape(10000, 784).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)

print('Test acc: {0}'.format(test_acc))
