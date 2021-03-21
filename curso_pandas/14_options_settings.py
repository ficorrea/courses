import pandas as pd
import numpy as np

# Mudando atributos e opções e dot sintax
data = np.random.randint(0, 100, [1000, 50])
df = pd.DataFrame(data)
pd.options.display.max_rows = 30
pd.options.display.max_columns = 30

# Mudando opções dos métodos
pd.get_option('max_rows')
pd.set_option('max_rows', 10)
pd.reset_option('max_rows')
pd.describe_option('max_rows')

# Opção de precisão
df = pd.DataFrame(np.random.randn(3, 3))
pd.options.display.precision = 3
pd.get_option('precision')
pd.set_option('precision', 4)


