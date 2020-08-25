from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Something Super Awesome At Root Level!'


@app.route('/<int:number>')
def display_in_order_integers(number):
	starting_number = 1
	ending_number = number + 1

	consequtive_integers = [str(n) for n in range(starting_number, ending_number)]
	result = ' '.join(consequtive_integers)
	return result


@app.route('/<int:number>/odd')
def display_odd_numbers(number):
	starting_number = 1
	ending_number = number + 1

	odd_integers = [str(n) for n in range(starting_number, ending_number, 2)]
	result = ' '.join(odd_integers)
	return result

@app.route('/<int:number>/even')
def display_even_numbers(number):
	starting_number = 2
	ending_number = number + 1

	even_integers = [str(n) for n in range(starting_number, ending_number, 2)]
	result = ' '.join(even_integers)
	return result


@app.route('/<int:number>/prime')
def prime_numbers(number):
	starting_number = 1
	ending_number = number + 1
	result = ''

	if number < 3:
		result  = '2'
		return result

	else:
		numbers_range = [True for n in range(starting_number, ending_number)]
		numbers_range[0] = False

		for n in range(2, ending_number):
			if numbers_range[n-1] == True:
				result += str(n) + ' '

				for m in range(n, ending_number, n):
					numbers_range[m-1] = False

	return result


if __name__ == '__main__':
	app.run()
