class profileObject: Mappable {
	var merchantCity: String
	var merchantCategoryCode: String
	var merchantName: String
	var countryCode: String
	var city: String
	var transactionCurrencyCode: String
	var contactPerson: String
	var faxNumber: String
	var state: String
	var phoneNumber: String
	var postCode: String
	var address: String
	var emailAddress: String
	var country: String
	var merchantId: String
	
    init() {
    }

    required init?(map: Map) {
    }
    
	func mapping(map: Map) {
		merchantCity <- map["merchantCity"]
		merchantCategoryCode <- map["merchantCategoryCode"]
		merchantName <- map["merchantName"]
		countryCode <- map["countryCode"]
		city <- map["city"]
		transactionCurrencyCode <- map["transactionCurrencyCode"]
		contactPerson <- map["contactPerson"]
		faxNumber <- map["faxNumber"]
		state <- map["state"]
		phoneNumber <- map["phoneNumber"]
		postCode <- map["postCode"]
		address <- map["address"]
		emailAddress <- map["emailAddress"]
		country <- map["country"]
		merchantId <- map["merchantId"]
	}
}