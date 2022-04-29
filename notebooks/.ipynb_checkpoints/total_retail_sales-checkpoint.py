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

item_count = pd.read_csv('~/pipeline_mvp/data/item_count.csv')

item_count = item_count.set_index('item')

retail_cost = pd.read_csv('~/pipeline_mvp/data/retail_cost_per_item.csv')

retail_cost = retail_cost.set_index('item')



count_cost = pd.concat([retail_cost, item_count], axis=1)

count_cost['retail_cost_per_item'] * count_cost['value']

count_cost['total_sales'] = count_cost['retail_cost_per_item'] * count_cost['value']

count_cost.to_csv('~/pipeline_mvp/data/total_retail_sales.csv')


