#! Python 2.7.12

import psycopg2


DBNAME = "news"


def most_popular():
    database = psycopg2.connect(database=DBNAME)
    command = database.cursor()
    command.execute("select title, count(path) \
    from log, articles \
    where log.path like '%' || articles.slug || '%' \
    group by title \
    order by count(path) desc \
    limit 3;")
    most_popular_articles = command.fetchall()
    for article in most_popular_articles:
        print(str(article[0]) + ' - ' + str(article[1]) + ' views\n')
    database.close()


def most_popular_author():
    database = psycopg2.connect(database=DBNAME)
    command = database.cursor()
    command.execute("select name, count(path) from log, articles, authors \
    where log.path like '%' || articles.slug || '%' \
    and articles.author = authors.id \
    group by name \
    order by count(path) desc;")
    most_popular_authors = command.fetchall()
    for author in most_popular_authors:
        print(str(author[0]) + ' - ' + str(author[1]) + ' views\n')
    database.close()


def error_days():
    database = psycopg2.connect(database=DBNAME)
    command = database.cursor()
    command.execute("select date, errorcount*100.00/total as percentage_error \
    from (select cast(time as date) as Date, count(time) as Total, \
    sum(case when status = '200 OK' then 0 else 1 end) ErrorCount \
    from log \
    group by cast(time as date)) as errorcalculator \
    where errorcount*100/total > 1;")
    worst_error_days = command.fetchall()
    for days in worst_error_days:
        date = str(days[0]).split('-')
        day = date[2]
        if day[-1] == '1':
            day += 'st'
        if day[-1] == '2':
            day += 'nd'
        if day[-1] == '3':
            day += 'rd'
        else:
            day += 'th'
        month_dictionary = {'01': 'January', '02': 'February', '03': 'March',
                            '04': 'April', '05': 'May', '06': 'June',
                            '07': 'July', '08': 'August', '09': 'September',
                            '10': 'October', '11': 'November',
                            '12': 'December'}
        month = date[1]
        month = month_dictionary[month]
        year = date[0]
        properly_formatted_date = month + ' ' + day + ' , ' + year
        percentage_error = str(days[1])[:3] + "%" + " errors"
        print(properly_formatted_date + ' - ' + percentage_error)
    database.close()


print('1. What are the most popular three articles of all time?\n\n')
print(most_popular())
print('\n2. Who are the most popular article authors of all time?\n\n')
print(most_popular_author())
print('\n3. On which days did more than 1% of requests lead to errors?\n\n')
print(error_days())
