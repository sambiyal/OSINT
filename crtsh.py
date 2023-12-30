import requests
import sys
import argparse

def search_crtsh(domain):
    url = f'https://crt.sh/?q={domain}&output=json'

    # Send GET request to crt.sh
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse JSON response
        results = response.json()

        # Extract and print the results
        return [result['name_value'] for result in results]
    else:
        print(f"Failed to perform crt.sh search. HTTP Status Code: {response.status_code}")
        return None

def save_to_file(output_list, filename):
    with open(filename, 'w') as file:
        for item in output_list:
            file.write(item + '\n')

if __name__ == "__main__":
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Search crt.sh for a domain and optionally save the results to a file.")
    parser.add_argument('domain', metavar='domain', type=str, help='Domain name to search for')
    parser.add_argument('-o', '--output', metavar='filename', type=str, help='Save results to a file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform crt.sh search using direct API call
    search_results = search_crtsh(args.domain)

    if search_results:
        # Print the results
        for result in search_results:
            print(result)

        # Save to a file if the output option is provided
        if args.output:
            save_to_file(search_results, args.output)
            print(f"Results saved to {args.output}")
