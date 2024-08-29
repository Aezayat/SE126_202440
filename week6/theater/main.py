def show_seating_chart(seating_arrangement):
    print("    A B C D E F G H   J K L M N O P Q R S T U V   X Y Z AA AB AC AD AE AF")
    for row_number, row in enumerate(seating_arrangement):
        seats = [seat for seat in row]
        print(f"Row {row_number + 1:2d}: {' '.join(seats[:8])}   {' '.join(seats[8:21])}   {' '.join(seats[21:])}")


def create_seating_plan(total_rows=15, total_columns=30):
    return [['#' for _ in range(total_columns)] for _ in range(total_rows)]


def translate_seat_code(seat_code):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(seat_code) == 1:  # Single-letter seat
        return alphabet.index(seat_code), 0
    elif len(seat_code) == 2:  # Two-letter seat
        first_char, second_char = seat_code[0], seat_code[1]
        if first_char in alphabet and second_char in alphabet:
            return alphabet.index(first_char), alphabet.index(second_char)
    return None, None


def book_seat(seating_arrangement, row_idx, seat_idx):
    if seating_arrangement[row_idx][seat_idx] == '#':
        seating_arrangement[row_idx][seat_idx] = '*'
        print("Reservation confirmed!")
    else:
        print("Seat already taken!")


# Main program loop
user_action = ""
seating_arrangement = create_seating_plan()  # Create the seating arrangement at the beginning

while user_action != 'exit':
    show_seating_chart(seating_arrangement)
    user_action = input("\nEnter 'book' to reserve a seat, 'exit' to quit: ").lower()

    if user_action == 'book':
        try:
            row_idx = int(input("Enter row number (1-15): ")) - 1
            seat_code = input("Enter seat code (e.g., A, B, ..., AE): ").upper()
            seat_column, seat_row = translate_seat_code(seat_code)

            if seat_row is not None and 0 <= row_idx < 15 and 0 <= seat_column < 30:
                book_seat(seating_arrangement, row_idx, seat_column)
            else:
                print("Invalid row or seat code!")
        except (ValueError, IndexError):
            print("Error with your input. Please try again.")
    elif user_action != 'exit':
        print("Invalid option!")

print("Thank you for using the seat reservation system!")