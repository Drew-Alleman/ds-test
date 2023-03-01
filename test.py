import os
import random
import argparse
from faker import Faker

faker = Faker()

data_types = [
    ('email', 5),
    ('credit_card', 5),
    ('mac_address', 5),
    ('ip_address', 5),
    ('ipv6_address', 5),
    ('computer_login', 5),
    ('dns_name', 5),
    ('dns_srv', 5),
    ('text', 60),
]

def generate_srv_dns():
    priority = random.randint(0, 100)
    weight = random.randint(0, 100)
    port = random.randint(0, 65535)
    target = faker.domain_name()
    return f"_service._proto IN SRV {priority} {weight} {port} {target}"

def generate_message(data_type):
    if data_type == 'email':
        return faker.email()
    elif data_type == 'credit_card':
        return faker.credit_card_number()
    elif data_type == 'mac_address':
        return faker.mac_address()
    elif data_type == 'ip_address':
        return faker.ipv4()
    elif data_type == 'ipv6_address':
        return faker.ipv6()
    elif data_type == 'computer_login':
        username = faker.first_name()
        if random.choice([True, False]):
            username += "." + faker.last_name()
        return f"{username}@{faker.domain_name()}"
    elif data_type == 'dns_name':
        return faker.domain_name()   
    elif data_type == 'dns_srv':
        return generate_srv_dns()
    elif data_type == 'text':
        return faker.text() * 500

def generate_test_file(output, size, speed):
    total_file_size = size * 1024
    print(f"[*] Generating a {size}GB test file called '{output}'")
    with open(output, 'w') as f:
        file_size_mb = 0
        while file_size_mb < total_file_size:
            data_type = random.choices(*zip(*data_types))[0]
            message = generate_message(data_type) + '\n'
            f.write(message)
            file_size_mb = os.path.getsize(output) / (1024*1024)
            if file_size_mb >= speed:
                f.flush()
    print(f"[*] Created: '{output}' with a size of: {file_size_mb}MB")

def main():
    parser = argparse.ArgumentParser(description="DataSurgeon Test File Generator")
    parser.add_argument(
        "--output",
        "-o",
        help="Name of the output file (default: test.txt)", 
        default="test.txt",
    )
    parser.add_argument(
        "--size",
        "-s",
        help="Size to create the test file in Gigabytes (Default: 5)", 
        default=5,
        type=int
    )
    parser.add_argument(
        "--speed",
        "-S",
        help="Write speed (Default: 500)", 
        default=500,
        type=int
    )
    args = parser.parse_args()
    generate_test_file(args.output, args.size, args.speed)

if __name__ == "__main__":
    main()
