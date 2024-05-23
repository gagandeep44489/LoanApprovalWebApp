# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:43:11 2024

@author: dell
"""

mkdir ~p ~/.streamlit/
echo "\
[general]\n\
emial = \"gagandeep.44489@gmail.com"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\n
port = $PORT\n\
" > ~/.stremlit/config.toml    