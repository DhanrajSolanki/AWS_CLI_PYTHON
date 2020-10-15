import os
import speech_recognition as sr
import pyttsx3
print()
pyttsx3.speak("I am John here is the menu for this program")
print("\t I am John here is the menu for this program")
print()
print("\n 1) Create a Key Pair")
print("\n 2) Create a Security Group")
print("\n 3) Assign Inbound Rule to Security Group")
print("\n 4) Launch an Instance")
print("\n 5) Create a Volume")
print("\n 6) Attach Volume with Instance")
print("\n 7) Describe your Instance")
print("\n 8) Start your Instance")
print("\n 9) Stop your Instance")
print()
while True:
	print()
	print("\t I am your assistant for AWS public cloud")
	pyttsx3.speak("I am your assistant for AWS public cloud")
	print()

	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Start Saying...")
		audio=r.listen(source)
		print("Listen done...")
	text=r.recognize_google(audio)
	print(text)

	if ("launch" in text) or ("deploy" in text) and ("instance" in text) or ("operating system" in text):
		pyttsx3.speak("Launching instances on aws cloud")
		os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id subnet-b6d5a3fa --security-group-ids sg-05ee2eb30732f7d10 --key-name mykey111")
	elif ("describe" in text) or ("detail" in text)  and ("instances" in text) or ("OS" in text):
		pyttsx3.speak("Showing Detail of instances")
		os.system("aws ec2 describe-instances")
	elif ("create a key pair" in text) or ("generate" in text) and ("key pair" in text) or ("key" in text):
		pyttsx3.speak("Creating Key Pair for you")
		os.system("aws ec2 create-key-pair --key-name mykey111")
	elif ("create a security" in text) or ("produce" in text) and ("security group" in text):
		pyttsx3.speak("Creating Security Group for you")
		os.system("aws ec2 create-security-group --group-name myawssec --description myawssecgroup")
	elif ("assign" in text) or ("allocate" in text) and ("inbound rule" in text) or ("rule" in text):
		pyttsx3.speak("Assigning inbound rule to your security group")
		os.system("aws ec2 authorize-security-group-ingress --group-name myawssec  --protocol tcp --port 80 --cidr 0.0.0.0/0")
	elif ("create a volume" in text) or ("create" in text) and ("volume" in text) or ("ebs volume" in text):
		pyttsx3.speak("Creating 1gb of volume for you")
		os.system("aws ec2 create-volume  --availability-zone ap-south-1b --size 1")
	elif ("attach" in text) or ("mount" in text) and ("volume" in text) or ("ebs" in text):
		pyttsx3.speak("Mounting ebs volume with your instance")
		os.system("aws ec2 attach-volume --device /dev/xvdf --instance-id i-0b8bc588a47077c9b --volume-id vol-0488410ea31597c24")
	elif ("start" in text) and ("instance" in text):
		pyttsx3.speak("Starting your stoped instance")
		os.system("aws ec2 start-instances --instance-ids ")
	elif ("stop" in text) and ("instance" in text):
		pyttsx3.speak("Stoping your started instance")
		os.system("aws ec2 stop-instances --instance-ids ")
	else:
		print("We are working on it")
		pyttsx3.speak("For more update you have to wait")