import tensorflow as tf


def get_model():
    input_op = tf.keras.Input(shape=(128, 44))

    dropout = 0.0
    layers = tf.keras.layers
    # BATCH_NORM
    x = layers.BatchNormalization()(input_op)

    # LSTM
    # https://github.com/tensorflow/tensorflow/issues/30263
    x = layers.Bidirectional(layers.LSTM(256, activation='sigmoid', return_sequences=True))(x)
    x = layers.Dropout(dropout)(x)

    # LSTM
    # https://github.com/tensorflow/tensorflow/issues/30263
    x = layers.Bidirectional(layers.LSTM(256, activation='sigmoid', return_sequences=True))(x)
    x = layers.Dropout(dropout)(x)

    # LSTM
    # https://github.com/tensorflow/tensorflow/issues/30263
    x = layers.Bidirectional(layers.LSTM(256, activation='sigmoid'))(x)
    x = layers.Dropout(dropout)(x)

    # BATCH_NORM
    x = layers.BatchNormalization()(x)

    # DENSE
    x = layers.Dense(512)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Dropout(dropout)(x)

    # DENSE
    x = layers.Dense(256)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Dropout(dropout)(x)

    # DENSE
    x = layers.Dense(128)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Dropout(dropout)(x)

    # DENSE
    x = layers.Dense(64)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Dropout(dropout)(x)

    output_op = layers.Dense(12)(x)

    return tf.keras.Model(inputs=input_op, outputs=output_op)