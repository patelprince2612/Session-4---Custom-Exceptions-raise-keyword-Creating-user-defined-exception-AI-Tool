# 1. Create a custom exception class called InvalidCouponCodeError for a Zomato-style food ordering app, and raise this exception if a user tries to apply a coupon code that is not in the list of valid codes.
class InvalidCouponCodeError(Exception):
    pass

def apply_coupon(code):
    valid_codes = ["SAVE20", "ZOMATO50", "WELCOME10"]
    if code not in valid_codes:
        raise InvalidCouponCodeError()
        
    print("Coupon applied successfully")

try:
    apply_coupon("ZOMATO50")
    apply_coupon("INVALID100")
except InvalidCouponCodeError:
    print("Invalid coupon code applied")

# 2. Write a function add_song_to_playlist(song_name, playlist) for a Spotify-like app that raises a SongAlreadyExistsError (custom exception) if the song is already present in the playlist. Hint: Define SongAlreadyExistsError as a user-defined exception class and use the raise keyword inside your function.
class SongAlreadyExistsError(Exception):
    pass

def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError()
    playlist.append(song_name)
    print("Song added to playlist")

my_playlist = ["Shape of You", "Believer"]
try:
    add_song_to_playlist("Perfect", my_playlist)
    add_song_to_playlist("Believer", my_playlist)
except SongAlreadyExistsError:
    print("Song is already in the playlist")

# 3. Simulate a Flipkart-style checkout process where a function process_payment(amount) raises a PaymentFailedError (custom exception) if the amount is less than or equal to zero, and prints 'Payment Successful' otherwise.
class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError()
    print("Payment Successful")

try:
    process_payment(500)
    process_payment(-10)
except PaymentFailedError:
    print("Payment failed due to invalid amount")

# 4. Given the following traceback from a Python program, use ChatGPT to explain in your own words what the error means and how you would fix it: Traceback (most recent call last): File "main.py", line 8, in <module> book_ticket('Avengers', -2) File "main.py", line 4, in book_ticket raise InvalidSeatNumberError('Seat number must be positive') NameError: name 'InvalidSeatNumberError' is not defined
class InvalidSeatNumberError(Exception):
    pass

def book_ticket(movie, seats):
    if seats <= 0:
        raise InvalidSeatNumberError("Seat number must be positive")
    print("Ticket booked successfully")

try:
    book_ticket('Avengers', -2)
except InvalidSeatNumberError as e:
    print(e)