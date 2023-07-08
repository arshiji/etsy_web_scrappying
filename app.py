#!/usr/bin/env python
# coding: utf-8

from IPython.display import display, HTML
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Permanently changes the pandas settings
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', -1)


# In[80]:


def scrape_etsy():
    url = "https://www.etsy.com/ca/search?q=canada+tshirt&ref=search_bar"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    product_list = []
    
    # Find product elements on the page
    products = soup.find_all("div", class_="v2-listing-card__info")
    #try:
    for product in products:
        # Extract relevant information
        title = product.find("h3", class_="wt-text-caption v2-listing-card__title wt-text-truncate").text.strip() if product.find("h3", class_="wt-text-caption v2-listing-card__title wt-text-truncate") else None
        price = product.find("span", class_="currency-value").text.strip() if product.find("span", class_="currency-value") else None
        currency = product.find("span", class_="currency-symbol").text.strip() if product.find("span", class_="currency-symbol") else None
        #url = product.find("input", name="listing_url").text.strip()
        delivery = product.find("div", class_="streamline-spacing-shop-rating").text.strip() if product.find("div", class_="streamline-spacing-shop-rating") elif product.find("span", class_="wt-badge wt-badge--small wt-badge--sale-01").text.strip() else print("Paid")  
         
        sales_count = product.find("p", class_="wt-text-title-01 lc-price").text.strip() if product.find("p", class_="wt-text-title-01 lc-price") else None
        org_prc = product.find("p", class_="wt-text-title-01 lc-price").text.strip() if product.find("p", class_="wt-text-title-01 lc-price") else None
        if len(org_prc) > 12:
            sales_count = product.find("p", class_="wt-text-caption search-collage-promotion-price wt-text-slime wt-text-truncate wt-no-wrap")
            if sales_count:
                org_prc = sales_count.find("span", class_="currency-value").text.strip() 

        product_data = {
            "Title": title,
            "Currency": currency,
            "Price": price,
            "Delivery": delivery,
            "sales_price": org_prc
        }

        product_list.append(product_data)
    products = product_list

        
    return products

# Call the function to scrape Etsy
etsy_products = scrape_etsy()
#etsy_products
df = pd.DataFrame(etsy_products)



# In[77]:


# etsy_449_results
def scrape_etsy():
    base_url = "https://www.etsy.com/ca/search?q=canada+tshirt&ref=search_bar"
    product_list = []
    
    page = 1
    while True:
        url = base_url + f"&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find product elements on the page
        products = soup.find_all("div", class_="v2-listing-card__info")
        
        if not products:
            break
        try:
            for product in products:
                # Extract relevant information
                title = product.find("h3", class_="wt-text-caption v2-listing-card__title wt-text-truncate").text.strip()
                price = product.find("span", class_="currency-value").text.strip()
                currency = product.find("span", class_="currency-symbol").text.strip()
                #delivery = product.find("span", class_="wt-badge wt-badge--small wt-badge--sale-01").text.strip()#
                delivery = product.find("div", class_="streamline-spacing-shop-rating").text.strip() if product.find("div", class_="streamline-spacing-shop-rating") else product.find("span", class_="wt-badge wt-badge--small wt-badge--sale-01").text.strip()  
                sales_count = product.find("p", class_="wt-text-title-01 lc-price").text.strip()
                org_prc = product.find("p", class_="wt-text-title-01 lc-price").text.strip()

                if len(org_prc) > 12:
                    sales_count = product.find("p", class_="wt-text-caption search-collage-promotion-price wt-text-slime wt-text-truncate wt-no-wrap")
                    if sales_count:
                        org_prc = sales_count.find("span", class_="currency-value").text.strip()

                product_data = {
                    "Title": title,
                    "Currency": currency,
                    "Price": price,
                    "Delivery": delivery,
                    "sales_price": org_prc
                }

                product_list.append(product_data)
        except:
            pass
        page += 1
    
    return product_list

# Call the function to scrape Etsy
etsy_products = scrape_etsy()

# Convert the list of products to a DataFrame
etsy_results = pd.DataFrame(etsy_products)

# Display the DataFrame
#etsy_results.to_csv("etsy_results.csv")
etsy_results.count()
