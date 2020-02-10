# imbalance-anomaly-gt
Ground truth data for anomaly detection in imbalance authentication logs.

## Creating a new virtual environment

1. Create a conda virtual environment

   `conda create --name imbalance-anomaly-gt python=3.6`

2. Activate the environment

   `conda activate imbalance-anomaly-gt`

## Extracting the datasets and install the package

1. Clone this repository

   `git clone https://github.com/studiawan/imbalance-anomaly-gt.git`

2. Go to the project directory
    
   `cd imbalance-anomaly-gt`

3. Install this package
   
   `pip install -e .`

4. Extract dfrws-2009 dataset

   `tar -xzvf datasets/dfrws-2009/auth.all.log.tar.gz --directory datasets/dfrws-2009/`

5. Extract Hofstede et al. dataset

   `tar -xzvf datasets/hofstede/auth.all.log.tar.gz --directory datasets/hofstede/`

6. Extract SecRepo dataset

   `tar -xzvf datasets/secrepo/auth.all.log.tar.gz --directory datasets/secrepo/`

## Building the ground truth

1. To build the ground truth, run this command
   
   `python imbalance-anomaly-gt/groundtruth.py $DATASET_NAME$`
   
   Example:
   
   `python imbalance-anomaly-gt/groundtruth.py secrepo`

2. The supported datasets are `dfrws-2009`, `hofstede`, and `secrepo`

3. The ground truth file is `auth.all.pickle` and it is located in directory `datasets/$DATASET_NAME$`

## References

Casey, E.  and Richard III, G. G. (2009). DFRWS Forensic Challenge 2009. http://old.dfrws.org/2009/challenge/index.shtml

Hofstede, R., Hendriks, L., Sperotto, A., and Pras, A. (2014). SSH compromise detection using NetFlow/IPFIX. ACM SIGCOMM Computer Communication Review, 44(5), 20-26.

Sconzo, M. (2020). SecRepo.com: security data samples repository. http://www.secrepo.com/auth.log/auth.log.gz
