import pandas as pd
from datasets import load_dataset, Dataset

# Load the CSV file
csv_file_path = "faq.csv"
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')


def format_row(row):
    return f"<s>[INST] {row['question']} [/INST] {row['answer']} </s>"


df['text'] = df.apply(format_row, axis=1)


df = df[['text']]

# Save the new DataFrame to a CSV file
formatted_csv_file_path = "formatted_faq.csv"
df.to_csv(formatted_csv_file_path, index=False)

# Step 2: Load the Formatted CSV File as a Dataset and Push to Hugging Face


dataset = load_dataset('csv', data_files=formatted_csv_file_path)

# Push the dataset to Hugging Face
dataset_repo = "dhruvbhatia1/bank-faqs"

dataset.push_to_hub(dataset_repo, private=False)
