from pymongo import MongoClient


class createjson:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["detector_data"]
        self.collection = self.db["board"]
        self.data_dict = dict()
    
    def execute(self):
        board_info = self.collection.find()
        for info in board_info:
            self.data_dict[info["board_id"]] = info["CSV_list"]
        with open("board.json","w") as f:
            f.write(str(self.data_dict).replace("'",'"'))

if __name__ == "__main__":
    createjson().execute()