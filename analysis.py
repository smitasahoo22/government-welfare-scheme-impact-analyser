def basic_stats(df):
    return {
        "total_states": df['State'].nunique(),
        "total_districts": df['District'].nunique(),
        "total_workers": df['Total Workers'].sum(),
        "total_expenditure": df['Total Expenditure'].sum()
    }


def top_states_by_employment(df):
    return df.groupby('State')['Persondays Generated'].sum().sort_values(ascending=False).head(10)


def women_participation(df):    
    if 'Women Persondays' in df.columns:
        return df.groupby('State')['Women Persondays'].sum().sort_values(ascending=False)
    else:
        return None