"""
Generates Euler Harmonies from lists of prime numbers.
"""
import argparse
from pythonosc import udp_client
import custom_combinations

def get_factors(integer):
    # returns factor list of integer
    factors = []
    for i in range(1, integer+1):
        if integer % i == 0:
            factors.append(i)
    return factors

def convert_to_freqs(fundamental, harmonics_list):
    freq_list = []
    for i in harmonics_list:
        freq = i * fundamental
        if freq > 22000:
            freq = 0
        freq_list.append(freq)
    if len(freq_list) < 30:
        trailing_zeros = 30 - len(freq_list)
        for zero in range(trailing_zeros):
            freq_list.append(0)
    return freq_list

PORT = 7401

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=PORT,
        help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)

while True:
    print("Get Euler Harmonies")
    print("1. through factoring a number. 2. entering custom prime list. 'q' "
          "to quit")
    user_selection = input()
    if user_selection == '1':
        user_number = input('Enter integer to be factored: ')
        prime_list = get_factors(int(user_number))
    elif user_selection == '2':
        user_list = input('Enter primes with no separators: ')
        prime_list = [int(i) for i in user_list]
    elif user_selection == 'q':
        break
    print('Your list:', prime_list)

    all_combinations = custom_combinations.make_all_combinations(prime_list)
    euler_harmonies = custom_combinations.multiply_combinations(
        all_combinations,
        return_set=True)

    print('Euler harmonies: ', euler_harmonies)

    fundamental = int(input('Enter fundamental frequency for Hz conversion: '))
    freq_list = convert_to_freqs(fundamental, euler_harmonies)
    print('Frequencies:', freq_list)
    client.send_message('length', len(freq_list))
    client.send_message("freqs", freq_list)

    input()