# TYPEFACE_TEST

Question1:

Given an input black & white image. Return bounding boxes of all isolated white patches in the images.

Input: A MxN matrix with 0 & 1s. 0s indicating black pixel and 1 indicating white pixel
Output: List of bounding boxes of white patches where each bounding box is represented using 4 numbers (centerX, centerY, width & height). [[8, 8, 3, 3], [16, 15, 4, 4]
Sample image1: https://cortex6-my.sharepoint.com/:i:/g/personal/kishoreb_typeface_ai/Ed_aqlVwoqpIjELK4L8cAPEB5nJ72tlhTTeXIz1N7IJxgA?e=3hA5lp
has 2 isolated white patches
Sample image2: https://cortex6-my.sharepoint.com/:i:/g/personal/kishoreb_typeface_ai/EcCu_ueplYVOt5o2wdcSko4BILGU4MHrxZQ7B6wRKwxr9Q?e=T2GAnP
has 1 isolated withe patch

Question2:

Write an algorithm to search for all phonetic combinations of a given word in the given file. For example, if the search string is "Murthy" output should contain all combinations like "Moorthy", "Moorthi", "Murthi" etc., Phonetic match is where the English characters sound like input character sound.

Input: A string to search for phonetic combinations, A file with all the available words in the 
output: List of phonetically matching strings to input strings

Question3:

Design a datastore to save monitoring data of a service. Assume the service has 100 APIs and there are 1000 users who are roughly making 1 million requests per day. Some of the sample queries that will be performed on this datastore

- Get the API with maximum average response time across the users.
- Get the API with maximum average response time for each user.
- Get error percentage of each API in buckets of 1 hours for 24 hours.
