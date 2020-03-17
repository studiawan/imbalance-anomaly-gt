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

4. Extract casper-rw dataset

   `tar -xzvf datasets/casper-rw/all.log.tar.gz --directory datasets/casper-rw/`

5. Extract dfrws-2009 dataset

   `tar -xzvf datasets/dfrws-2009/all.log.tar.gz --directory datasets/dfrws-2009/`

6. Extract honeynet-challenge7 dataset

   `tar -xzvf datasets/honeynet-challenge7/all.log.tar.gz --directory datasets/honeynet-challenge7/`

## Building the ground truth

1. To build the ground truth, run this command
   
   `python imbalance-anomaly-gt/groundtruth.py $DATASET_NAME$`
   
   Example:
   
   `python imbalance-anomaly-gt/groundtruth.py dfrws-2009`

2. The supported datasets are `casper-rw`, `dfrws-2009`, and `honeynet-challenge7`

3. The ground truth file is `log.all.pickle` and it is located in directory `datasets/$DATASET_NAME$`

## References

Garfinkel, S.: nps-2009-casper-rw: An ext3 file system from a bootable USB (2009), http://downloads.digitalcorpora.org/corpora/drives/nps-2009-casper-rw/

Casey, E., Richard III, G.G.: DFRWS Forensic Challenge 2009 (2009), http://old.dfrws.org/2009/challenge/index.shtml

Arcas, G., Gonzales, H., Cheng, J.: Challenge 7 of the Honeynet Project Forensic Challenge 2011 - Forensic analysis of a compromised server (2011), https://old.honeynet.org/challenges/2011_7_compromised_server
