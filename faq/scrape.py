import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://retail.onlinesbi.sbi/npersonal/faq.html'

# Send a GET request to the webpage
response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')


faq_list = soup.find('ol')


questions = []
answers = []


for item in faq_list.find_all('li'):

    question_element = item.find('p', class_='faqQues')

    if question_element:
        question = question_element.text.strip()
    else:
        continue  


    answer_element = item.find_all('p')
    

    if len(answer_element) > 1:
        answer = answer_element[1].text.strip()
    else:
        continue  


    questions.append(question)
    answers.append(answer)

# Create a DataFrame from the lists
faq_df = pd.DataFrame({
    'Question': questions,
    'Answer': answers
})

# Save the DataFrame to a CSV file
faq_df.to_csv('faq.csv', index=False)

print('FAQ data has been saved to faq.csv')
