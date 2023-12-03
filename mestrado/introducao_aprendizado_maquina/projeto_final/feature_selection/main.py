from genetic_features import GeneticFeatures
from operator import itemgetter
from types import MethodType
from statistics import mean

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay

FILENAME_COMPLEMENT = 'agg'

# Load dataframe
df = pd.read_csv(f'musk_{FILENAME_COMPLEMENT}.csv')
cols = df.columns[2:-1]
x = df.iloc[:, 2:-1]
y = df.iloc[:, -1]

# Scaling dataframe
rob = MinMaxScaler()
x = rob.fit_transform(x)
x = pd.DataFrame(x, columns=cols)

# Create model
mdl = RandomForestClassifier(criterion='entropy', random_state=42, n_jobs=-1)

# Get columns by individual
def get_cols(df, ind):
    temp = [cl if j == 1 else None for cl, j in zip(df.columns, ind[0:-1])]
    return list(filter(lambda itm : itm is not None, temp))

# Save output data
def write_output(filename, generations, chosen_columns, scores):
    with open(filename, 'w') as file:
        file.write(f'Generations: {generations + 1}\nColumns Choosen: {chosen_columns}\nTotal Features: {len(chosen_columns)}\nScores: {scores}')

# Save dash
def plot_dash(values, selection, crossover):
    # Plot dash of generations
    plt.plot(range(len(values)), values)
    plt.title(f'{str.upper(selection)}.{str.upper(crossover)}')
    plt.xlabel('Generation')
    plt.ylabel('Score')
    plt.savefig(f'{selection}.{crossover}.{FILENAME_COMPLEMENT}.png')
    plt.close()

# Confusion matrix
def confusion_matrix_dash(y_test, y_pred, selection=None, crossover=None):
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.title(f'{str.upper(selection)}.{str.upper(crossover)}')
    plt.savefig(f'cm_{selection}.{crossover}.{FILENAME_COMPLEMENT}.png')
    plt.close()

# ROC Curve
def roc_curve_dash(y_test, y_pred, selection=None, crossover=None):
    RocCurveDisplay.from_predictions(y_test, y_pred, plot_chance_level=True)
    plt.title(f'{str.upper(selection)}.{str.upper(crossover)}')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.savefig(f'roc_{selection}.{crossover}.{FILENAME_COMPLEMENT}.png')
    plt.close()

# Train test dataset
def get_train_dataset(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25)
    return x_train, x_test, y_train, y_test

# Baseline
scores = cross_val_score(mdl, x, y, cv=5, n_jobs=-1)
with open(f'baseline_dataset_{FILENAME_COMPLEMENT}.txt', 'w') as file:
    file.write(f'Score Baseline: {mean(scores)}')
x_train, x_test, y_train, y_test = get_train_dataset(x, y)
mdl.fit(x_train, y_train)
y_pred = mdl.predict(x_test)
confusion_matrix_dash(y_test, y_pred, 'baseline', 'dataset')
roc_curve_dash(y_test, y_pred, 'baseline', 'dataset')

# Running
runs = [('elitism','one-point'), ('elitism','two-points'), ('elitism','uniform'),
        ('roulette','one-point'), ('roulette','two-points'), ('roulette','uniform'), 
        ('tournament','one-point'), ('tournament','two-points'), ('tournament','uniform')]

# GA fixed parameters
ITERATIONS = 30
POP_SIZE = 150

for run in runs:
    # GA parameters
    SELECTION = run[0]
    CROSSOVER = run[1] 

    # Create genetic object
    g = GeneticFeatures(
        qtd_features=x.shape[1], 
        pop_size=POP_SIZE, 
        iterations=ITERATIONS,
        crossover=CROSSOVER,
        selection=SELECTION, 
        metric_ascending=True)

    # Overwrite fit method
    def fit(self):
        for ind in self.pop:
            if ind[-1] is None:
                ccols = get_cols(x, ind)
                scores = cross_val_score(mdl, x[ccols], y, cv=5, n_jobs=-1)
                ind[-1] = mean(scores)
    g.fit = MethodType(fit, g)

    # Running GA
    print(f'{run[0]} - {run[1]}')
    max_values, best_ind, iters = g.run()
    chosen_cols = get_cols(x, best_ind)
    write_output(f'{SELECTION}.{CROSSOVER}.{FILENAME_COMPLEMENT}.txt', iters, chosen_cols, max_values)
    plot_dash(max_values, SELECTION, CROSSOVER)
    x_train, x_test, y_train, y_test = get_train_dataset(x[chosen_cols], y)
    mdl.fit(x_train, y_train)
    y_pred = mdl.predict(x_test)
    confusion_matrix_dash(y_test, y_pred, SELECTION, CROSSOVER)
    roc_curve_dash(y_test, y_pred, SELECTION, CROSSOVER)