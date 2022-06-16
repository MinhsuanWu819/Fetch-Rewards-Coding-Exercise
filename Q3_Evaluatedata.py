import json


def parseReceipts():
    print("Parsing receipts...")
    # reading the JSON file
    with open('.//receipts.json', 'r', encoding='utf-8') as f:
        line = f.readline()
        no_price = 0
        no_quantity = 0
        while line:
            data = json.loads(line)

            receipt_id = data['_id']['$oid']

            if 'rewardsReceiptItemList' in data:
                for item in data["rewardsReceiptItemList"]:
                    finalPrice = -1
                    quantityPurchased = -1
                    if 'itemPrice' in item:
                        finalPrice = item['itemPrice']
                    if 'discountedItemPrice' in item:
                        finalPrice = item['discountedItemPrice']
                    if 'finalPrice' in item:
                        finalPrice = item['finalPrice']
                    if 'quantityPurchased' in item:
                        quantityPurchased = item['quantityPurchased']

                    if finalPrice == -1:
                        no_price += 1
                        print("there are no price in this item, receipt_id:" + receipt_id)
                    if quantityPurchased == -1:
                        no_quantity += 1
                        print("there are no quantityPurchased in this item, receipt_id:" + receipt_id)

            line = f.readline()
    print(no_price)
    print(no_quantity)
    f.close()


parseReceipts()
