class notification: Mappable {

	var sendViaPushNotification: Bool
	var sendViaWebNotification: Bool
	var sendViaSms: Bool
	var sendViaEdcPos: Bool

    func init() {
    }

    func required init(map: Map) {
    }
    
	func mapping(map: Map) {
		sendViaPushNotification <- map["sendViaPushNotification"]
		sendViaWebNotification <- map["sendViaWebNotification"]
		sendViaSms <- map["sendViaSms"]
		sendViaEdcPos <- map["sendViaEdcPos"]
	}

}