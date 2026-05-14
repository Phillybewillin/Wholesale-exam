from sklearn.decomposition import PCA

def apply_pca(data, n_components=2):
    """
    Apply PCA to reduce dimensionality of the data.
    Returns the transformed data and the explained variance ratio.
    """
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)
    explained_variance = pca.explained_variance_ratio_
    
    return transformed_data, explained_variance
