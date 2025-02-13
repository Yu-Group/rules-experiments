import sys
sys.path.append("../..")
from feature_importance.scripts.simulations_util import *

X_DGP = sample_real_X
X_PARAMS_DICT = {
    "fpath": "data/X_splicing_cleaned.csv",
    "sample_row_n": 1500,
    "sample_col_n": 100
}
Y_DGP = logistic_lss_model
Y_PARAMS_DICT = {
    "m": 3,
    "r": 2,
    "tau": 0,
    "beta": 2,
    "frac_label_corruption": None
}

VARY_PARAM_NAME = ["frac_label_corruption", "sample_row_n"]
VARY_PARAM_VALS = {"frac_label_corruption": {"0": None, "0.05": 0.05, "0.15": 0.15, "0.25": 0.25},
                   "sample_row_n": {"100": 100, "250": 250, "500": 500, "1000": 1000, "1500": 1500}}
