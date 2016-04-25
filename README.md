# Pairwise Kernel Method
##Discription
[Protein–ligand interaction prediction: an improved chemogenomics approach](http://www.ncbi.nlm.nih.gov/pubmed/18676415) 

にて提案されたPairwise Kernel Methodを用いたCompound-Protein Interaction予測手法を実装しました．分類器にはSupport Vector Machineを使っています．ここではデータセットとして九州大学 山西芳裕准教授が以下の論文で作成したものを使用しました．

[Prediction of drug-target interaction networks from the integration of chemical and genomic spaces](http://bioinformatics.oxfordjournals.org/content/24/13/i232.full.pdf+html)

データセットは[こちら](http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/)から無償でダウンロードできます．データセットはGPCR，ion channel，Nuclear Recepter，Enzymeの4種類が利用可能です．

また，link_indicator.pyにてNetworkXで用意されているLink Prediction Argorithmsの拡張機能を提供しています．具体的にはグラフ構造から求められる，ノード間の関係性を示す指標として以下を提供しています．

- Common Neighbor
- Cosine Similarity
- HPI
- HDI
- LHN-1
- Sorensen
- Graph Distance

各指標の定義は[こちら](http://arxiv.org/abs/1010.0725)を参照してください．入力及び出力はNetworkXのLink Prediction Argorithmsに準じています．

These sources provides you the Compound-Protein Interaction tool using Pairwise Kernel Method proposed by [this paper](http://www.ncbi.nlm.nih.gov/pubmed/18676415). Support vector machine is used as classifier. The dataset in this tool is provided by Yoshihiro Yamanishi(Kyusyu unv, JPN). You can download the dataset from [here](http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/) for open and free. There are four kinds of dataset, GPCR，ion channel，Nuclear Recepter and Enzyme.

Furthermore, the extension of networkx's link prediction argorithms is provided in link_indicator.py. I implement indicators that represent the relation between node pair. 

- Common Neighbor
- Cosine Similarity
- HPI
- HDI
- LHN-1
- Sorensen
- Graph Distance

If you want to know these definitions, refer to [this paper](http://arxiv.org/abs/1010.0725). Input and Output forms conform to networkx's link prediction argorithms.

##Usage
実行に際して，以下のpythonライブラリが必要です．

(Required python libraries)

- Numpy
- Scipy
- scilit learn
- NetworkX
- matplotlib

run.pyを実行するとSVMによる学習，10 fold cross-validationによる評価が行われます．用いるデータセットを変更する場合はrun.pyに記載されているパスを変更してください．
評価指標としてAUROC(Area Under ROC Curve)とAUPR(Area Under Precision-Recall Curve)の2種類が使用可能です．
