# Pairwise Kernel Method
##Discription
[Protein–ligand interaction prediction: an improved chemogenomics approach](http://www.ncbi.nlm.nih.gov/pubmed/18676415) 

にて提案されたPairwise Kernel Methodを用いたCompound-Protein Interaction予測手法を実装しました．分類器にはSupport Vector Machineを使っています．ここではデータセットとして九州大学 山西芳裕准教授が以下の論文で作成したものを使用しました．

[Prediction of drug-target interaction networks from the integration of chemical and genomic spaces](http://bioinformatics.oxfordjournals.org/content/24/13/i232.full.pdf+html)

データセットは[こちら](http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/)から無償でダウンロードできます．データセットはGPCR，ion channel，Nuclear Recepter，Enzymeの4種類が利用可能です．

##Usage
実行に際して，以下のpythonライブラリが必要です．

- Numpy
- Scipy
- scilit learn
- NetworkX
- matplotlib

run.pyを実行するとSVMによる学習，10 fold cross-validationによる評価が行われます．用いるデータセットを変更する場合はrun.pyに記載されているパスを変更してください．
評価指標としてAUROC(Area Under ROC Curve)とAUPR(Area Under Precision-Recall Curve)の2種類が使用可能です．
