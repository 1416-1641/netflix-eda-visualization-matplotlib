'''This file is created to be contain  all Matplotlib visualization functions'''
import pandas as pd
import matplotlib.pyplot as plt

def line_plot(data:pd.DataFrame,col:str,title : str ="line plot") ->None:
    """
        This function to draw a line plot with one line
        Args:
            data (pd.DataFrame): a data that has a column that i want to draw
            col (str): The column name to plot.
            title(str): a flixeble title of plot
        Returns :
            None :display the plot 
    """
    column=data[col]
    dic={'fontsize':20}
    plt.plot(column,color="palegreen")
    plt.grid()
    plt.title(title,loc='center',fontdict=dic)
    plt.show()

def bar_to_count(data:pd.DataFrame,col:list=[],title,)