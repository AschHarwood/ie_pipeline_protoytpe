# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd

item_weight = pd.read_csv('~/pipeline_mvp/data/item_weight.csv')

item_weight = item_weight.set_index('item')

item_count = pd.read_csv('~/pipeline_mvp/data/item_count.csv')

item_count = item_count.set_index('item')

shipping_cost = pd.read_csv('~/pipeline_mvp/data/shipping_cost_per_lb.csv')

shipping_cost = shipping_cost.set_index('item')

shipping_cost

ship_weight_count = pd.concat([item_count, item_weight, shipping_cost], axis=1)

ship_weight_count.multiply()

ship_weight_count['ship_cost'] = ship_weight_count.iloc[:, 0] * ship_weight_count.iloc[:, 1] * ship_weight_count.iloc[:, 2]

ship_weight_count.to_csv('shipping_cost.csv')


