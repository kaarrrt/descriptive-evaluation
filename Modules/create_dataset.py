import numpy as np
import pandas as pd

# Create random data
keywords = np.random.randint(1, 7, size=(10000,))
grammar = np.random.randint(0, 2, size=(10000,))
qst = np.random.randint(1, 7, size=(10000,))
classes = np.random.randint(1, 10, size=(10000,))

# Combine data into a DataFrame
df = pd.DataFrame({'keyword': keywords, 'grammar': grammar, 'qst': qst, 'class': classes})

# Save DataFrame to CSV file
df.to_csv('dataset.csv', index=False)