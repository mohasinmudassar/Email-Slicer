email = input ("what is your email address? :  ").strip()

user_name = email[: email.index("@")]

domain_name = email [ email.index("@")+1 :]

output = " Your username is '{}'and your domain name is '{}'" . format (user_name,domain_name)

print (output)