Folder dataset contains training and testing set for k=2 and k=4. 
For each dataset the goal is to predict, for each cascade with k nodes, if it will double its size (reaching respectively size 4 and 8).

Each cascade contains a variable number of tweets with the same URL. The content (e.g. text) of all the tweets in a cascade is assumed to be the same (even if the text may be different).
For accessing the content of a cascade, check the file root_tweet.json, which specifies the id of the tweet with the content for each cascade.

You are not required to download any data online, unless you want to design some novel feature (but be aware that dataset was collected in 2010: data online may then be different and many tweets may be missing).

social_network.json contains the social graph of the users: for each user_id a list of followers is provided (Al: [John, Jack] means that Al is a follower of both John and Jack, equivalently John and Jack are followees of Al).

Execute the python file ass2_read_data.py for a simple inspection of two sample cascades. Make sure all the paths in the code are in accord with the local filesystems. 
Please have a look at the code for understanding how to use the dataset.

Further details will be provided in class.
For inquiries, don’t esitate asking me: francesco.gelli@u.nus.edu