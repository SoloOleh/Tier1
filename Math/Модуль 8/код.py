import pandas as pd
url = 'https://docs.google.com/spreadsheets/d/18WCpPS96Tb3cB0FCsIA92PEhcmBkp08sjYhS9DsQfJE/edit#gid=954244094' 
url = url[:url.find('/edit')] + '/export?format=csv'
df = pd.read_csv(url)
