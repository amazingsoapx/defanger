def defang_url(url):
    
    defanged_url = url.replace('.', '[.]').replace('@', '[@]').replace('https://', 'hxxps[://]').replace('http://', 'hxxp[://]')
    return defanged_url

while True: 
    user_input = input("Enter a URL/Email address to defang or type exit to quit.\nDefanger: ").lower().strip()
    if user_input.lower().strip() == 'exit':
        print("Exiting...")
        break
    
    defanged_data = defang_url(user_input)
    
    print("\nDefanged URL/Email Address:", defanged_data, "\n")
