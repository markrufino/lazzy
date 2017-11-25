class OutletProfile: Mappable {
	var status: String
	var profile: profileObject
	var timestamp: Int
	var sample: Double
	var notification: notificationObject
	var id: String
	var statusCode: Int
	
    init() {
    }

    required init?(map: Map) {
    }
    
	func mapping(map: Map) {
		status <- map["status"]
		profile <- map["profile"]
		timestamp <- map["timestamp"]
		sample <- map["sample"]
		notification <- map["notification"]
		id <- map["id"]
		statusCode <- map["statusCode"]
	}
}