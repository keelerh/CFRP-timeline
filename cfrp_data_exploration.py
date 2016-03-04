import csv

filename = "RCF - Plays.csv"
output = "cfrp_timeline_output.csv"

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    play_details = {}
    for _, author, title, genre, _, _, _, _, _, _, _, _, _, _, date in reader:
        play_details[title] = {'title': title, 'author': author,
                               'genre': genre, 'date': date}
    # print play_details

with open(output, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Year', 'Month', 'Day', 'Time', 'End Year', 'End Month',
                     'End Day', 'End Time', 'Display Date', 'Headline', 'Text',
                     'Media', 'Media Credit', 'Media Caption', 'Media'
                     'Thumbnail', 'Type', 'Group', 'Background'])
    for play in play_details.itervalues():
        date = play['date']
        if date != '':
            year, month, day = date.split('-')
            headline = play['title']
            text = play['author']
            genre = play['genre']
            if genre == 'com\xc3\xa9die':
                media = 'http://i.f1g.fr/media/figaro/805x453_crop/2015/06/' \
                        '11/XVM3aa11084-1025-11e5-993b-13c3811e2e5c.jpg'
            elif genre == 'trag\xc3\xa9die':
                media = 'http://www.culturekiosque.com/images66/victor_hugo_' \
                        'lecretia1_borgia.jpg'
            else:
                media = 'http://culturebox.francetvinfo.fr/sites/default/files' \
                        '/assets/images/2015/02/estivants_2.jpg'
            writer.writerow([year, month, day, '', year, month, day, '', date,
                             headline, text, media, '', genre, media, '', '', ''])  