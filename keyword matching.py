#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# import the csv file 
flipkart_products=pd.read_csv("C:\\Users\\shaba\\OneDrive\\Desktop\\products.csv",index_col=False)


# # Project Description:

# This project allows users to search for products in a dataset. Users enter a search keyword, and the system checks if the keyword is found in the  dataset. If a match is found, it displays the products that match the keyword. This project is useful for quickly finding and viewing product information based on user-provided keywords and checking the user what searching.

# In[2]:


flipkart_products


# In[3]:


flipkart_products=flipkart_products.drop(flipkart_products.columns[[6,7]],axis=1)


# In[4]:


flipkart_products


# In[5]:


flipkart_products.head(20)


# In[6]:


x = input("search the product you want :")

print(x)

if flipkart_products['Product Name'].str.contains(x).any():
    print("product was match")
    
else:
    print("product was not match")


# In[7]:


# 3 conditions

x = input("Search for the product you want: ")

print(x)

exact_match=flipkart_products['Product Name'].str.contains(f'^{x}$').any()

somewhat_match=flipkart_products['Product Name'].str.contains(x).any()



if exact_match:
    print("exactly match ")
elif somewhat_match:
    print("some what match")
else:
    print("not match")


# In[8]:


flipkart_products


# In[11]:


# Get the user's input (search query).
x = input("Search for the product you want: ")

columns_to_check = ['Product Name', 'Category', 'Description']

exact_match = any(flipkart_products[col].str.contains(f'^{x}$', case=False, regex=True).any() for col in columns_to_check)


partial_match = any(flipkart_products[col].str.contains(x, case=False, regex=True).any() for col in columns_to_check)

# Check if the user's input matches 'Price' or 'Stock Quantity' columns.

cannot_find_match = (
    flipkart_products['Price'].astype(str).str.contains(x).any() or
    flipkart_products['Stock Quantity'].astype(str).str.contains(x).any()
)

if exact_match:
    print(f"Exact match found in {', '.join(columns_to_check)} ")
elif partial_match:
    print(f"Partial match found in {', '.join(columns_to_check)} ")
elif cannot_find_match:
    print("Cannot be judged based on 'Price' or 'Stock Quantity' columns.")
else:
    print("No match found in the dataset.")


# In[12]:


# Get the user's input (search query).
x = input("Search for the product you want: ")

columns_to_check = ['Product Name', 'Category', 'Description']

exact_match = any(flipkart_products[col].str.contains(f'^{x}$', case=False, regex=True).any() for col in columns_to_check)


partial_match = any(flipkart_products[col].str.contains(x, case=False, regex=True).any() for col in columns_to_check)

# Check if the user's input matches 'Price' or 'Stock Quantity' columns.

cannot_find_match = (
    flipkart_products['Price'].astype(str).str.contains(x).any() or
    flipkart_products['Stock Quantity'].astype(str).str.contains(x).any()
)

if exact_match:
    print(f"Exact match found in dataset ")
elif partial_match:
    print(f"Partial match found in dataset ")
elif cannot_find_match:
    print("Cannot be judged based on 'Price' or 'Stock Quantity' columns.")
else:
    print("No match found in the dataset.")


# In[15]:


# Get the user's input (search query).
x = input("Search for the product you want: ")

columns_to_check = ['Product Name', 'Category', 'Description']

exact_match = any(flipkart_products[col].str.contains(f'^{x}$', case=False, regex=True).any() for col in columns_to_check)


partial_match = any(flipkart_products[col].str.contains(x, case=False, regex=True).any() for col in columns_to_check)

# Check if the user's input matches 'Price' or 'Stock Quantity' columns.

cannot_find_match = (
    flipkart_products['Price'].astype(str).str.contains(x).any() or
    flipkart_products['Stock Quantity'].astype(str).str.contains(x).any()
)

if exact_match:
    print(f"Exact match found in dataset ")
elif partial_match:
    print(f"Partial match found in dataset ")
elif cannot_find_match:
    print("Cannot be judged based on 'Price' or 'Stock Quantity' columns.")
else:
    print("No match found in the dataset.")


# In[14]:


# Get the user's input (search query).
x = input("Search for the product you want: ")

columns_to_check = ['Product Name', 'Category', 'Description']

exact_match = any(flipkart_products[col].str.contains(f'^{x}$', case=False, regex=True).any() for col in columns_to_check)


partial_match = any(flipkart_products[col].str.contains(x, case=False, regex=True).any() for col in columns_to_check)

# Check if the user's input matches 'Price' or 'Stock Quantity' columns.

cannot_find_match = (
    flipkart_products['Price'].astype(str).str.contains(x).any() or
    flipkart_products['Stock Quantity'].astype(str).str.contains(x).any()
)

if exact_match:
    print(f"Exact match found in dataset ")
elif partial_match:
    print(f"Partial match found in dataset ")
elif cannot_find_match:
    print("Cannot be judged based on 'Price' or 'Stock Quantity' columns.")
else:
    print("No match found in the dataset.")

