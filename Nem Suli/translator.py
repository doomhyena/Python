import pandas as pd
from googletrans import Translator

file_path = "vocabulary.xlsx"
df = pd.read_excel(file_path)

english_column = 'Angol' 

translator = Translator()

df['Magyar'] = df[english_column].apply(lambda x: translator.translate(x, src='en', dest='hu').text)

output_file = "translated_excel_file.xlsx"
df.to_excel(output_file, index=False)

print(f"A fordított fájl elmentve: {output_file}")
