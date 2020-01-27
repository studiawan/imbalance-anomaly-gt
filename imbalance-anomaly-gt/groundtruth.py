import os
import sys
import pickle
import re
from nltk import corpus
from statistics import mean
from nerlogparser.nerlogparser import Nerlogparser


class GroundTruth(object):
    def __init__(self, dataset):
        self.dataset = dataset
        self.configurations = {}
        self.parser = Nerlogparser()
        self.stopwords = corpus.stopwords.words('english')

    @staticmethod
    def __read_wordlist():
        # read word list of particular log type
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'anomaly-terms'))

        # open word list files in the specified directory
        wordlist_path = os.path.join(current_path, 'auth.txt')
        with open(wordlist_path, 'r') as f:
            wordlist_temp = f.readlines()

        # get word list
        wordlist = []
        for wl in wordlist_temp:
            wordlist.append(wl.strip())

        return wordlist

    def __get_preprocessed_logs(self, log_file):
        # parse log files
        parsed_logs = self.parser.parse_logs(log_file)

        return parsed_logs

    def __preprocess(self, message):
        # split
        message = message.lower()
        message = message.replace('=', ' ')
        message = message.replace('/', ' ')
        message = message.replace('-', ' ')
        line = message.split()

        # get alphabet only
        line_split = []
        for li in line:
            alphabet_only = re.sub('[^a-zA-Z]', '', li)
            if alphabet_only != '':
                line_split.append(alphabet_only)

        # remove word with length only 1 character
        for index, word in enumerate(line_split):
            if len(word) == 1:
                line_split[index] = ''

        # remove stopwords
        preprocessed_message = []
        for word in line_split:
            if word != '':
                if word not in self.stopwords:
                    preprocessed_message.append(word)

        return preprocessed_message

    @staticmethod
    def __set_sentiment_label(wordlist, parsed_logs):
        sentiment_label = {}

        # check sentiment for each log line
        for line_id, parsed in parsed_logs.items():
            log_lower = parsed['message'].lower().strip()

            # 0 = negative
            # 1 = positive
            label = 1
            for word in wordlist:
                # negative sentiment
                if word in log_lower:
                    label = 0
                    sentiment_label[line_id] = label
                    break

            # positive sentiment
            if label == 1:
                sentiment_label[line_id] = label
                # print(log_lower)

        return sentiment_label

    def __save_groundtruth(self, groundtruth):
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datasets', self.dataset))
        groundtruth_file = os.path.join(current_path, 'auth.all.pickle')
        with open(groundtruth_file, 'wb') as handle:
            pickle.dump(groundtruth, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def __min_max_mean(message_length):
        min_length = min(message_length)
        max_length = max(message_length)
        mean_length = mean(message_length)

        print(min_length, max_length, mean_length)

    def get_ground_truth(self):
        # get log file
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datasets', self.dataset))
        log_file = os.path.join(current_path, 'auth.all.log')

        # log parsing
        parsed_logs = self.__get_preprocessed_logs(log_file)

        # set label for each line in a log file
        wordlist = self.__read_wordlist()
        print('\nProcessing', log_file, '...')

        # get label
        anomaly_label = self.__set_sentiment_label(wordlist, parsed_logs)

        groundtruth = {}
        message_length = []
        for line_id, label in anomaly_label.items():
            preprocessed_message = self.__preprocess(parsed_logs[line_id]['message'])
            message_length.append(len(preprocessed_message))

            groundtruth[line_id] = {
                'message': preprocessed_message,
                'label': label
            }

        # save ground truth
        self.__save_groundtruth(groundtruth)

        # check min max mean of message length
        self.__min_max_mean(message_length)


if __name__ == '__main__':
    dataset_list = ['dfrws-2009', 'hofstede', 'secrepo']
    if len(sys.argv) < 2:
        print('Please input dataset name.')
        print('python groundtruth.py dataset_name ')
        print('Supported datasets:', dataset_list)
        sys.exit(1)

    else:
        dataset_name = sys.argv[1]
        gt = GroundTruth(dataset_name)
        gt.get_ground_truth()
