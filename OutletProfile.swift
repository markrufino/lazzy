class OutletProfile: Mappable {

	var status: String
	var profile: profile
	var timestamp: Int
	var sample: Double
	var notification: notification
	var id: String
	var statusCode: Int

    func init() {
    }

    func required init(map: Map) {
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