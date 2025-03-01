import qrcode

#Taking UPI ID As a Input
upi_id = input("Enter your UPI Id = ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#Defing the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1235'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1235'  #f' it is f string
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1235'

#Creates QR codes for each payments app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
#Save the QR cde to image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()