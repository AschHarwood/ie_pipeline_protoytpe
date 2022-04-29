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

total_retail_sales = pd.read_csv('~/pipeline_mvp/data/total_retail_sales.csv')

total_retail_sales = total_retail_sales.set_index('item')

total_cost = pd.read_csv('~/pipeline_mvp/data/total_cost.csv')

total_cost = total_cost.set_index('item')

total_cost

total_retail_sales

net_profit = total_retail_sales.total_sales - total_cost.total_cost

net_profit.to_csv('~/pipeline_mvp/data/net_profit.csv')


