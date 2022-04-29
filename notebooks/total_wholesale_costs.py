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

wholesale_costs = pd.read_csv('~/pipeline_mvp/data/wholesale_cost.csv')

wholesale_costs = wholesale_costs.set_index('item')

item_count = pd.read_csv('~/pipeline_mvp/data/item_count.csv')

item_count

item_count = item_count.set_index('item')

whole_count = pd.concat([item_count, wholesale_costs], axis=1)

whole_count

whole_count['total_cost'] = whole_count['value'] * whole_count['wholesale_cost_per_item']

whole_count.to_csv('~/pipeline_mvp/data/total_cost.csv')


