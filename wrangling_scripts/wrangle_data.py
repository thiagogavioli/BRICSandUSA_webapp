import pandas as pd
import plotly.graph_objs as go


def cleandata(dataset, keepcolumns = ['Country Name', '1990','2000', '2010', '2019'], value_variables = ['1990', '2000', '2010', '2019']):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for BRICS + USA economies
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """    
    df = pd.read_csv(dataset, skiprows=4)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    brics = ['United States', 'China', 'India', 'Brazil', 'Russian Federation', 'South Africa']
    df = df[df['Country Name'].isin(brics)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars = value_variables)
    df_melt.columns = ['country','year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # output clean csv file
    return df_melt



def return_figures():
    """Creates five plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the five plotly visualizations

    """

    # first chart plots GDP from 1990 to 2019 
    # as a line chart
    graph_one = []
    df = cleandata('data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1926685.csv')
    df.columns = ['country','year','GDP_in_USD']
    df.sort_values('year', ascending=True, inplace=True)
    countrylist = df.country.unique().tolist()
    
    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val =  df[df['country'] == country].GDP_in_USD.tolist()
        graph_one.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_one = dict(title = 'GDP - 1990 to 2019 (USD)',
                    xaxis = dict(title = 'Year',
                      autotick=False, tick0=1990, dtick=10),
                    yaxis = dict(title = 'GDP'),
                    )
    
# second chart plots GDP per capita from 1990 to 2019    
    graph_two = []
    df = cleandata('data/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_1926744.csv')
    df.columns = ['country','year','GDP_per_capita']
    df.sort_values('year', ascending=True, inplace=True)
    countrylist = df.country.unique().tolist()

    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val =  df[df['country'] == country].GDP_per_capita.tolist()
        graph_two.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_two = dict(title = 'GDP per capita - 1990 to 2019 (USD)',
                    xaxis = dict(title = 'Year',
                      autotick=False, tick0=1990, dtick=10),
                    yaxis = dict(title = 'GDP per capita'),
                    )
    

# third chart plots Exports of goods and services 2019
    graph_three = []
    df = cleandata('data/API_NE.EXP.GNFS.CD_DS2_en_csv_v2_1928255.csv')
    df.columns = ['country','year','EXP']
    df.sort_values('EXP', ascending=False, inplace=True)
    df = df[df['year'] == 2019] 

    graph_three.append(
          go.Bar(
          x = df.country.tolist(),
          y = df.EXP.tolist(),
          )
        )

    layout_three = dict(title = 'Exports of goods and services in 2019 (USD)',
                    xaxis = dict(title = 'Country',),
                    yaxis = dict(title = 'EXP'),
                    )
    
# fourth chart plots Imports of goods and services 2019
    graph_four = []
    df = cleandata('data/API_NE.IMP.GNFS.CD_DS2_en_csv_v2_1926771.csv')
    df.columns = ['country','year','IMP']
    df.sort_values('IMP', ascending=False, inplace=True)
    df = df[df['year'] == 2019] 

    graph_four.append(
          go.Bar(
          x = df.country.tolist(),
          y = df.IMP.tolist(),
          )
        )

    layout_four = dict(title = 'Imports of goods and services in 2019 (USD)',
                    xaxis = dict(title = 'Country',),
                    yaxis = dict(title = 'IMP'),
                    )
    
    # fifth chart plots foreign direct investment over time in USD
    graph_five = []
    df = cleandata('data/API_BX.KLT.DINV.CD.WD_DS2_en_csv_v2_1927091.csv')
    df.columns = ['country','year','FDI']
    df.sort_values('year', ascending=False, inplace=True)
    countrylist = df.country.unique().tolist()

    for country in countrylist:
        x_val = df[df['country'] == country].year.tolist()
        y_val =  df[df['country'] == country].FDI.tolist()
        graph_five.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_five = dict(title = 'Foreign direct investment - 1990 to 2019 (USD)',
                    xaxis = dict(title = 'Year',
                      autotick=False, tick0=1990, dtick=10),
                    yaxis = dict(title = 'F.D.I.'),
                    )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))

    return figures