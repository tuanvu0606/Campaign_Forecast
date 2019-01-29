require 'net/http'
require 'uri'

uri = URI.parse("https://api.mediasmart.io/api/analytics/availability/drilldown/size?limit=64&rules=countrycode=\\[AUT\\];image=\\[yes\\];size=\\[300x250,320x50,320x480,728x90\\]")
request = Net::HTTP::Get.new(uri)
request["Authorization"] = "m1e5enponocicyue9mv8nd4c93ugedwh"

req_options = {
  use_ssl: uri.scheme == "https",
}

response = Net::HTTP.start(uri.hostname, uri.port, req_options) do |http|
  http.request(request)
end

puts response
# response.code
# response.body