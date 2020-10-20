sim_matrix = similarity_matrix(littleWomenList, scarletList, signOfFourList,
                                   adventureHolmesList, romeoJulietList, hamletList, othelloList, macbethList, learList, merchantVeniceList, midsummerList)
    S = np.asarray(sim_matrix)
    dissimilarities = 1 - S
    coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)
    plt.scatter(coord[:, 0], coord[:, 1])
    for i in range(coord.shape[0]):
        plt.annotate(str(i), (coord[i, :]))
    plt.show()
