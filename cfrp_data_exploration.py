import csv

output = "cfrp_timeline_output.csv"


with open("RCF - Plays.csv", 'r') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    play_details = {}
    for _, author, title, genre, _, _, _, acts, _, _, _, _, _, _, date in reader:
        play_details[title] = {'title': title, 'author': author,
                               'genre': genre, 'date': date, 'acts': acts}

with open('RCF - Ticket_Sales.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    ticket_sales = {}
    venue_name = {}
    for _, _, name, title, _, _, _, total_sold in reader:
        ticket_sales[title] = ticket_sales.get(title, 0) + int(total_sold)
        venue_name[title] = name

with open(output, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Year', 'Month', 'Day', 'Time', 'End Year', 'End Month',
                     'End Day', 'End Time', 'Display Date', 'Headline', 'Text',
                     'Media', 'Media Credit', 'Media Caption', 'Media'
                     'Thumbnail', 'Type', 'Group', 'Background'])
    seen = set()
    for play in play_details.itervalues():
        date = play['date']
        headline = play['title']
        if date != '' and headline not in seen:
            year, month, day = date.split('-')
            acts = play['acts'] if play['acts'] != '' else 'Unknown'
            tickets_sold = 'Unknown'
            name = 'Unknown'
            background = ''
            if headline in ticket_sales:
                tickets_sold = ticket_sales[headline]
                name = venue_name[headline]
                if tickets_sold < 5000:
                    background = '#F7BABE'
                elif tickets_sold < 15000:
                    background = '#F77C84'
                else:
                    background = '#F51625'
            text = headline + ' was written by ' + play['author'] + ' in ' + date + '. It has ' + acts + \
                   ' acts, sold a total of ' + str(tickets_sold) + ' tickets and was performed in ' + name + '.'
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
            seen.add(headline)
            writer.writerow([year, month, day, '', year, month, day, '', date,
                             headline, text, media, '', genre, media, '', '', background])  


