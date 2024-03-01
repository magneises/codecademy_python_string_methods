highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# exercise 1
print(highlighted_poems)

# exercise 2
highlighted_poems_list = highlighted_poems.split(',')

# exercise 3
print(highlighted_poems_list)

# exercise 4
highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())


# exercise 5
print(highlighted_poems_stripped)


# exercise 6
highlighted_poems_details = []

# exercise 7
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

# exercise 8
titles = []
poets = []
dates = []

# exercise 9
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
# exercise 10
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))







