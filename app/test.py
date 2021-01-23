      
      statuses
        200-{'status':'success'}
        401-{'status':'error'}

  /upload_photo [POST] 
          -token(str)
          -image(file)

      
      statuses
        200-{'status':'success'}
        401-{'status':'error'}
/get_city [GET]
	-city(str)

	statuses
      200-{
    reazer385@gmail&&com: "reazer385@gmail&&com",
    reazer386@gmail&&com: "reazer386@gmail&&com"
    coarts:{07865430680140b0bb345ceaf4a97cad{
                addr: 
                "Aksay"
                city: 
                "almaty"
                id: 
                "07865430680140b0bb345ceaf4a97cad"
                owner: 
                "alex"
                phone: 
                "87073373318"
                photo: 
                "https://firebasestorage.googleapis.com/v0/b/ora..."
                user: 
                "reazer385@gmail&&com"}
}


            }
      401-{'status':'error'}

	
