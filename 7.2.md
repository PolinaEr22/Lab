def count_emails(filename):
    with open(filename, 'r') as file:
        emails = file.readlines()
    return len(emails), emails

def most_common_domain(emails):
    domains = {}
    for email in emails:
        domain = email.split('@')[-1].strip()
        domains[domain] = domains.get(domain, 0) + 1
    most_common_domain = max(domains, key=domains.get)
    return most_common_domain, domains[most_common_domain]

filename = "emails.txt"
total_emails, all_emails = count_emails(filename)
print(f"Количество email адресов в файле: {total_emails}")

most_common_domain, num_users = most_common_domain(all_emails)
print(f"Наиболее часто встречающийся домен: {most_common_domain}, количество пользователей: {num_users}")
