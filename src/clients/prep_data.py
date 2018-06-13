import pandas as pd

extensions = ['user.csv', 'posts.csv', 'server.csv', 'userinfo.csv']

out_files = [open('./Tests/results/{}'.format(extension), 'wb') for extension in extensions]

dfs = [pd.read_csv('Tests/results/data/{}'.format(extension)) for extension in extensions]

for i in range(1, 7):
    for j, df in enumerate(dfs):
        new_df = pd.read_csv('Tests/results/data{}/{}'.format(i, extensions[j]))
        df = df.append(new_df)
        if i is not 6:
            new_df = pd.read_csv('c:/proj/data{}/{}'.format(i, extensions[j]))
            df = df.append(new_df)
        dfs[j] = df

groupbys = [df.groupby(['num_logs_to_init', 'threshold']).mean() for df in dfs]

groupbys = [group.add_suffix('_Avg').reset_index() for group in groupbys]

for df in groupbys:
    df['ratio_Avg'] = df['total transactions_Avg'] / df['total saved logs_Avg']
    df['ratio after initialization_Avg'] = df['total transactions after initialization_Avg'] / df['total saved logs after initialization_Avg']


for i, group in enumerate(groupbys):
    group.to_csv('./Tests/results/{}'.format(extensions[i]), index=False)
    out_files[i].close()
