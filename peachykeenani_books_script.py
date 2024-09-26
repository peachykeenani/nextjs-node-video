# list of dictionaries of books with authors, titles, and page count
books = [
	{
	    'author': 'George Orwell',
	    'book': '1984',
	    'page_count': 328,
	},
	{
	    'author': 'Leo Tolstoy',
	    'book': 'War and Peace',
	    'page_count': 1225,
	},
	{
	    'author': 'Ralph Ellison',
	    'book': 'Invisible Man',
	    'page_count': 624,
	},
	{
	    'author': 'Antoine de Saint-Exupéry',
	    'book': 'The little Prince',
	    'page_count': 96,
	},
]

# calculate the total number of pages in these books
counter = 0

for listing in books:
	counter += listing['page_count']
print(f'there are {counter} pages combined in all the books')