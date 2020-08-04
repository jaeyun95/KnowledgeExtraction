## This is knowledge extraction system


# 1.Generation Knowledge DataBase
This is generate Knowledge DataBase. Link is [Here](https://github.com/jaeyun95/KnowledgeExtraction/tree/master/generationDB)

# 2.Setting up Environment
```
wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
conda update -n base -c defaults conda
conda create --name kes python=3.6
source activate kes

conda install numpy h5py nltk pymongo transformers

conda install pytorch cudatoolkit=9.0 -c pytorch
pip install git+git://github.com/pytorch/vision.git@24577864e92b72f7066e1ed16e978e873e19d13d
```