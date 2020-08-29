import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

class DCGenerator(object):
    def __init__(self, shape: tuple, latent_space_size: int):
        _, _, self.channels = shape
        self.model = self.build_model(latent_space_size)
        self.model.compile(
            loss='binary_crossentropy',
            optimizer=Adam(lr=1e-4, beta_1=0.2),
            metrics=['accuracy']
        )

        self.latent_space = np.random.normal(0, 1, (latent_space_size, ))
    
    def build_model(self, latent_space_size: int)->Sequential:
        model = Sequential()

        model.add(
            layers.Dense(
                8 * 8 * 256,
                activation=layers.LeakyReLU(0.2),
                input_dim=latent_space_size
            )
        )

        model.add(layers.BatchNormalization())
        model.add(layers.Reshape((8, 8, 256)))
        model.add(layers.UpSampling2D())

        model.add(
            layers.Conv2D(
                128, 5,
                padding='same',
                activation=layers.LeakyReLU(0.2)
            )
        )
        model.add(layers.BatchNormalization())

        model.add(layers.UpSampling2D())
        model.add(
            layers.Conv2D(
                64, 5,
                padding='same',
                activation=layers.LeakyReLU(0.2)
            )
        )
        model.add(layers.BatchNormalization())

        model.add(layers.UpSampling2D())
        model.add(
            layers.Conv2D(
                self.channels, 5,
                padding='same',
                activation='tanh'
            )
        )

        return model

    def save_model(self, path: str):
        self.model.save(path)

    def load_model(self, path: str):
        self.model = load_model(path)
