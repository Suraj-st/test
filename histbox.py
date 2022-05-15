def histogram_boxplot(data, features, figsize=(12,7), kde= False, bins= None ):
    f2, (ax_box2, ax_hist2) = plt.subplots(
    nrows=2,
    sharex = True,
    gridspec_kw={'height_ratios' : (0.25, 0.75)},
    figsize=figsize
    )
    sns.boxplot(
    data = data, x = features, ax = ax_box2, showmeans=True, color="violet"
    )
    sns.histplot(
    data = data, x=features, kde=kde, ax=ax_hist2, bins=bins, palette='winter'
    ) if bins else sns.histplot(
        data = data, x=features, kde=kde, ax=ax_hist2, 
    )
    ax_hist2.axvline(
    data[features].mean(), color="green", linestyle="--"
    )
    ax_hist2.axvline(
    data[features].median(), color='blue', linestyle='-'
    )
