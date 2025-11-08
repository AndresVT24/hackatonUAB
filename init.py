import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", palette="pastel")
plt.rcParams.update({
    "figure.figsize": (12, 6),
    "axes.titlesize": 18,
    "axes.labelsize": 14
})

from starter_kits.utils.data_loader import (
    load_aps,
    load_clients,
    print_dataset_summary,
    get_top_aps
)

df_aps = load_aps(
    data_dir="data/AP",
    max_files=None,
    verbose=True
)

# Cargar Clientes (primeros 10 archivos)
df_clients = load_clients(
    data_dir="data/clients",
    max_files=10,
    verbose=True
)

df_aps.head()
print_dataset_summary(df_aps, "Access Points")

print_dataset_summary(df_clients, "Clientes")