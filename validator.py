
while True:
   input_email = input('please enter your email:  ')

   pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
   
   check_input = pattern.search(input_email)

   if check_input:
       print('your email is valid')
       break
   else:
        print('invalid email,please try again')
        continue

while True:
    input_password = input('please enter your password:  ')

    pattern2 = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")

    check_input2 = pattern2.search(input_password)

    if check_input2:
        print('your password is valid')
        break
    else:
        print('please enter an appropriate password') 
