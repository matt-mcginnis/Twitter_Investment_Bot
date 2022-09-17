from bs4 import BeautifulSoup
from typing import List
import requests

def get_raw_investment_data(url:str, head:dict) -> BeautifulSoup:
    '''
    Function to return structured table 
    data from webpage given the URL
    '''
    r = requests.get(url, headers=head)
    table_soup = BeautifulSoup(r.content, 'html5lib')
    table = table_soup.find('table', attrs = {'id':'grid'})
    return table

def get_investment_data_multiple_qtrs(qrts: List[tuple], data:BeautifulSoup) -> List[str]:
    '''
    Wrapper function to return a list 
    of investment data strings for 
    multiple quarters and years
    '''
    for q_data in qrts:
        get_investment_data_single_qtr(q_data[0], q_data[1], data)

def get_investment_data_single_qtr(qtr:str, year:str, data:BeautifulSoup) -> List[str]:
    '''
    Function to return a list of 
    investment data strings given 
    a specific quarter and year
    '''
    current_qtr = None
    quarterly_data = []

    for row in data.findAll('tr'):
        qtr_data = row.findAll('b')
        if len(qtr_data) != 0:
            current_qtr = ' - '.join([html.getText() for html in qtr_data])
        elif current_qtr != f'{qtr} - {year}':
            continue
        else:
            stock_names = row.findAll('td', attrs = {'class':['stock', 'buy', 'sell']})
            stock_info = ' - '.join([html.getText() for html in stock_names])
            combined_info = f'{current_qtr}\n{stock_info}'
            quarterly_data.append(combined_info)

    return quarterly_data