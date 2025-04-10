import tensorflow as tf
import numpy as np

# Create a simple model (classification example)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(10,)),  # 10 input features
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')  # Binary classification
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Generate fake training data
x_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, size=(100,))

# Train model
model.fit(x_train, y_train, epochs=10)

# Save the model
model.save("toastcake_model")
print("✅ Model saved successfully!")
