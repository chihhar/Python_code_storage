from PIL import Image
from sklearn import cluster
import matplotlib.pyplot as plt
cluster_K=8
def main():
  #濃淡画像の読みこみ
  pil_im = Image.open("/content/test.png").convert("L")
  #画像から画素値のデータを取り出す
  img = np.array(Image.open("/content/test.png").convert("L"),"f")
  img_vector=img.reshape(-1)
  img_vector=img_vector.reshape(img_vector.shape[0],1)
  #• 取り出した画素値のデータをK個のクラスタにクラスタリング(入力)
  k_means = cluster.KMeans(n_clusters=cluster_K)
  k_means.fit(img_vector)
  #• ある画素値がどのクラスタに属するか調べて，自分の画素値を，そのクラスタ中心の画素値に置き換える
  k_mean_posterization=(Image.fromarray((k_means.cluster_centers_[k_means.labels_]).reshape(pil_im.height, pil_im.weight))).convert("L")
  #結果の表示
  k_mean_posterization.show()
  #結果の保存
  k_mean_posterization.save(str(cluster_K)+"cluster_test.jpg")
if __name__ == "__main__":
  main()
