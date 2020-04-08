import numpy as np
import pandas as pd
import webbrowser

df = []
df.append(dict(date='2016-04-02', sleep=7.3, calories=3600))
df.append(dict(date='2016-04-03', sleep=7.3, calories=3500))
df = pd.DataFrame(df)

np.random.seed(6182018)
demo_df = pd.DataFrame({'date': np.random.choice(pd.date_range('2018-01-01', '2018-06-18', freq='D'), 2),
                        'analysis_tool': np.random.choice(['pandas', 'r', 'julia', 'sas', 'stata', 'spss'],2),              
                        'database': np.random.choice(['postgres', 'mysql', 'sqlite', 'oracle', 'sql server', 'db2'],2), 
                        'os': np.random.choice(['windows 10', 'ubuntu', 'mac os', 'android', 'ios', 'windows 7', 'debian'],2), 
                        'num1': np.random.randn(2)*100,
                        'num2': np.random.uniform(0,1,2),                   
                        'num3': np.random.randint(100, size=2),
                        'bool': np.random.choice([True, False], 2)
                       },
                        columns=['date', 'analysis_tool', 'num1', 'database', 'num2', 'os', 'num3', 'bool']
          )
#np.random.seed(6018)
demo_df3 = pd.DataFrame({'date': np.random.choice(pd.date_range('2018-01-01', '2018-06-18', freq='D'), 2),
                        'analysis_tool': np.random.choice(['pandas', 'r', 'julia', 'sas', 'stata', 'spss'],2),              
                        'database': np.random.choice(['postgres', 'mysql', 'sqlite', 'oracle', 'sql server', 'db2'],2), 
                        'os': np.random.choice(['windows 10', 'ubuntu', 'mac os', 'android', 'ios', 'windows 7', 'debian'],2), 
                        'num1': np.random.randn(2)*100,
                        'num2': np.random.uniform(0,1,2),                   
                        'num3': np.random.randint(100, size=2),
                        'bool': np.random.choice([True, False], 2)
                       },
                        columns=['date', 'analysis_tool', 'num1', 'database', 'num2', 'os', 'num3', 'bool']
          )
df_merge = [demo_df3, demo_df]
demo_df2 = pd.concat(df_merge, sort=False).sort_index().reset_index()
htstr = """
<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style type="text/css">
        body,
        html {
            height: 100%;
        }
        body {
            background: #8360c3;
            background-image: linear-gradient(-45deg, #5433ff, #20bdff, #a5fecb);
         } 
        th,
        td {
            text-align: left;
            /*background-color: rgb(235, 243, 235); */
            border: 1px solid rgb(7, 7, 7);
        }

        thead {
            padding-top: 12px;
            background-color: #278bdc;
            color: white;
        }
        table.dataframe {
            padding-top: 50px;
            padding-bottom: 50px;
        }
        div.card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
            text-align: center;
        }
    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> -->

</head>

<body>

    <div class="container" style="padding-top: 100px;">
        <div class="card panel panel-default"> 
"""
footer = """ </div>
    </div>

</body>

</html>"""

def highlight_diff_header(s):
    color = ['background-color: #fff' if i%2 == 0 else 'background-color: #f2f2f2' for i in range(0, len(s))]
    row = 1
    while row <= len(s):
        if s[row] != s[row-1]:
            color[row] = 'background-color: #f47f7f'
        row += 2
    return color

s = df.style.apply(highlight_diff_header) \
    .set_table_attributes('class="dataframe table table-hover table-bordered"') \
    .hide_index()
s2 = demo_df.style.apply(highlight_diff_header) \
    .set_table_attributes('class="dataframe table table-hover table-bordered"') \
    .hide_index()
s3 = demo_df2.style.apply(highlight_diff_header) \
    .set_table_attributes('class="dataframe table table-hover table-bordered"') \
    .hide_index()

#ht = df.to_html()
with open('file.html', 'w') as f:
    f.write(htstr + s3.render() + footer)
    #f.write(htstr + df.to_html(classes=['table table-bordered table-hover']) + footer)
webbrowser.open_new('file.html')
