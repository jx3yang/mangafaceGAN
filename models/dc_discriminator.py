from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers

class DCDiscriminator(object):
    def __init__(self, shape: tuple, latent_space_size: int):
        self.height, self.width, self.channels = shape
        self.model = self.build_model(latent_space_size)
        self.model.compile(
            loss='binary_crossentropy',
            optimizer=Adam(lr=1e-4, beta_1=0.2),
            metrics=['accuracy']
        )
    
    def build_model(self, latent_space_size: int)->Sequential:
        model = Sequential()

        model.add(
            layers.Conv2D(
                64, 5,
                strides=(2,2), input_shape=(self.height, self.width, self.channels),
                padding='same', activation=layers.LeakyReLU(alpha=0.2)
            )
        )
        model.add(layers.Dropout(0.3))
        model.add(layers.BatchNormalization())

        model.add(
            layers.Conv2D(
                128, 5, strides=(2,2),
                padding='same', activation=layers.LeakyReLU(alpha=0.2)
            )
        )
        model.add(layers.Dropout(0.3))
        model.add(layers.BatchNormalization())

        model.add(layers.Flatten())
        model.add(layers.Dense(1, activation='sigmoid'))

        return model
