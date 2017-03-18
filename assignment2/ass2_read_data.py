import json


def read_data(tr_path, ts_path):
    with open(tr_path, 'r') as f:
        tr_data = json.load(f)
    with open(ts_path, 'r') as f:
        ts_data = json.load(f)
    return tr_data, ts_data


def inspect_data(dataset, tw_info_file):
    with open(tw_info_file, 'r') as f:
        tw_info = json.load(f)

    # Inspecting two random urls
    example_urls = ['http://de.tk/z4ux9', 'http://tinyurl.com/2flgbxw']
    for url in example_urls:
        cascade = dataset[url]
        tw_id = tw_info[url]

        # This is how you access the content of the cascade:
        with open('tweets/'+tw_id+'.json', 'r') as f:
            tw_content = json.load(f)

        # Printing some info about the cascade
        print 'CASCADE:', url, '| NUM OF TWEETS:', len(cascade), '| CONTENT:', tw_content['text']
    return


'Return the integer id of the root of the cascade (because 1 sometimes may be missing)'
def find_root_of_cascade(cascade):
    tweets = cascade.keys()
    return str(sorted(map(int, tweets))[0])


'''Extract the number of followees of the root of the tree'''
def extract_example_features(dataset, network):
    example_urls = ['http://de.tk/z4ux9', 'http://tinyurl.com/2flgbxw']
    for url in example_urls:
        cascade = dataset[url]
        root = find_root_of_cascade(cascade)
        number_of_followees = len(network[cascade[root]['user']])
        print 'NUMBER OF FOLLOWEES OF ROOT FOR CASCADE', url, 'IS:', number_of_followees
    return number_of_followees


def read_social_network(input_path):
    with open(input_path, 'r') as f:
        return json.load(f)


'''Get the label viral/non-viral (True or False) for a cascade.'''
def get_label(cascade, k):
    return len(cascade) >= 2*k

def extract_labels(dataset, k):
    example_urls = ['http://de.tk/z4ux9', 'http://tinyurl.com/2flgbxw']
    labels = [get_label(dataset[url], k) for url in example_urls]
    print 'LABELS FOR THE SAMPLE CASCADES ARE: ', labels
    return


if __name__ == '__main__':
    tr, ts = read_data('dataset/k4/training.json', 'dataset/k4/testing.json')
    inspect_data(tr, 'dataset/k4/root_tweet.json')
    social_network = read_social_network('social_network.json')
    ft = extract_example_features(tr, social_network)
    tr_labels = extract_labels(tr, 4)
