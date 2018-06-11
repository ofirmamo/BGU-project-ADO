import pandas as pd

extensions = ['user.csv', 'posts.csv', 'server.csv', 'userinfo.csv']

dfs = [pd.read_csv('../server/app/data/{}'.format(extension)) for extension in extensions]

groupbys = [df.groupby(['num_logs_to_init', 'threshold', 'total injected']).mean() for df in dfs]

groupbys = [group.add_suffix('_Avg').reset_index() for group in groupbys]

out_files = [open('./Tests/results/{}'.format(extension), 'wb') for extension in extensions]

for i, group in enumerate(groupbys):
    group.to_csv('./Tests/results/{}'.format(extensions[i]), index=False)
    out_files[i].close()
