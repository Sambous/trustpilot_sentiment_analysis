import pandas as pd
import numpy as np
from textblob import TextBlob

def get_polarity(text):
    blob = TextBlob(text)
    return blob.polarity

def extract_stars(stars_url):
    print(stars_url)
    pass

def extract_review_data(review_data):
    total_polarities = np.empty((0, 2), int)

    for review_entry in review_data:
        polarity_entry = np.array([[get_polarity(review_entry[0]),
                          get_polarity(str(review_entry[1])),
                          ]])
        extract_stars(review_entry[2])
        total_polarities = np.append(total_polarities, polarity_entry, axis=0)

    return total_polarities


def main():
    work_sheet = pd.read_excel('trustpilot_data.xlsx')
    total_polarities = extract_review_data(np.array(work_sheet))
    title_polarites = total_polarities[:, [0]]
    review_polarites = total_polarities[:, [1]]
    avg_title_polarities = np.average(title_polarites)
    avg_review_polarities = np.average(review_polarites)

    print(avg_title_polarities, avg_review_polarities)

if __name__ == '__main__':
    main()
