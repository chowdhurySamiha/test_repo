import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Mantamonis_bacterial_contamination_analysis.xlsx')
counts = df['Preliminary Verdict:'].value_counts()

plt.figure(figsize=(8,6))
counts.plot(kind='bar')
plt.title('Preliminary Verdict Counts')
plt.xlabel('Verdict')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('preliminary_classification.png')

