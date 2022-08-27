

# import requests
#
# myrequest = requests.get ()
#
# result = myrequest.status_code
# print(result)

def w_name():
    counter = 5
    while counter > 0:
        my_file = open("names.txt", "a")
        my_file.write(input("Please enter a name:")+"\n")
        my_file.close()
        counter -= 1


w_name()


# def hello_name():
#     my_file = open("names.txt")
#     lines = my_file.readlines()
#     for line in lines:
#         print("hello " + line)
#
#
# hello_name()
# my_file = open("read_my_content2.txt", "w")
# my_file.write("Hello from mars the time here is :" + str(datetime.now()))
# my_file.close()


# for line in my_file.readlines():
#     print(line, end='')
# my_file.close
