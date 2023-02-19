import flexclust
from flexclust import data
data(vacmot, package="flexclust")
with open("vacmot-clusters.RData", "rb") as f:
    vacmot_clusters = pickle.load(f)



from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import ward, dendrogram

vacmot_vdist = pdist(vacmot.T)
vacmot_vclust = ward(vacmot_vdist)



import matplotlib.pyplot as plt

# assuming vacmot.k6 is a vector of cluster assignments
# and vacmot.vclust is a hierarchical clustering object
# with the order of the leaves as vacmot.vclust.order
order = vacmot_vclust.order[::-1]
barchart_data = vacmot_k6
plt.bar(range(len(barchart_data)), barchart_data[order], color='gray')
plt.xticks(range(len(barchart_data)), order)
plt.show()


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

vacmot_pca = PCA().fit_transform(vacmot)
plt.scatter(vacmot_pca[:, 1], vacmot_pca[:, 2], c=vacmot_k6)
plt.xlabel("principal component 2")
plt.ylabel("principal component 3")
plt.colorbar()
plt.show()

# projAxes() is a custom function that
# shows the principal axes of the PCA
projAxes(vacmot_pca, which=[1, 2])

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# vacmot.k6 is a vector of cluster assignments
# and vacmot.pca is a PCA object
# with the transformed data in vacmot_pca
vacmot_pca = vacmot_pca[:, [1, 2]]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
for i in range(6):
    idx = vacmot_k6 == i + 1
    plt.scatter(vacmot_pca[idx, 0], vacmot_pca[idx, 1], color=colors[i], alpha=0.5)
    hull = ConvexHull(vacmot_pca[idx, :])
    plt.fill(vacmot_pca[idx, 0][hull.vertices], vacmot_pca[idx, 1][hull.vertices], color=colors[i], alpha=0.2)
plt.xlabel("principal component 2")
plt.ylabel("principal component 3")
plt.show()

# projAxes() is a custom function that
# shows the principal axes of the PCA
projAxes(vacmot_pca, which=[1, 2], col='darkblue', cex=1.2)