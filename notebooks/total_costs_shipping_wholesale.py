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

total_wholesale_cost = pd.read_csv('~/pipeline_mvp/data/total_cost.csv')

total_wholesale_cost = total_wholesale_cost.set_index('item')

shipping_cost = pd.read_csv('~/pipeline_mvp/data/shipping_cost.csv')

shipping_cost = shipping_cost.set_index('item')

total_cost = total_wholesale_cost['total_cost'] + shipping_cost['ship_cost']

shipping_cost

total_cost.to_csv('~/pipeline_mvp/data/total_item_cost.csv')


