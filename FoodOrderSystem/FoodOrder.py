from asyncore import read
import json
import datetime

def register_user(user_json,name,password,age,phn):
	user={

	     "id":1,
	     "name":name,
	     "password":password,
	     "age":age,
	     "phone_number":phn,
	     "order_history":{}



	}
	try:
		file=open(user_json,'r+')
		content=json.load(file)
		for i in range(len(content)):
			if content[i]["phone_number"]==phn:
				file.close()
				return "user already exists"
		else:
			user["id"]=len(content)+1
			content.append(user)
	except JSONDecodeError:
		content=[]
		content.append(user)
	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()
	return "Success"

def user_order_history(user_json,user_id):
	file=open(user_json,'r+')
	content=json.load(file)
	for i in range(len(content)):
		if content[i]["id"]==user_id:
			print("order history")
			print("Date | Order")
			for i,j in content[i]["order_history"].items():
				print(f"{i} | {j}")
			file.close()
			return True
	file.close()
	return False

def user_place_order(user_json,food_json,user_id,food_id,quantity):
	date=datetime.datetime.today().strftime('%m-%d-%Y')
	#user.json file
	file=open(user_json,'r+')
	content=json.load(file)
	#fooditems.json file
	file1=open(food_json,'r+')
	content1=json.load(file1)

	for i in range(len(content1)):
		if content1[i]["id"]==food_id:
			if content1[i]["no_of_plates"]>quantity:
				for j in range(len(content)):
					if content[j]["id"]==user_id:
						content1[i]["no_of_plates"]-=quantity
						if date not in content[j]["order_history"]:
							content[j]["order_history"][date]=[content1[i]["name"]]
						else:
							content[j]["order_history"][date].append(content1[i]["name"])
			else:
				print("please enter less quantity")
				break

			
		else:
			print("food is not available")
			break
	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()

	file1.seek(0)
	file1.truncate()
	json.dump(content1,file1,indent=4)
	file1.close()

	return "Success"




def add_food(user_json,food_name,no_of_plates=1):
	food={

	      "id":1,
	      "name":food_name,
	      "no_of_plates":no_of_plates



	}
	try:
		file=open(user_json,'r+')
		content=json.load(file)
		for i in range(len(content)):
			if content[i]["name"]==food_name:
				file.close
				return "Food already Present in Menu"
		food["id"]=len(content)+1
		content.append(food)
	except JSONDecodeError:
		content=[]
		content.append(food)

	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()
	return "Success"

def update_food(food_json,food_id,no_of_plates=1):
	file=open(food_json,'r+')
	content=json.load(file)
	for i in range(len(content)):
		if content[i]["id"]==food_id:
			content[i]["no_of_plates"]+=no_of_plates
			break
	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()
	return "Success"

def remove_food(file_json,food_id):
    file=open(file_json,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"]==food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "Success"
    return "please enter valid food id"

def read_food(file_json):
	file=open(file_json,'r+')
	content=json.load(file)
	print("Menu")
	for i in range(len(content)):
		print(f"{content[i]['id']}-{content[i]['name']}-{content[i]['no_of_plates']} plates")

	file.close()
	return "Success"



val=input("Do You Want To Order Food y/n:")
while val.lower()=='y':
	print("Menu:")
	print("1.Register")
	print("2.Login")
	print("3.Exit")
	val1=int(input("Choose options and enter Herer:"))
	if val1==1:
#-------------Register-------------------
		print()
		name=input("Enter Name")
		password=input("Enter password")
		age=input("Enter Age")
		phone=input("Enter Phone Number")
		print(register_user("users.json",name,password,age,phone))

	elif val1==2:
#-------------Login-------------------	
		print()
		while True:
			print("1.Users")
			print("2.Admin Login")
			print("3.Exit")
			val2=int(input("Enter Option Here:"))
			if val2==1:
			#start----------users-----------------------------------------------------------------
				print("------users------")
				user=input("Enter Name")
				password=input("Enter password")
				file=open("users.json",'r+')
				content=json.load(file)
				for i in range(len(content)):
					if content[i]["name"]==user:
						if content[i]["password"]==password:
							while True:
								print("1.view menu")
								print("2.place order")
								print("3.show history")
								print("4.update profile")
								print("5.Exit")
								val3=int(input("Enter Options"))

								if val3==1:
									#--------menu---------------------
									print("Menu:")
									read_food("fooditem.json")	
									#--------menu---------------------
								elif val3==2:
									#-----------place order----------------
									print("order")
									#user_place_order(user_json,food_json,user_id,food_id,quantity):
									userid=int(input("Enter Userid"))
									foodid=int(input("Enter Food Id"))
									quantity=int(input("Enter quantity"))
									print(user_place_order("users.json","fooditem.json",userid,foodid,quantity))
									#-----------place order-----------------

								elif val3==3:
									#--------food history--------
									print("Food History")
									userid=int(input("Enter Userid"))
									user_order_history("users.json",userid)
									#--------food history--------

								elif val3==4:
									#start-----update Profile------------------------
									print("update profile")
									print("1.Update Name")
									print("2.Update password")
									print("3.update Phone")
									print("4.Exit")
									val4=int(input("Enter the option Here:"))
									if val4==1:
										#start-----update name----------
										userid=int(input("Enter Userid"))
										name=input("Enter Name to Update")
										file=open("users.json","r+")
										content=json.load(file)
										if content[i]["id"]==userid:
											content[i]["name"]=name

											file.seek(0)
											file.truncate()
											json.dump(content,file,indent=4)
											file.close()
											print("Name Updated")

										else:
											print("invalid userid")
										#end------update name---------------


									elif val4==2:
										#start------update password------------
										print("Update password")
										userid=int(input("Enter Userid"))
										password=input("Enter password to Update")
										file=open("users.json","r+")
										content=json.load(file)
										if content[i]["id"]==userid:
											content[i]["password"]=password

											file.seek(0)
											file.truncate()
											json.dump(content,file,indent=4)
											file.close()
											print("Password Updated")

										else:
											print("invalid password")
										#End------update password------------

									elif val4==3:
										#Start---------update phone number-------------
										print("Update phone")
										userid=int(input("Enter Userid"))
										phone=input("Enter phone Number to Update")
										file=open("users.json","r+")
										content=json.load(file)
										if content[i]["id"]==userid:
											content[i]["phone"]=phone

											file.seek(0)
											file.truncate()
											json.dump(content,file,indent=4)
											file.close()
											print("phone Number Updated")

										else:
											print("invalid userid")
										#End---------update phone number-------------

									elif val4==4:
										break
									#End-------------update profile-------------------------------
								elif val3==5:
									print("Bye")
									break



						else:
							print("Wrong password")

					else:
						print("Wrong Username")
			#End----------users-----------------------------------------------------------------
			elif val2==2:
			#start-------admin login-------------------------------------------------------------
				print("---------Admin--------")
				user=input("Enter Username:")
				password=input("Enter Password:")
				file=open("admin.json","r+")
				content=json.load(file)
				if content["name"]==user:
					if content["password"]==password:
						while True:
							print()
							print("1.Add Food")
							print("2.Edit Food")
							print("3.view Food")
							print("4.Remove Food")
							print("5.Exit")
							val3=int(input("Enter option Here:"))
							#start----------AddFood-----------
							if val3==1:
								print()
								foodname=input("Enter Food Name")
								quantity=int(input("Enter quantity"))
								print(add_food("fooditem.json",foodname,quantity))
							elif val3==2:
								print()
								foodid=int(input("Enter FoodId"))
								quantity=int(input("Enter number of Qyantity"))
								print(update_food("fooditem.json",foodid,no_of_plates=1))
							elif val3==3:
								print()
								read_food("fooditem.json")
							elif val3==4:
								print()
								foodid=int(input("Enter food id"))
								print(remove_food("fooditem.json",foodid))
							elif val==5:
								break
						    	
					else:
						print("invalid password")
				else:
					print("invalid Username")    
		    #End-------admin login-------------------------------------------------------------
			elif val2==3:
				print("Bye")
				break
	elif val1==3:
		print("Visit Again")
		break






		


