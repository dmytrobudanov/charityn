import pandas as pd

def create_df() -> pd.DataFrame:
    table = {
        "charity_navigator_link":[],
        "title":[],
        "site":[],
        "location":[],
        "ein":[],
        "description":[],
        "rating":[]
    }

    df = pd.DataFrame(table)

    return df

def add_charity_navigator_link(df: pd.DataFrame, link: str | list) -> pd.DataFrame:
    if type(link) is list:
        for l in link:
            df.loc[len(df.index)] = [l, '', '', '', '', '','']
    else:
        df.loc[len(df.index)] = [link, '', '', '', '', '','']
    return df

def add_info(df: pd.DataFrame, row_index: int, data: list) -> pd.DataFrame:
    df.loc[row_index] = data
    return df
