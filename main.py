from barcode import Code39
from barcode.writer import ImageWriter
import http.server
import socketserver
import json

## Set basic variables
PORT = 8111
DIRECTORY = "barcodes"
pythonObj = {
  "count": 0,
  "files": []
}

## Sample UPS Tracking Codes
barcodeData = ["1Z6V68R80371450682", "1Z5RY338YW56985952", "1Z47618Y0379426705", "1Z3569V20300283205", "1Z0Y01V10396466244", "1Z21R00V1332083713", "1ZA934A50303692992", "1Z383RA10290004858", "1Z0RV4470214939266", "1ZA09E850392263996", "1Z8A81F84208340920", "1ZY83Y114297946891", "1Z1WE3501390141133", "1ZR0541Y0304798731", "1Z806YY40229387582", "1Z3Y18900218467621", "1Z722F080300445497", "1Z78A20E0410114174", "1Z81F9A00332436406", "1ZX799470398513854", "1ZX799390370765659", "1ZR43Y850370383658", "1Z247A7F0292865097", "1Z0X07944219266842", "1Z814VR64200475357", "1Z852A710395727942", "1Z6A28040311556175", "1Z8Y82R30367773334", "1Z82V7481315944379", "1Z548YW10311014033", "1ZY393360317879266", "1Z1WE1021375248785", "1Z57FA349086582463", "1Z6V68R8YW77651321", "1Z834AW00395252149", "1ZY549V70249827199", "1ZY584440200058997", "1ZR7828Y0393365737", "1ZW8X8500302612602", "1ZW8X8500302612317", "1ZR43Y850366957895", "1ZA2027W0368036283", "1Z6R46A10305285043", "1Z1AF5680390383483", "1Z6R46A10304079223", "1Z6R46A10337159996", "1Z6AE646A828895410", "1Z8W0R000396509676", "1Z6R46A10236633315", "1Z21E574PW16626449"]

## Generate the barcode images
for data in barcodeData:
    with open(DIRECTORY + '/code39-' + data + '.png', 'wb') as f:
        print("Generating barcode image at: " + DIRECTORY + "code39-" + data + ".png")
        Code39(data, writer=ImageWriter()).write(f)
        newCount = pythonObj["count"] + 1
        pythonObj["count"] = newCount
        pythonObj['files'].append("code39-" + data + ".png")

# Write JSON file
with open(DIRECTORY + '/barcodes.json', 'w') as outfile:
    json.dump(pythonObj, outfile)

## Configure the HTTP Server
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

## Start the HTTP Server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()