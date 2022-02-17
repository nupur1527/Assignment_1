import numpy as np
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import date
import python_mail

data= pd.read_excel(r"C:\Users\nupur\Desktop\SampleData.xlsx")

def modified_data():
    modified_data =[]

    year= str(date.today().year)
    for index, row in data.iterrows():
        given_date= row['Date']+" "+year
        date_format = '%b %d %Y'
        dtObj = dt.datetime.strptime(given_date, date_format)
    
        future_date= dtObj+ relativedelta(months= row['Expected Run'])
    
        print(future_date)
    
        data.loc[index, 'Modified_Date'] = future_date
        modified_data.append({'Date':given_date, 'Expected Run':row['Expected Run'], 'Modified Date': future_date})

    df = pd.DataFrame(modified_data)

    table = df.to_html(sparsify=False, index=False, justify='justify-all', col_space='100px')
    return table


def construct_emailbody():
    HTML = modified_data()
    emailbody = """<!DOCTYPE html>
    <html>
    <body>
    <p>Hello,</p>
    <p>Your module run successfully. Please refer the below table</p>
    """ + HTML + """
    <p>Thanks,<br>Automation Team</p>

    </body>
    </html>
    """
    return emailbody

python_mail.Send_mail(construct_emailbody(), 'tomar.nupur01@gmail.com, aakash.g@motivitylabs.com, shiva.m@motivitylabs.com')
