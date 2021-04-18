import json

filename = './flu_tweets.json'


# open the json file
def read_json(file: str) -> list:
    with open(file, encoding="utf8") as f:
        data = json.load(f)
        return data


result = read_json()
print(type(result))
print(result)

# if __name__ == '__main__':
#     main()
