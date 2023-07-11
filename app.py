#!/usr/bin/env python
# coding: utf-8

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import re
# from flask import Flask, render_template, jsonify
from website import create_app

app = create_app()


if __name__ == '__main__':
    # debug reruns the webserver changes everytime you change/add to your code.
    # not needed in production
    app.run(debug=True, port=5000)
